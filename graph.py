import Queue
class Graph():
    def __init__(self,nodes):
        self.nodes=nodes
        #item then the for loop(for however many times you want to add item)
        self.ad_list=[[]for i in range(nodes)]
        print(self.ad_list)

    def add_edge(self,node1,node2):
        self.ad_list[node1].append(node2)
        self.ad_list[node2].append(node1)
        print(self.ad_list)

    def bfs_traversAL(self,start):
        visited=[]
        queue=Queue.Queue(self.nodes)
        queue.enqueue(start)
        visited.append(start)
        while not queue.is_empty():
            node=queue.dequeue()
            for i in self.ad_list[node]:
                if i not in visited:
                    queue.enqueue(i)
                    visited.append(i)
        return visited


a=Graph(4)
a.add_edge(0,1)
a.add_edge(0,3)
a.add_edge(1,3)
a.add_edge(2,3)
print(a.bfs_traversAL(0))