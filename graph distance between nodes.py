import graph
import Queue
a=graph.Graph(6)
a.add_edge(0,1)
a.add_edge(0,2)
a.add_edge(1,3)
a.add_edge(1,4)
a.add_edge(2,3)
a.add_edge(2,5)

def distance_from_source(graph,source):
    visited=[]
    q=Queue.Queue(graph.nodes)
    distances=[-1 for i in range(graph.nodes)]
    #distance from the source to source is always 0
    distances[source]=0
    visited.append(source)
    q.enqueue(source)
    while not q.is_empty():
        taken_out=q.dequeue()
        for i in graph.ad_list[taken_out]:
            if i not in visited:
                distances[i]=distances[taken_out]+1
                visited.append(i)
                q.enqueue(i)
    return distances

print(distance_from_source(a,3))
                                                        