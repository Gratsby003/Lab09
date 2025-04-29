import networkx as nx
from database.DAO import DAO


class Model:
    def __init__(self):
        pass

    def airport_analysis(self,valore):
        lista=DAO.query_airport(valore)
        print(lista)
        grafo = nx.Graph()
        for i in lista:
            grafo.add_edge(i[0],i[1],weight=float(i[2]))
        return grafo


