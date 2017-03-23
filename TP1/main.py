from graph_tool.all import *

def readGraph(path, separator=" ", direct=True):
    print("start reading !")
    g = Graph(directed=direct)
    file = open(path, "r")
    vertexArray = {}
    for l in file:
        vIdO = l.split(separator)[0]
        vIdD = l.split(separator)[1].split("\n")[0]

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

def degreesMetric(g, direct=True):
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
    else:
        degrees = g.get_out_degrees(g.get_vertices())
        degreeData = {
            "max": degrees.max(),
            "min": degrees.min(),
            "mean": degrees.mean(),
            "std": degrees.std(),
        }
    return degreeData

g = readGraph('./networks/facebook_combined.txt', " ", False)
def distanceMetric(g, direct=True):
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

def clusteringMetric(g, direct=True):
    localCluster = local_clustering(g, undirected= not direct)
    localResult = vertex_average(g, localCluster)
    maxClust = 0;
    minClust = infDistance;
    for v in g.vertices():
        if(localCluster[v] >= maxClust):
            maxClust = localCluster[v]
        if(localCluster[v] <= minClust):
            minClust = localCluster[v]

    return {
        "global": global_clustering(g),
        "min": minClust,
        "max": maxClust,
        "std": localResult[1],
        "mean": localResult[0]
    }

# data = degreesMetric(g, False)
# graph_draw(g, output_size=(2048, 1280), output="facebookT.png")

