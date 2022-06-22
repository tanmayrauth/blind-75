"""
This is a good problem for graph. Don't ignore it. 

First you will create a adj node dict. 
Now since this is undirected graph so while doing dfs you need to keep track of prevNode jst to see if it creates cycle or not. 
Your base condition for dfs should be that if node in visit then return False. 
Then you should run loop over adj node and see if any of it is in prevNode then continue it else return False. 
At the end you also need to make sure that your dfs return True and the length of visit set is equal to the total no of graph nodes. 
This will ensure the whole graph is connected. 

Compare this problem with Course Schedule problem you will find some differences. And check the learning section.
"""

def Solution:
    def validTree(self, n, edges):

        if not n:
            return True

        adj = { i:[] for i in range(n) }
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visit = set()

        def dfs(node, prev):
            if node in visit:
                return False

            visit.add(node) 
            for n in adj[node]:
                if n == prev:
                    continue
                else:
                    if not dfs(n, node):
                        return False 
            return True

        return dfs(0, -1) and len(visit) == n
