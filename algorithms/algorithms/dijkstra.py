import heapq

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_edge(self, from_vertex, to_vertex, weight):
        if from_vertex not in self.vertices:
            self.vertices[from_vertex] = {}
        if to_vertex not in self.vertices:
            self.vertices[to_vertex] = {}
        self.vertices[from_vertex][to_vertex] = weight
        self.vertices[to_vertex][from_vertex] = weight  # If the graph is undirected

class Dijkstra:
    def __init__(self, graph):
        self.graph = graph.vertices

    def calculate_distances(self, start_vertex):
        distances = {vertex: float('infinity') for vertex in self.graph}
        distances[start_vertex] = 0
        priority_queue = [(0, start_vertex)]

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in self.graph[current_vertex].items():
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances

# Example usage:
graph = Graph()
graph.add_edge('A', 'B', 1)
graph.add_edge('A', 'C', 4)
graph.add_edge('B', 'C', 2)
graph.add_edge('B', 'D', 5)
graph.add_edge('C', 'D', 1)

dijkstra = Dijkstra(graph)
distances = dijkstra.calculate_distances('A')
print(distances)
