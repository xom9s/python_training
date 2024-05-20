class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adjacency_matrix = [[0] * num_vertices for _ in range(num_vertices)]

    def add_edge(self, vertex1, vertex2):
        if 0 <= vertex1 < self.num_vertices and 0 <= vertex2 < self.num_vertices:
            self.adjacency_matrix[vertex1][vertex2] = 1
            self.adjacency_matrix[vertex2][vertex1] = 1

    def remove_edge(self, vertex1, vertex2):
        if 0 <= vertex1 < self.num_vertices and 0 <= vertex2 < self.num_vertices:
            self.adjacency_matrix[vertex1][vertex2] = 0
            self.adjacency_matrix[vertex2][vertex1] = 0

    def display(self):
        for row in self.adjacency_matrix:
            print(row)

# Example usage
num_vertices = 3
graph = Graph(num_vertices)
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)

graph.display()

# Removing an edge
graph.remove_edge(0, 1)

graph.display()