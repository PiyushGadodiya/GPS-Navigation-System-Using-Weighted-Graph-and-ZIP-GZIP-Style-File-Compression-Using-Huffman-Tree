
import heapq
from collections import Counter
from itertools import count


class HuffmanNode:
    def __init__(self, char=None, left=None, right=None):
        self.char = char
        self.left = left
        self.right = right

    def is_leaf(self):
        return self.left is None and self.right is None


class HuffmanCompression:
    def __init__(self):
        self.codes = {}
        self.root = None

    def build_tree(self, text):
        if not text:
            self.root = None
            self.codes = {}
            return

        frequency = Counter(text)
        sequence = count()
        heap = []

        for char, freq in frequency.items():
            node = HuffmanNode(char)
            heapq.heappush(heap, (freq, next(sequence), node))

        while len(heap) > 1:
            freq1, _, left = heapq.heappop(heap)
            freq2, _, right = heapq.heappop(heap)

            merged = HuffmanNode(left=left, right=right)

            heapq.heappush(
                heap,
                (freq1 + freq2, next(sequence), merged)
            )

        self.root = heap[0][2]
        self.codes = {}

        def generate_codes(node, code):
            if node.is_leaf():
                self.codes[node.char] = code or "0"
                return

            generate_codes(node.left, code + "0")
            generate_codes(node.right, code + "1")

        generate_codes(self.root, "")

    def compress(self, text):
        self.build_tree(text)

        encoded = "".join(self.codes[char] for char in text)
        return encoded

    def decompress(self, encoded):
        if self.root is None:
            return ""

        # Handle text containing only one unique character
        if self.root.is_leaf():
            return self.root.char * len(encoded)

        result = []
        node = self.root

        for bit in encoded:
            if bit == "0":
                node = node.left
            else:
                node = node.right

            if node.is_leaf():
                result.append(node.char)
                node = self.root

        return "".join(result)


# Main program
huffman = HuffmanCompression()

while True:
    print("\n===== Huffman File Compression =====")
    print("1. Compress Text")
    print("2. Decompress Text")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        text = input("Enter text: ")

        encoded = huffman.compress(text)

        print("\nCharacter Frequencies and Codes:")
        for char, code in huffman.codes.items():
            print(repr(char), ":", code)

        print("\nOriginal Text:", text)
        print("Encoded Bits:", encoded)
        print("Original Size:", len(text) * 8, "bits")
        print("Compressed Data Size:", len(encoded), "bits")
        print(
            "Note: Tree and code-table storage are not included "
            "in the compressed size."
        )

    elif choice == "2":
        encoded = input("Enter encoded bits: ")
        decoded = huffman.decompress(encoded)
        print("Decompressed Text:", decoded)

    elif choice == "3":
        print("Exiting Compression System.")
        break

    else:
        print("Invalid choice!")
