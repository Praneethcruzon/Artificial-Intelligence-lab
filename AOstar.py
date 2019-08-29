# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import queue
class Node:
    def __init__ (self, name, h, g, solved, goal, isAnd, parent):
        self.name = name
        self.h = h
        self.solved = solved
        self.isGoal = goal
        self.g = g
        self.isAnd = isAnd
        self.parent = parent
        
class Graph:
    def __init__(self, children):
        self.children = children
        
def minCostEdge(children):
    mini = 99999999
    for child in children:
        cost = child.h + child.g
        if(cost < mini):
            mini = cost
            node = child
    return mini, node

def calCost(graph, node):
    children = graph.children[node]
    cost = 0
    if(node.isAnd == True):
        for child in children:
            cost += (child.g + child.h)
            minEdge = node
    else:
        cost, minEdge = minCostEdge(children)
    return cost, minEdge

def updateCost(graph, node):
    while(node != None):
        cost,  minEdge = calCost(graph, node)
        node.cost = cost
        node = node.parent
            

def AndOr(graph, root):
    q = queue.Queue(maxsize = 20)
    q.put(root)
    while(q):
        node = q.get()
        cost, node = calCost(graph, node)
        node.h = cost
        updateCost(graph, node.parent)
        if(node.isAnd == True):
            for child in graph.children[node]:
                q.put(child)
        else:
            q.put(node)
    return root.h
def main():
    a = Node("A", 7, 0, False, False, True, None)
    b = Node("B", 4, 2, False, False, False, a)
    c = Node("C", 3, 1, False, False, False, a)
    d = Node("D", 2, 2, False, False, True, b)
    e = Node("E", 5, 1, False, False, True, b)
    f = Node("F", 0, 9, False, True, False, c)
    g = Node("G", 0, 7, False, True, False, c)
    h = Node("H", 0, 3, False, False, False, d)
    i = Node("I", 0, 10, False, True, False, d)
    j = Node("J", 0, 3, False, True, False, e)
    k = Node("K", 0, 4, False, True, False, e)
    graph = Graph(
            {a:[[b,c]],
             b:[[d],[e]],
             c:[[f],[g]],
             d:[[h,i]],
             e:[[j,k]]}
              )
    cost = AndOr(graph, a)
    print(cost)
    
main()

