
# coding: utf-8

# In[1]:


import networkx as nx
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
import random
import numpy as np
import scipy.stats as st


# In[17]:


def getFullProfile(graph, N):
    
    sigProfile = []
    zScores = getAllZScores(graph, N)
    alt = [x for x in zScores if x != 0]
    zSum = float(np.linalg.norm(alt, ord=2))
    n = len(zScores)
    
    for i in range(n):
        sigProfile.append(float(zScores[i]/zSum)) 
    
    return sigProfile


# In[3]:


def getAllZScores(graph, N):
    real_triads = getTriads(graph)
    random_sample_triads = sampleMultipleRandGraphs(graph, N)
    zScores = []
    n = len(real_triads)
    if(len(real_triads) == len(random_sample_triads)):
        for i in range(n):
            nReal = real_triads[i][1]
            sample = random_sample_triads[i]
            
            mRand = float(np.mean(sample))
            std = float(np.std(sample))
            
            if std != 0:
                zScore = float((nReal-mRand)/(std))
                zScores.append(zScore)
            else: 
                zScores.append(float(nReal-mRand))          
    return zScores


# In[4]:


def getZScore(nReal, sample):
    mRand = getMean(sample)
    stdRand = getStandardDeviation(sample)
    return (nReal - mRand)/(stdRand)


# In[14]:


def getTriads(graph):
    triads_16 = nx.triadic_census(graph)
    triads_13 = [(x,y) for x,y in triads_16.items() if(x != '003' and x != '012' and x != '102')]
    return triads_13


# In[7]:


def generateDirectedConfigurationModel(graph):
    in_degrees = graph.in_degree()
    out_degrees = graph.out_degree()
    in_degrees_list = [x[1] for x in list(in_degrees)]
    out_degrees_list = [x[1] for x in list(out_degrees)]
    return nx.directed_configuration_model(in_degrees_list, out_degrees_list, create_using=nx.DiGraph(), seed=random.seed())


# In[8]:


def sampleRandomGraph(graph):
    triads = []
    g = generateDirectedConfigurationModel(graph)
    return getTriads(g)


# In[9]:


def sampleMultipleRandGraphs(graph, N):
    triad_matrix = [[0 for x in range(N)] for y in range(13)]
    for i in range(N):
        triad_list = sampleRandomGraph(graph)
        for j in range(13):
            triad_matrix[j][i] = triad_list[j][1]
            
    return triad_matrix


# In[12]:


def getTriadGraphs():
    triad_motifs = []

    for i in range(13):
    
        if(i == 0):
            triad_motifs.append(nx.triad_graph("021D"))
        if(i == 1):
            triad_motifs.append(nx.triad_graph("021U"))
        if(i == 2):
            triad_motifs.append(nx.triad_graph("021C"))
        if(i == 3):
            triad_motifs.append(nx.triad_graph("111D"))
        if(i == 4):
            triad_motifs.append(nx.triad_graph("111U"))
        if(i == 5):
            triad_motifs.append(nx.triad_graph("030T"))
        if(i == 6):
            triad_motifs.append(nx.triad_graph("030C"))
        if(i == 7):
            triad_motifs.append(nx.triad_graph("201"))
        if(i == 8):
            triad_motifs.append(nx.triad_graph("120D"))
        if(i == 9):
            triad_motifs.append(nx.triad_graph("120U"))
        if(i == 10):
            triad_motifs.append(nx.triad_graph("120C"))
        if(i == 11):
            triad_motifs.append(nx.triad_graph("210"))
        if(i == 12):
            triad_motifs.append(nx.triad_graph("300"))
            
    return triad_motifs


# In[13]:


def make_ring(N):
    graph = nx.DiGraph()
    for i in range(N):
        graph.add_node(i)
    
    for i in range(N):
        k = random.choice(list(graph.nodes()))
        j = random.choice(list(graph.nodes()))
        while((k, j) in list(graph.edges) or k == j):
            j = random.choice(list(graph.nodes()))
            k = random.choice(list(graph.nodes()))
        graph.add_edge(k, j)
    
    return graph

