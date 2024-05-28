import sys
import random
import graph as g
import time
from itertools import permutations

def TFS_probabilistic_RANDOM_PATH(graf):
    vertex = graf.vertices[:]
    path = []
    while len(vertex) > 0:
        random_element = random.choice(vertex)
        path.append(random_element)
        vertex.remove(random_element)
    return path

def Dijkstra(graf, start):
    inf = sys.maxsize
    Q = []
    dist = [None] * 101
    prev = [None] * 101
    for v in graf.vertices:
        dist[v.id] = inf
        prev[v.id] = 0 #ALBO NONE
        Q.append(v)
    dist[start.id] = 0
    while len(Q) > 0:
        u = min(Q, key=lambda vertex: dist[vertex.id])
        Q.remove(u)
        for v in Q:
            alt = dist[u.id] + g.cost(u,v)
            if (alt < dist[v.id]):
                dist[v.id] = alt
                prev[v.id] = u
    dist = dist[1:]
    prev = prev[1:]
    return prev

def path_length(path):
    v = path[0]
    len = 0
    for a in range(1, 100):
        len = len + g.cost(v, path[a])
        v = path[a]
    len = len + g.cost(v, path[0])
    return len


def TFS_greedy(graf, start):
    vertex = graf.vertices[:]
    path = [start]
    vertex.remove(start)
    while(len(vertex)>0):
        min_cost = sys.maxsize
        min_vertex = None
        for e in vertex:
            cost = g.cost(path[-1], e)
            if cost < min_cost:
                min_cost = cost
                min_vertex = e
        path.append(min_vertex)
        vertex.remove(min_vertex)
    return(path)

def TFS_file_order(graf):
    return(graf.vertices)


def main():
    input = open('TSP.txt', 'r')

    graf = g.Graph()
    for line in input:
        line = line.strip()
        line = line.split()
        graf.add_vertex(int(line[0]), float(line[1]), float(line[2]))

    for v in graf.vertices:
        for u in graf.vertices:
            if v != u:
                graf.add_edge(v, u)
    t = time.time()
    print("TFS zachłanny: ", path_length(TFS_greedy(graf, graf.vertices[0])))
    print(time.time() - t)

    t = time.time()
    print("TFS według kolejności w pliku : ", path_length(TFS_file_order(graf)))
    print(time.time() - t)

    #probabilistyczny
    minLen = sys.maxsize
    N = 10000
    t = time.time()
    for i in range(N):
        minLen = min(minLen, path_length(TFS_probabilistic_RANDOM_PATH(graf)))
    print("TFS probabilistyczny", minLen)
    print(time.time() - t)

    minLen = sys.maxsize
    t = time.time()
    for i in range(100):
        minLen = min(minLen, path_length(TFS_greedy(graf, graf.vertices[i])))
    print("Algorytm zachłanny różne punkty startowe", minLen)
    print(time.time() - t)




if __name__ == "__main__":
    main()
