import Queue
import stackDS
class Graph():
    def __init__(self,nodes):
        self.nodes=nodes
        #item then the for loop(for however many times you want to add item)
        self.ad_list=[[]for i in range(nodes)]
        "print(self.ad_list)"

    def add_edge(self,node1,node2):
        self.ad_list[node1].append(node2)
        self.ad_list[node2].append(node1)
        "print(self.ad_list)"

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
    def dfs_traversal(self,start):
        visited=[]
        stack=stackDS.Stack(self.nodes)
        stack.push(start)
        while not stack.is_empty():
            popped=stack.pop()
            visited.append(popped)
            for i in self.ad_list[popped]:
                if i not in visited and not stack.check_item(i):
                    stack.push(i)
        return visited

"""
a=Graph(6)
a.add_edge(0,1)
a.add_edge(0,2)
a.add_edge(1,3)
a.add_edge(1,4)
a.add_edge(2,3)
a.add_edge(2,5)
print(a.bfs_traversAL(4))
print(a.dfs_traversal(4))"""