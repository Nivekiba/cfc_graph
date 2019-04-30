import json

with open('graph.json') as f:
	graph = json.load(f)

class Graph():
    def __init__(self, S):
        self.S = S
        self.plus = {}
        self.moins = {}
        self.CFC = {}
        for e in S.keys(): self.CFC[e] = False
    def suiv(self, som):
        return self.S[som]
    def pred(self, som):
        t = []
        for e in self.S.keys():
            if som in self.S[e]:
                t.append(e)
        return t
    def sommets(self):
        return list(self.S.keys())
    def init_mark(self):
        for e in self.S.keys():
            self.plus[e] = self.moins[e] = False

def dfs_suiv(graph, s):
    """
        Parcours DFS des suivants a partir du 
        sommet s
    """
    if graph.plus[s]: return
    graph.plus[s] = True
    for e in graph.suiv(s):
        dfs_suiv(graph, e)
        
def dfs_pred(graph, s):
    """
        Parcours DFS des precedents a partir du 
        sommet s
    """
    if graph.moins[s]: return
    graph.moins[s] = True
    for e in graph.pred(s):
        dfs_pred(graph, e)

def CFC(g):
    composantes = []
    for s in g.sommets(): # pour chaque sommet
        if g.CFC[s]:
            continue # S'il appartient deja a un CFC on le saute
        g.init_mark()
        dfs_suiv(g,s) # propagation des plus
        dfs_pred(g,s) # propagation des moins
        res = []
        for e in g.sommets():
            if g.plus[e] == g.moins[e] == True:
                res.append(e)
                g.CFC[e] = True
        composantes.append(res)
    g.init_mark()
    return composantes
	
# Creation du graphe sous forme de liste d'adjacence

g = Graph(graph)

cfcs = CFC(g)
print(cfcs)