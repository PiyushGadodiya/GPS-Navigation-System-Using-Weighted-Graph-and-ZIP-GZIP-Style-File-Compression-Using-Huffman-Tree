
import heapq

class GPSNavigation:
    def __init__(self):
        self.graph = {}

    def add_road(self, source, destination, distance):
        if source not in self.graph:
            self.graph[source] = []

        if destination not in self.graph:
            self.graph[destination] = []

        self.graph[source].append((destination, distance))
        self.graph[destination].append((source, distance))

    def display_map(self):
        print("\nCity Map:")
        for location, roads in self.graph.items():
            print(location, "->", roads)

    def shortest_path(self, start, end):
        if start not in self.graph or end not in self.graph:
            print("Location not found!")
            return

        distances = {node: float('inf') for node in self.graph}
        previous = {}

        distances[start] = 0
        priority_queue = [(0, start)]

        while priority_queue:
            current_distance, current_node = heapq.heappop(
                priority_queue
            )

            if current_distance > distances[current_node]:
                continue

            if current_node == end:
                break

            for neighbor, weight in self.graph[current_node]:
                new_distance = current_distance + weight

                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    previous[neighbor] = current_node

                    heapq.heappush(
                        priority_queue,
                        (new_distance, neighbor)
                    )

        if distances[end] == float('inf'):
            print("No route available!")
            return

        path = []
        node = end

        while node != start:
            path.append(node)
            node = previous[node]

        path.append(start)
        path.reverse()

        print("\nShortest Route:", " -> ".join(path))
        print("Total Distance:", distances[end], "km")


# Main program
gps = GPSNavigation()

# Add roads and distances
gps.add_road("College", "Kothrud", 4)
gps.add_road("College", "Swargate", 7)
gps.add_road("Kothrud", "Deccan", 3)
gps.add_road("Deccan", "Shivajinagar", 2)
gps.add_road("Swargate", "Shivajinagar", 5)
gps.add_road("Kothrud", "Shivajinagar", 8)

while True:
    print("\n===== GPS Navigation System =====")
    print("1. Display City Map")
    print("2. Find Shortest Route")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        gps.display_map()

    elif choice == "2":
        start = input("Enter starting location: ")
        end = input("Enter destination: ")
        gps.shortest_path(start, end)

    elif choice == "3":
        print("Exiting GPS System.")
        break

    else:
        print("Invalid choice!")
