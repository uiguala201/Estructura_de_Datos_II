#!/usr/bin/env python
# coding: utf-8

# In[2]:


#*Urbano Iguala, 9-744-1120*
#*Estructura de Datos II*
#*Tarea03*

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
    g.add_vertex('Coruña')
    g.add_vertex('Vigo')
    g.add_vertex('Valladolid')
    g.add_vertex('Oviedo')
    g.add_vertex('Bilbao')
    g.add_vertex('Zaragoza')
    g.add_vertex('Madrid')
    g.add_vertex('Badajoz')
    g.add_vertex('Cadiz')
    g.add_vertex('Sevilla')
    g.add_vertex('Jaen')
    g.add_vertex('Granada')
    g.add_vertex('Murcia')
    g.add_vertex('Albacete')
    g.add_vertex('Valencia')
    g.add_vertex('Barcelona')
    g.add_vertex('Gerona')
   
    
 
    g.add_edge('Coruña','Coruña',455)
    g.add_edge('Coruña','Valladolid',455)
    g.add_edge('Coruña','Vigo',171)
    g.add_edge('Vigo','Vigo',356)
    g.add_edge('Vigo','Coruña',171)
    g.add_edge('Vigo','Valladolid',356)
    g.add_edge('Valladolid','Valladolid',455)
    g.add_edge('Valladolid','Coruña',455)
    g.add_edge('Valladolid','Vigo',356)
    g.add_edge('Valladolid','Bilbao',280)
    g.add_edge('Valladolid','Madrid',193)
    g.add_edge('Oviedo','Oviedo',304)
    g.add_edge('Oviedo','Bilbao',304)
    g.add_edge('Bilbao','Bilbao',395)
    g.add_edge('Bilbao','Oviedo',304)
    g.add_edge('Bilbao','Valladolid',280)
    g.add_edge('Bilbao','Madrid',395)
    g.add_edge('Bilbao','Zaragoza',324)
    g.add_edge('Zaragoza','Zaragoza',325)
    g.add_edge('Zaragoza','Madrid',325)
    g.add_edge('Zaragoza','Bilbao',324)
    g.add_edge('Zaragoza','Barcelona',296)
    g.add_edge('Madrid','Madrid',403)
    g.add_edge('Madrid','Badajoz',403)
    g.add_edge('Madrid','Valladolid',193)
    g.add_edge('Madrid','Bilbao',395)
    g.add_edge('Madrid','Zaragoza',325)
    g.add_edge('Madrid','Jaen',335)
    g.add_edge('Madrid','Albacete',251)
    g.add_edge('Badajoz','Badajoz',403)
    g.add_edge('Badajoz','Madrid',403)
    g.add_edge('Cadiz','Cadiz',125)
    g.add_edge('Cadiz','Sevilla',125)
    g.add_edge('Sevilla','Sevilla',256)
    g.add_edge('Sevilla','Granada',256)
    g.add_edge('Sevilla','Jaen',242)
    g.add_edge('Jaen','Jaen',335)
    g.add_edge('Jaen','Madrid',335)
    g.add_edge('Jaen','Sevilla',242)
    g.add_edge('Jaen','Granada',99)
    g.add_edge('Granada','Granada',278)
    g.add_edge('Granada','Sevilla',256)
    g.add_edge('Granada','Jaen',99)
    g.add_edge('Granada','Murcia',278)
    g.add_edge('Murcia','Murcia',278)
    g.add_edge('Murcia','Granada',278)
    g.add_edge('Murcia','Albacete',150)
    g.add_edge('Murcia','Valencia',241)
    g.add_edge('Albacete','Albacete',251)
    g.add_edge('Albacete','Madrid',251)
    g.add_edge('Albacete','Murcia',150)
    g.add_edge('Albacete','Valencia',191)
    g.add_edge('Valencia','Valencia',349)
    g.add_edge('Valencia','Albacete',191)
    g.add_edge('Valencia','Murcia',241)
    g.add_edge('Valencia','Barcelona',349)
    g.add_edge('Barcelona','Barcelona',349)
    g.add_edge('Barcelona','Valencia',349)
    g.add_edge('Barcelona','Zaragoza',296)
    g.add_edge('Barcelona','Gerona',100)
    g.add_edge('Gerona','Gerona',100)
    g.add_edge('Gerona','Barcelona',100)
    
    

    
 
    for v in g:
        for w in v.get_connections():
            vid = v.get_id()
            wid = w.get_id()
            print ('( %s , %s, %3s)'  % ( vid, wid, v.get_weight(w)))
    for v in g:
        print ('g.vert_dict[%s]=%s' %(v.get_id(), g.vert_dict[v.get_id()]))


# In[ ]:




