#!/usr/bin/env python
# coding: utf-8

# In[50]:


#Proyecto Final de Estructura de Datos

#Rutas Utilizando Grafos

#Urbano Iguala

#9-744-1120


# In[23]:


import pandas as pd
import numpy as np
import networkx as nx
import queue


# In[24]:


df = pd.read_csv('C:\\Users\\uiguala\\Desktop\\Rutas.csv', index_col=None)
df.head()


# In[25]:


Rutas = nx.from_pandas_edgelist(df,source='Origen',target='Destino',edge_attr='Lengh')


# In[26]:


Rutas.nodes()


# In[27]:


Rutas.edges()


# In[28]:


Rutas.order()


# In[38]:


ciudad = Rutas.subgraph(['Coruna', 'Valladolid', 'Vigo', 'Couna', 'Bilbao', 'Madrid', 'Oviedo', 'Zaragoza', 'Barcelona', 'Badajoz', 'Jaen', 'Albacete', 'Cadiz', 'Sevilla', 'Granada', 'Murcia', 'Valencia', 'Gerona'])
nx.draw(ciudad, with_labels=True)


# In[39]:


class MyQUEUE:
    def __init__(self): 
        self.holder = [] 
    def enqueue(self,val): 
        self.holder.append(val) 
    def dequeue(self): 
        val = None 
        try: 
            val = self.holder[0] 
            if len(self.holder) == 1: 
                self.holder = [] 
            else: 
                self.holder = self.holder[1:] 
        except: 
            pass 
        return val 
    def IsEmpty(self): 
        result = False 
        if len(self.holder) == 0: 
            result = True 
        return result 
    
path_queue = MyQUEUE() 

def BFS(graph,start,end,q): 
    temp_path = [start] 
    
    q.enqueue(temp_path)
    
    while q.IsEmpty() == False: 
        tmp_path = q.dequeue() 
        last_node = tmp_path[len(tmp_path)-1] 
        if last_node == end: 
            print ("\nRuta Disponible : ",tmp_path)
        for link_node in graph[last_node]: 
            if link_node not in tmp_path: 
                #new_path = [] 
                new_path = tmp_path + [link_node] 
                q.enqueue(new_path) 
BFS(Rutas,"Sevilla","Coruna",path_queue)


# In[40]:


djk_path=nx.dijkstra_path(Rutas, source='Sevilla',target='Coruna',weight=False)
djk_path


# In[41]:


ruta01 = Rutas.subgraph(['Sevilla', 'Jaen', 'Madrid', 'Valladolid', 'Coruna']) 
nx.draw(ruta01, with_labels=True)


# In[53]:


ruta02 = Rutas.subgraph(['Sevilla', 'Granada', 'Jaen', 'Madrid', 'Valladolid', 'Vigo', 'Coruna']) 
nx.draw(ruta02, with_labels=True)


# In[44]:


ruta03 = Rutas.subgraph(['Sevilla', 'Jaen', 'Granada', 'Murcia', 'Albacete', 'Valencia', 'Barcelona', 'Zaragoza', 'Madrid', 'Bilbao', 'Valladolid', 'Vigo', 'Coruna']) 
nx.draw(ruta03, with_labels=True)


# In[45]:


ruta04 = Rutas.subgraph(['Sevilla', 'Jaen', 'Granada', 'Murcia', 'Valencia', 'Barcelona', 'Zaragoza', 'Bilbao', 'Madrid', 'Valladolid', 'Vigo', 'Coruna']) 
nx.draw(ruta04, with_labels=True)


# In[49]:


ruta05 = Rutas.subgraph(['Sevilla', 'Granada', 'Murcia', 'Albacete', 'Valencia', 'Barcelona', 'Zaragoza', 'Bilbao', 'Valladolid', 'Vigo', 'Coruna']) 
nx.draw(ruta05, with_labels=True)


# In[54]:


ruta06 = Rutas.subgraph(['Sevilla', 'Jaen', 'Granada', 'Murcia', 'Albacete', 'Madrid', 'Bilbao', 'Valladolid', 'Vigo', 'Coruna']) 
nx.draw(ruta06, with_labels=True)


# In[ ]:




