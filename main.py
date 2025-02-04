import networkx as nx
import matplotlib.pyplot as plt

def print_hi(name):
    # n = 20
#     # p = 0.15
#     # G = nx.erdos_renyi_graph(n, p, directed=True)
#     #
#     #
#     # nx.draw_spring(G, with_labels=True)
#     # plt.show()

    G = nx.Graph()
    G.add_edge(1, 2, color='red', weight=0.84, size=300)
    G.add_edge(2, 3, color='blue', weight=0.1, size=300)
    G.add_edge(3, 4, color='blue', weight=1, size=300)
    G.add_edge(1, 3, color='blue', weight=1, size=300)
    print(G[1][2]['color'])

    print(nx.dijkstra_path(G,1, 4))
    nx.draw_circular(G, with_labels=True)
    plt.show()



if __name__ == '__main__':
    print_hi('PyCharm')


