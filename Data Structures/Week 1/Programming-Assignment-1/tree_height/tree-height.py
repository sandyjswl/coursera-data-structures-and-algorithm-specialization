# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeHeight:
        def read(self):
                self.n = int(sys.stdin.readline())
                self.parent = list(map(int, sys.stdin.readline().split()))
                self.nodes={}
                for i in range(self.n):
                    self.nodes[i]=[]
                for i in range(self.n):
                    if self.parent[i]==-1:
                        pass
                    else:
                        self.nodes[self.parent[i]]+=[i]        

        def compute_height(self):
                # Replace this code with a faster implementation
                root=None
                try:
                    root=self.parent.index(-1)
                except ValueError:
                    return 0    
                queue=[]
                queue.append(root)
                height=0

                while True:
                    count_node=len(queue)
                    if count_node==0:
                        return height
                    height=height+1
                    while count_node>0:
                        node=queue[0]
                        queue.pop(0)
                        if self.nodes[node]:
                            for i in self.nodes[node]:
                                queue.append(i)  
                        count_node=count_node-1          

def main():
  tree = TreeHeight()
  tree.read()
  print(tree.compute_height())

threading.Thread(target=main).start()
