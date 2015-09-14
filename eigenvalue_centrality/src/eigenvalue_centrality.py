'''
Created on Jun 28, 2011

@author: sony
'''
def eigenvector_centrality(G,n,v=False):
    from numpy.linalg import eig
    from networkx.linalg.spectrum import adj_matrix
    no_of_nodes =n
    eigenvector_centrality = {}
    G_mat = adj_matrix(G)
    G_ev = eig(G_mat)  # NumPy implementation of generalized eigenvector
    G_evals = G_ev[0]     # Eigenvalues array
    G_evec_mat = G_ev[1]  # Full N X N Eigenvector matrix
    G_evals = G_evals.tolist()
    # Error handling for complex numbers
    try:
        dominant_eigvector = G_evals.index(max(G_evals))  # Index of dominant Eigenvector
        for i in range (0,G.number_of_nodes):
            eigenvector_centrality[i] = abs(G_evec_mat[i,dominant_eigvector])
    except TypeError:
        
       # For some arrays we must handle complex numbers by extracting 'real' portion
        complex_temp = list()
        for d in range(0,len(G_evals)):
                        complex_temp.append(G_evals[d].real)
                        dominant_eigvector = complex_temp.index(max(complex_temp))  # Index of dominant Eigenvector
        for i in range (0,no_of_nodes):
            eigenvector_centrality[i] = abs(G_evec_mat[i,dominant_eigvector].real)
        if not v:
            return eigenvector_centrality
        else:
            return eigenvector_centrality[v]
    
    
   
if __name__ =='__main__':
    import networkx as nx
    pos = {}
    G = nx.Graph()
    n=input("enter no of vertices in the graph")
    print ("reading the given graph data")
    G.add_edges_from([(0,1),(0,3),(0,4),(1,4),(1,5),(2,5),(3,4),(4,5),(4,2),(5,3)])
    import matplotlib.pyplot as plt
    weights = {(0,1):4,(0,3):5,(0,4):1,(1,4):3,(1,5):1,(2,5):1,(3,4):1,(4,5):1,(4,2):2,(5,3):2}
##    nx.drawing.nx_pylab.draw_networkx_edges(G,nx.spring_layout(G))
##    nx.drawing.nx_pylab.draw_networkx_edge_labels(G,nx.spring_layout(G),edge_labels=weights)
##    plt.show()
    ec=eigenvector_centrality(G,n)
    for i in range(0,n):
        print "eigenvector centrality of %d is found to be %f " % (i,ec[i])
    
