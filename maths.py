# def vending_machine(money):
#     if money >=30:
#       return "Snack.😘"
#     else:
#       return "No snack😒"  

# print(vending_machine(76))


import networkx as nx
import matplotlib.pyplot as plt  

#Draw a "classroom graph" where nodes are students and edges show who shares snacks. guide me on this
G = nx.Graph()
students =["Conso", "Ken", "Alice","Jane"]
G.add_nodes_from(students)
G.add_edges_from([("Conso","Alice"),("Alice", "Ken"), ("Ken","Conso"),("Alice","Jane"),("Jane","Ken")])

plt.figure(figsize=(5,5))

nx.draw(G, with_labels=True, node_color="lightgreen", edge_color="red",font_size=10, font_weight="bold")

plt.show()

# #pip install networkx
