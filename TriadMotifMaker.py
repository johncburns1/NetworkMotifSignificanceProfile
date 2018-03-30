
# coding: utf-8

# In[1]:


import networkx as nx
import os as os
import random
import numpy as np
import SignificanceProfileHelper as sp

import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')

import warnings
warnings.filterwarnings("ignore", category=UserWarning)


# In[21]:


collegeMsg = nx.read_edgelist('data/collegeMessage/CollegeMsg.txt', 
                                    create_using=nx.DiGraph(), 
                                    nodetype=str, data=[('unix_timestamp', int)])


# In[22]:


bitcoinAlpha = nx.read_edgelist('data/bitcoinAlpha/bitcoinAlpha.txt', 
                                    create_using=nx.DiGraph(), 
                                    nodetype=str, data=[('rating', int), ('time', int)])


# In[23]:


email_eu_core = nx.read_edgelist('data/email_EU/email_Eu_core.txt', 
                                    create_using=nx.DiGraph(), 
                                    nodetype=str)


# In[24]:


email_eu_core_dep_labels = nx.read_edgelist('data/email_EU/email_Eu_core_department_labels.txt', 
                                    create_using=nx.DiGraph(), 
                                    nodetype=str)


# In[25]:


gnutella = nx.read_edgelist('data/Gnutella/p2p_Gnutella.txt', 
                                    create_using=nx.DiGraph(), 
                                    nodetype=str)


# In[26]:


bitcoinOTC = nx.read_edgelist('data/bitcoinOTC/bitcoinotc.txt', 
                                    create_using=nx.DiGraph(), 
                                    nodetype=str, data=[('rating', int), ('time', int)])


# In[21]:


ring = sp.make_ring(3000)
eR = nx.erdos_renyi_graph(150, .05, directed=True)


# In[22]:


#sig_ring = sp.getFullProfile(ring, 10)
#sig_profile = sp.getFullProfile(eR, 10)
#sig_profile_emailEuCoreDepLab = sp.getFullProfile(email_eu_core_dep_labels, 10)


# In[8]:


sig_profile_collegeMsg = sp.getFullProfile(collegeMsg, 10)


# In[9]:


sig_profile_bitcoinAlpha = sp.getFullProfile(bitcoinAlpha, 10)


# In[10]:


sig_profile_emailEuCore = sp.getFullProfile(email_eu_core, 10)


# In[11]:


sig_profile_gnutella_p2p = sp.getFullProfile(gnutella, 10)


# In[12]:


sig_profile_bitcoinOTC = sp.getFullProfile(bitcoinOTC, 10)


# In[14]:


def buildPlot():
    # Lines on top of scatter
    xAxis = [1,2,3,4,5,6,7,8,9,10,11,12,13]

    plt.figure()
    fig, ax = plt.subplots(1,1,figsize=(14, 4))
    ax.grid(True, which='minor')
    ax.axhline(y=0, color='k')
    plt.xticks(np.arange(min(xAxis), max(xAxis)+1, 1.0))

    
    #plt.plot(xAxis, sig_profile,'r', lw=1, label='erdos-renyi-model', zorder=1)
    #plt.plot(xAxis, sig_ring,'b', lw=1, label='randomized circular graph', zorder=1)
    #plt.plot(xAxis, sig_profile_emailEuCoreDepLab, 'y', lw=1, label='email EU core department labels', zorder=1)
    plt.plot(xAxis, sig_profile_bitcoinAlpha, 'm', lw=1, label='bitcoin alpha', zorder=1)
    plt.plot(xAxis, sig_profile_bitcoinOTC, 'b', lw=1, label='bitcoin otc', zorder=1)
    plt.plot(xAxis, sig_profile_collegeMsg, 'g', lw=1, label='college message', zorder=1)
    plt.plot(xAxis, sig_profile_emailEuCore, 'c', lw=1, label='email EU core', zorder=1)
    plt.plot(xAxis, sig_profile_gnutella_p2p, 'r', lw=1, label='gnutella p2p', zorder=1)

    #plt.scatter(xAxis, sig_ring, s=100, zorder=2, c='b')
    #plt.scatter(xAxis, sig_profile, s=100, zorder=2, c='r')
    #plt.scatter(xAxis, sig_profile_emailEuCoreDepLab, s=100, zorder=2, c='y')
    plt.scatter(xAxis, sig_profile_collegeMsg, s=100, zorder=2, c='g')
    plt.scatter(xAxis, sig_profile_bitcoinAlpha, s=100, zorder=2, c='m')
    plt.scatter(xAxis, sig_profile_bitcoinOTC, s=100, zorder=2, c='b')
    plt.scatter(xAxis, sig_profile_emailEuCore, s=100, zorder=2, c='c')
    plt.scatter(xAxis, sig_profile_gnutella_p2p, s=100, zorder=2, c='r')
    

    plt.title('Significance profile')
    plt.xlabel("motif", fontsize='large')
    plt.ylabel("z-score", fontsize='large')

    l = plt.legend()
    l.set_zorder(20)


# In[15]:


buildPlot()

