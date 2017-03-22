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


g = readGraph('./networks/facebook_combined.txt', " ", False)
# graph_draw(g, output_size=(2048, 1280), output="facebookT.png")

