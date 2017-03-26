from graph_tool.all import *
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
    meanDist = []
    stdDist = []
    for v in g.vertices():
        dist = distances[v].a
        selfDist = np.where(dist == 0)
        newDist = np.delete(dist, selfDist)
        maxDist.append(newDist.max())
        minDist.append(newDist.min())
        meanDist.append(newDist.mean())
        stdDist.append(newDist.std())

    return {"max": np.max(maxDist), "min": min(minDist), "mean": np.mean(meanDist), "std": np.std(stdDist)}

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
    cdfReport(vertexCloseness.a, filename);
    return {
        "max": vertexCloseness.a.max(),
        "min": vertexCloseness.a.min(),
        "mean": vertexCloseness.a.mean(),
        "std": vertexCloseness.a.std()
    }

g = readGraph('./networks/wiki-Vote.txt', " ", endline="\r",  direct=False)
# data = degreesMetric(g, False)
# print(clusteringMetric(g))
# print(betweenessMetric(g))
# print(componentsMetric(g, False))
print(closenessMetric(g))
# graph_draw(g, output_size=(2048, 1280), output="facebookT.png")
