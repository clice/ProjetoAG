# from graph import Graph
#
# # Example usage:
# graph = Graph()
# graph.add_nodes([1, 2, 3, 4, 5])
# graph.add_edges([(1, 2), (1, 3), (2, 4), (3, 4), (4, 5)])
# graph.draw()

import networkx as nx
import random

def generate_random_map():
    # Generate a random number of vertices (locations)
    num_vertices = random.randint(5, 20)  # You can adjust the range as per your requirement

    # Create an empty graph to represent the map
    game_map = nx.Graph()

    # Add vertices (locations) to the map
    for i in range(num_vertices):
        # Add a vertex with a random position
        x = random.uniform(0, 100)  # Random x-coordinate (adjust the range as needed)
        y = random.uniform(0, 100)  # Random y-coordinate (adjust the range as needed)
        game_map.add_node(i, pos=(x, y))  # Node index and position as attributes

    # Add random edges between vertices (locations)
    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            if random.random() < 0.3:  # Adjust the probability of having a connection between locations
                game_map.add_edge(i, j)

    return game_map

# Generate a random map
random_map = generate_random_map()

# Draw the map
import matplotlib.pyplot as plt

pos = nx.get_node_attributes(random_map, 'pos')
nx.draw(random_map, pos, with_labels=True, node_size=300, node_color='skyblue', font_size=10)
plt.show()
