'''
Adaptado de:
@author: Edielson - https://github.com/edielsonpf
'''

from SearchAlgorithms.greedy_search import greedy_search
import networkx as nx


try:
    import matplotlib.pyplot as plt
except:
    raise


def printPath(path, start):
    string = (start)
    for city in path:
        if city != start:
            string = (string+' -> '+city)
    print(string)


def plotGraph(G, option, position=None):
    """Plot a graph G with specific position.

    Parameters
    ----------
    G : NetworkX graph
    option : if 1, edges with weight greater then 0 are enlarged. The opposite happens for option equal to 0.
    position : nodes position 

    Returns
    -------
    position: nodes position generated during plot (or same positions if supplied).

    """
    if option == 1:
        elarge = [(u, v)
                  for (u, v, d) in G.edges(data=True) if d['weight'] > 0]
        esmall = [(u, v)
                  for (u, v, d) in G.edges(data=True) if d['weight'] <= 0]
    else:
        elarge = [(u, v)
                  for (u, v, d) in G.edges(data=True) if d['weight'] <= 0]
        esmall = [(u, v)
                  for (u, v, d) in G.edges(data=True) if d['weight'] > 0]

    if position == None:
        position = nx.spring_layout(G)  # positions for all nodes

    # nodes
    nx.draw_networkx_nodes(G, position, node_size=500)

    # edges
    nx.draw_networkx_edges(G, position, edgelist=elarge, width=2)
    nx.draw_networkx_edges(G, position, edgelist=esmall,
                           width=2, alpha=0.5, edge_color='b', style='dashed')

    # labels
    nx.draw_networkx_labels(G, position, font_size=20,
                            font_family='sans-serif')

    plt.axis('off')
    # plt.savefig("weighted_graph.png") # save as png
    plt.show()  # display

    return position


class FindPath(object):
    '''
    classdocs
    '''

    def __init__(self, graph):
        '''
        Constructor
        '''
        self.problem = graph

    def ObjectiveTest(self, current, target):
        """Return ``True`` if ``current`` state corresponds to the ``target`` state 
        """
        solution = False
        if current == target:
            solution = True
        return solution

    def ExpandSolution(self, current):
        """Returns all possible states from ``current`` 
        """
        return self.problem.neighbors(current)

    def Heuristic(self, target, current):
        """Returns heuristic associated to ``current`` 
        """
        custo_linha_reta = {
            ('S. R. Sapucaí', 'Campinas'): 165,
            ('Pouso Alegre', 'Campinas'): 137,
            ('Cambuí', 'Campinas'): 108,
            ('Congonhal', 'Campinas'): 135,
            ('Camanducaia', 'Campinas'): 97,
            ('Borda da Mata', 'Campinas'): 117,
            ('Bragança Paulista', 'Campinas'): 54,
            ('Ipuiúna', 'Campinas'): 139,
            ('Jacutinga', 'Campinas'): 84,
            ('Andradas', 'Campinas'): 106,
            ('Atibaia', 'Campinas'): 57,
            ('Itapira', 'Campinas'): 58,
            ('Esp. Santo Pinhal', 'Campinas'): 86,
            ('Mogi-Guaçu', 'Campinas'): 62,
            ('Mogi Mirim', 'Campinas'): 54,
            ('Campinas', 'Campinas'): 0,
        }

        Heuristic = custo_linha_reta.get((current, target))
        print(Heuristic)
        return Heuristic


if __name__ == '__main__':

    nodes = ['S. R. Sapucaí', 'Pouso Alegre', 'Cambuí', 'Congonhal', 'Camanducaia', 'Borda da Mata',
             'Ipuiúna', 'Bragança Paulista', 'Jacutinga', 'Andradas', 'Atibaia', 'Itapira',
             'Esp. Santo Pinhal', 'Mogi-Guaçu', 'Mogi Mirim', 'Campinas']

    edges = [
        ('S. R. Sapucaí', 'Pouso Alegre'),
        ('Pouso Alegre', 'Cambuí'),
        ('Cambuí', 'Camanducaia'),
        ('Camanducaia', 'Bragança Paulista'),
        ('Bragança Paulista', 'Atibaia'),
        ('Bragança Paulista', 'Itapira'),
        ('Atibaia', 'Campinas'),
        ('Pouso Alegre', 'Borda da Mata'),
        ('Borda da Mata', 'Jacutinga'),
        ('Jacutinga', 'Itapira'),
        ('Itapira', 'Campinas'),
        ('Pouso Alegre', 'Congonhal'),
        ('Congonhal', 'Ipuiúna'),
        ('Ipuiúna', 'Andradas'),
        ('Andradas', 'Esp. Santo Pinhal'),
        ('Esp. Santo Pinhal', 'Mogi-Guaçu'),
        ('Mogi-Guaçu', 'Mogi Mirim'),
        ('Mogi Mirim', 'Campinas'),
    ]

    cost = {
        ('S. R. Sapucaí', 'Pouso Alegre'): 28.5,
        ('Pouso Alegre', 'Cambuí'): 49.1,
        ('Cambuí', 'Camanducaia'): 24.7,
        ('Camanducaia', 'Bragança Paulista'): 60.4,
        ('Bragança Paulista', 'Atibaia'): 25.2,
        ('Bragança Paulista', 'Itapira'): 82.4,
        ('Atibaia', 'Campinas'): 65.6,
        ('Itapira', 'Campinas'): 70.7,
        ('Pouso Alegre', 'Borda da Mata'): 28.8,
        ('Borda da Mata', 'Jacutinga'): 57.6,
        ('Jacutinga', 'Itapira'): 33.2,
        ('Pouso Alegre', 'Congonhal'): 24.3,
        ('Congonhal', 'Ipuiúna'): 24.6,
        ('Ipuiúna', 'Andradas'): 67.6,
        ('Andradas', 'Esp. Santo Pinhal'): 28.4,
        ('Esp. Santo Pinhal', 'Mogi-Guaçu'): 35.7,
        ('Mogi-Guaçu', 'Mogi Mirim'): 25.0,
        ('Mogi Mirim', 'Campinas'): 60.1,
    }

    G = nx.DiGraph()

    G.add_nodes_from(nodes)

    # Adding the respective cost for each edge in the graph
    for u, v in edges:
        G.add_edge(u, v, weight=cost[u, v])
    positions = plotGraph(G, 1, None)

    # Creating an problem object based on FindPath class
    Problema = FindPath(G)

    # Creating an object for breadth first search algorithm for ``FindPath`` problem
    SearchObj = greedy_search(Problema)

    start = 'S. R. Sapucaí'
    target = 'Campinas'
    print('\nSearching %s starting from %s...' % (target, start))
    solution, path, path_edges = SearchObj.search(start, target)
    print('Done!\n')
    if solution:
        print('Path found!')
        printPath(path, start)
        for u, v in edges:
            if (u, v) not in path_edges:
                G.remove_edge(u, v)
        plotGraph(G, 1, positions)
    else:
        print('Path not found!')
