import networkx as nx

# Create a graph
G = nx.Graph()

# Define the (8x4) matrix
matrix = [['q', 'w', 'e', 'r','<'],
          ['t', 'y', 'u', 'I','?'],
          ['o', 'P', 'A', 'S','+'],
          ['d', 'F', 'G', 'h','-'],
          ['j', 'k', 'L', 'z',')'],
          ['X', 'C', 'v', 'b','('],
          ['n', 'm', '!', '@','*'],
          ['#', '$', '%', '^','&']]

# Add nodes and edges to the graph based on matrix
rows, cols = len(matrix), len(matrix[0])
for i in range(rows):
    for j in range(cols):
        node = matrix[i][j]
        G.add_node(node)

        # Connect adjacent nodes
        if i > 0:
            G.add_edge(matrix[i-1][j], node)
        if j > 0:
            G.add_edge(matrix[i][j-1], node)

# Function to find coordinates of a string
def find_coordinates(search_string):
    coordinates = [(i, j) for i in range(rows) for j in range(cols) if matrix[i][j].lower() in search_string.lower()]
    return coordinates

# Input string
input_name = input("Input: ")

# Find and print coordinates
output_coordinates = find_coordinates(input_name)
print(f"Output: {output_coordinates}")