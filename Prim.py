"""Prim.py
Author: BO WANG
Date: 09/18/2014
Prim's algorithm for MST using Priority-queue structure to reduce complexity"""

from pqdict import PQDict

def prim(G):
    """ Return MST of the given undirected graph"""
    sumWeight = 0

    heap = PQDict()
    for u in G:
        heap[u] = float("inf")
    flag = [False] * len(G)
    heap[0] = 0
    #parents is the MST
    # parents = {}
    # parents[0] = 0
    while len(heap) != 0:
        [u, value] = heap.popitem()
        flag[u] = True
        sumWeight += value
        for v in G[u]:
            if flag[v] is False:
                # parents[v] = u
                heap[v] = min(heap[v], G[u][v])
    return sumWeight