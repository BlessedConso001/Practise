# def vending_machine(money):
#     if money >=30:
#       return "Snack.😘"
#     else:
#       return "No snack😒"  

# print(vending_machine(76))


#import networkx as nx
#import matplotlib.pyplot as plt  
#Draw a "classroom graph" where nodes are students and edges show who shares snacks. guide me on this
#G = nx.Graph()

import matplotlib
import matplotlib.pyplot as plt  
matplotlib.use('TkAgg')
exams =[1, 2, 3, 4, 5]
maths_scores = [50, 85, 45, 20,89]
plt.scatter(exams,maths_scores, color="blue")
plt.xlabel("exams")
plt.ylabel("maths_scores")
plt.title("opener exam maths score")
plt.show()

#G.add_nodes_from(students)
#G.add_edges_from([("Conso","Alice"),("Alice", "Ken"), ("Ken","Conso"),("Alice","Jane"),("Jane","Ken")])

#plt.figure(figsize=(5,5))

#nx.draw(G, with_labels=True, node_color="lightgreen", edge_color="red",font_size=10, font_weight="bold")

#plt.show()

# #pip install networkx
