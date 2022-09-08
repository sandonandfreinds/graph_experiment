import csv
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib import pylab
import plotly.graph_objects as go
   

class GraphVisualization:
   
    def __init__(self):
          
        # visual is a list which stores all 
        # the set of edges that constitutes a
        # graph
        self.visual = []
          
    # addEdge function inputs the vertices of an
    # edge and appends it to the visual list
    def addEdge(self, a, b):
        temp = [a, b]
        self.visual.append(temp)
          
    # In visualize function G is an object of
    # class Graph given by networkx G.add_edges_from(visual)
    # creates a graph with a given list
    # nx.draw_networkx(G) - plots the graph
    # plt.show() - displays the graph
    def visualize(self):
        G = nx.Graph()
        G.add_edges_from(self.visual)
        nx.draw_networkx(G)
        #plt.figure(num=None, figsize=(100, 100), dpi=80)
        plt.savefig(r'C:\Users\adair\OneDrive\Desktop\test.png',figsize=(100,100), dpi=2000)
        plt.show()
####
file_path=r'file'
table_dict = {}
with open(r'C:\Users\adair\Downloads\Change_request.csv') as file:
    data = csv.reader(file, delimiter=',')
    for row in data:
        dependency=row[1].split('|')
        buildtime=row[2].split(':')
        buildtime=int((row[2].split(':'))[0])*(60*60)+int((row[2].split(':'))[1])*(60)+int((row[2].split(':'))[2])
        table_dict[row[0]] = {'dependency':dependency, 'buildtime':buildtime}
####
G = GraphVisualization()
j = 0
for table in table_dict:
    if table_dict[table]['dependency'] != '':
        for i in table_dict[table]['dependency']:
            G.addEdge(table, i)
    else:
        G.addEdge(table, table)
    j += 1
    if j == 30:
        break
 G.visualize()
