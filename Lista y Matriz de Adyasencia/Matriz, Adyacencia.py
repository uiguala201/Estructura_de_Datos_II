#*Urbano Iguala, 9-744-1120*
#*Estructura de Datos II*
#*Matriz de Adyacencia*

import array
import queue
import requests
import json
import pprint
import numpy as np
import string
import random

    
class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost = 0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def get_vertices(self):
        return self.vert_dict.keys()

if __name__ == '__main__':



    g = Graph()
    g.add_vertex('A')
    g.add_vertex('B')
    g.add_vertex('C')
    g.add_vertex('D')
    g.add_vertex('E')
    g.add_vertex('F')
 
    g.add_edge('A','A',6)
    g.add_edge('A','B',4)
    g.add_edge('B','B',4)
    g.add_edge('B','C',5)
    g.add_edge('B','E',3)
    g.add_edge('C','C',5)
    g.add_edge('C','D',1)
    g.add_edge('C','F',2)
    g.add_edge('D','D',1)
    g.add_edge('D','F',2)
    g.add_edge('E','B',4)
    g.add_edge('E','E',3)
    g.add_edge('E','F',2)
    g.add_edge('F','C',5)
    g.add_edge('F','D',1)
    g.add_edge('F','E',3)
    g.add_edge('F','F',2)
    
 
    for v in g:
        for w in v.get_connections():
            vid = v.get_id()
            wid = w.get_id()
            print ('( %s , %s, %3s)'  % ( vid, wid, v.get_weight(w)))
    for v in g:
        print ('g.vert_dict[%s]=%s' %(v.get_id(), g.vert_dict[v.get_id()]))
