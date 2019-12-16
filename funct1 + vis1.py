#!/usr/bin/env python
# coding: utf-8

# ### <font color= purple>Distance graph - file containing physical distances between each pair of nodes. Each line follows this structure:
#     (Id_Node1, Id_Node2, d(Id_Node1,Id_Node2)), where d(x,y) is the physical distance between x and y.
# 
# ### <font color = brown>Travel time graph - file containing time distances between each pair of nodes. Each line follows this structure: 
#     (Node1, Node2, t(Id_Node1, Id_Node2)), where t(x,y) is the time distance between x and y.
# 
# 
# ### <font color = green> Node information file - file containing node coordinates. Each line follows this structure: 
#     (Id_Node, Latitude, Longitude)
# 
# 
# 

# # <font color=red> Implementation of the backend
# 
# The goal of this part is the implementation of a unique system that has four different functionalities. The program takes in input always a number i in [1,4]: given the input, the program has to run Functionality i, applied to the graph you create from the downloaded data.

# ## Functionality 1 - Find the Neighbours!
# 
# It takes in input:
# 
# * __a node v__
# *  One of the following distances function: __t(x,y), d(x,y) or network distance (i.e. consider all edges to have weight equal to 1).__
# * __a distance threshold d__
# 
#  Implement an algorithm (using proper data structures) that returns the set of nodes at distance <= d from v, corresponding to v’s neighborhood.

# In[1]:


# import libraries and functions
from dataset_loader import DatasetLoader
from utils import make_adj_list
import networkx as nx
import copy


# In[2]:


# create Dataframe from .co and .gr files
coord = DatasetLoader('coordinates','C:\\Users\\giuseppe\\Desktop\\HW5\\dataset\\').get_dataset()
dist = DatasetLoader('distance','C:\\Users\\giuseppe\\Desktop\\HW5\\dataset\\').get_dataset()
timedist = DatasetLoader('time-distance','C:\\Users\\giuseppe\\Desktop\\HW5\\dataset\\').get_dataset()

# create dicts with all neighbors for each node
neighbors = make_adj_list('distance')
t_neighbors = make_adj_list('time-distance')


# In[39]:


# create Functionality 1

def fun1(v, dis, d):
    
    if v == 0 or v > 1890815:
        print('Error! Absent node: insert a valid id node!')
        return -1
    
    if dis not in ['distance','time-distance']:
        print("Distance metric not valid, please choose 'distance' or 'time-distance'. ")
        return -1
    
    if type(d) != int:
        print('Error! Invalid Threshold: please insert a number')
        return -1
    
    if dis == 'distance' and d > 215354 or dis == 'time-distance' and d > 538385:
        print('Error: Threshold inserted too large!')
        return -1
    
    if dis == 'distance':
        nodes = copy.deepcopy(neighbors)
    else:
        nodes = copy.deepcopy(t_neighbors)
    
    
    for key,value in nodes[v].items():
        if value > d:
            nodes[v] = copy.deepcopy(nodes[v])
            nodes[v].pop(key, None)
            
    
    return print('Neighbors Nodes: ', list(nodes[v]))
    
        
    
    


# In[40]:


fun1(2948938598, 'distance', 45)


# In[42]:


fun1(35, 'timistance', 100)


# In[43]:


fun1(343, 'time-distance', 'mille')


# In[44]:


fun1(498, 'distance', 2349853)


# In[45]:


fun1(35436, 'distance', 1000)


# In[36]:


fun1(35436, 'time-distance', 2000)


# # <font color= red> Implementation of the frontend
# In this section, you build the visualizations for users’ queries results.
# 
# 

# ## Visualization 1 - Visualize the Neighbours!
# 
# Once the user runs Functionality 1, we want the system to show in output a complete map that contains: the input node, the output nodes and all the streets that connect these points. Choose different colors in order to highlight which is the input node, and which are the output nodes. Furthermore, choose different colors for edges, according to the distance function used.

# In[69]:


def vis1():

    print('Write the input node: ')
    x = input()
    print('Choose "distance" or "time-distance": ') 
    y = input()
    print('Write the threshold: ')
    z = input()
    
    fun1(int(x),y,int(z))
    
    
    
    


# In[70]:


vis1()


# In[ ]:




