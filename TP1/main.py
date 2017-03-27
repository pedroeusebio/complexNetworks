from __future__ import division
from graph_tool.all import *
import math
import numpy as np
import matplotlib.pyplot as plt

infDistance = 2147483647

def readGraph(path, separator=" ", endline="\n", direct=True):
    print("start reading !")
    g = Graph(directed=direct)
    file = open(path, "r")
    vertexArray = {}
    for l in file:
        vIdO = l.split(separator)[0]
        vIdD = l.split(separator)[1].split(endline)[0]
        vO,vD = None, None
        if(vIdO in vertexArray):
            vO = vertexArray[vIdO]
        else:
            vO = g.add_vertex()
            vertexArray[vIdO] = vO

        if(vIdD in vertexArray):
            vD = vertexArray[vIdD]
        else:
            vD = g.add_vertex()
            vertexArray[vIdD] = vD

        if(direct) :
            g.add_edge(vO,vD)
        else:
            vONeighbours = vO.all_neighbours()
            added = False
            for neighbour in vONeighbours:
                if(neighbour == vD):
                    added = True
                    break
            if(added == False):
                g.add_edge(vO,vD)

    print("ending reading");
    return g

def cdfReport(data, filename="export"):
    sorted = np.sort(data)
    yvals = np.arange(len(sorted))/float(len(sorted))
    plt.plot(sorted, yvals)
    plt.savefig(filename)


def degreesMetric(g, direct=True, graphName="default"):
    degreeData = {}
    if(direct):
        degreesIn = g.get_in_degrees(g.get_vertices())
        degreesOut = g.get_out_degrees(g.get_vertices())
        degreeData = {
            "in" : {
                "max": degreesIn.max(),
                "min": degreesIn.min(),
                "mean": degreesIn.mean(),
                "std": degreesIn.std(),
            },
            "out": {
                "max": degreesOut.max(),
                "min": degreesOut.min(),
                "mean": degreesOut.mean(),
                "std": degreesOut.std(),
            }
        }
        cdfReport(degreeIn, filename="_".join(str(x) for x in [graphName,"degreeIn"]))
        cdfReport(degreeOut, filename="_".join(str(x) for x in [graphName,"degreeOut"]))
    else:
        degrees = g.get_out_degrees(g.get_vertices())
        degreeData = {
            "max": degrees.max(),
            "min": degrees.min(),
            "mean": degrees.mean(),
            "std": degrees.std(),
        }
        cdfReport(degrees, filename="_".join(str(x) for x in [graphName,"degree"]))
    return degreeData

def distanceMetric(g, direct=True, graphName="default"):
    distanceData = {}
    distances = shortest_distance(g, directed=direct)
    maxDist = []
    minDist = []
    distArray = []
    totalDistance = 0
    for v in g.vertices():
        dist = distances[v].a
        selfDist = np.where(dist == 0)
        infiniteDist = np.where(dist == infDistance)
        newDist = np.delete(dist, np.append(selfDist, infiniteDist))
        if(len(newDist) > 0):
            maxDist.append(newDist.max())
            minDist.append(newDist.min())
            distArray.append(np.sum(newDist))
            totalDistance += len(newDist)

    return {"max": np.max(maxDist), "min": min(minDist), "mean": np.sum(distArray)/ totalDistance}

def clusteringMetric(g, direct=True, graphName="default"):
    filename = "_".join(str(x) for x in [graphName,"cluster"])
    localCluster = local_clustering(g, undirected= not direct)
    localResult = vertex_average(g, localCluster)
    maxClust = 0;
    minClust = infDistance;
    for v in g.vertices():
        if(localCluster[v] >= maxClust):
            maxClust = localCluster[v]
        if(localCluster[v] <= minClust):
            minClust = localCluster[v]
    cdfReport(localCluster.a, filename)

    return {
        "global": global_clustering(g),
        "min": minClust,
        "max": maxClust,
        "std": localResult[1],
        "mean": localResult[0]
    }

def betweenessMetric(g, graphName="default"):
    filename = "_".join(str(x) for x in [graphName,"betweeness"])
    result = betweenness(g)
    vertex = result[0].a
    edge = result[1].a
    cdfReport(vertex, filename + "_vertex")
    cdfReport(edge, filename + "_edge")

    return {
        "vertex": {
            "min": vertex.min(),
            "max": vertex.max(),
            "mean": vertex.mean(),
            "std": vertex.std()
        },
        "edges": {
            "min": edge.min(),
            "max": edge.max(),
            "mean": edge.mean(),
            "std": edge.std()
        }
    }

def componentsMetric(g, direct=True, graphName="default"):
    filename = "_".join(str(x) for x in [graphName,"components"])
    comp, hist = label_components(g, directed=direct, attractors=True)
    nComponents = comp.a.max()
    largestComponent = hist.max()
    indexLargest = np.where(hist == largestComponent)
    idLargest = comp.a[indexLargest]
    cdfReport(hist, filename);
    return {
        "components": nComponents + 1,
        "largest" : {
            "size": largestComponent,
            "id": indexLargest
        },
        "mean": hist.mean(),
        "std": hist.std()
    }

def closenessMetric(g, graphName="default"):
    filename = "_".join(str(x) for x in [graphName,"closeness"])
    vertexCloseness = closeness(g)
    newCloseness = []
    for vertex in vertexCloseness.a:
        if(math.isnan(vertex) == False):
            newCloseness.append(vertex)
    cdfReport(newCloseness, filename);

    return {
        "max": np.max(newCloseness),
        "min": np.min(newCloseness),
        "mean": np.mean(newCloseness),
        "std": np.std(newCloseness)
    }


graphs = [
    {
        "path": './networks/facebook_combined.txt',
        "direct": False,
        "graphName": "facebook" ,
        "endline": '\n'
    },
    {
        "path": './networks/email-Enron.txt',
        "direct": False,
        "graphName": "email" ,
        "endline": '\r'
    },
    {
        "path": './networks/ca-HepPh.txt',
        "direct": False,
        "graphName": "ph" ,
        "endline": '\r'
    }
]

for graph in graphs:
    g = readGraph(graph["path"], " ", endline=graph["endline"], direct=graph["direct"])
    print(graph['graphName'])
    print(degreesMetric(g, direct=graph["direct"], graphName=graph["graphName"]))
    print(distanceMetric(g, direct=graph["direct"], graphName=graph["graphName"]))
    print(clusteringMetric(g, direct=graph["direct"], graphName=graph["graphName"]))
    print(betweenessMetric(g, graphName=graph["graphName"]))
    print(componentsMetric(g, direct=graph["direct"], graphName=graph["graphName"]))
    print(closenessMetric(g, graphName=graph["graphName"]))
    graph_draw(g, output_size=(2048, 1280), output=graph["graphName"] + ".png")
