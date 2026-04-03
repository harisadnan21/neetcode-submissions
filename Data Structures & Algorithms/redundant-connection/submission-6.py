class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # 1 - 2 - 3
        # create a graph map
        # remove the last edge that appears in a cycle
        # detectung cycles union find 
        # need to return the first edge that creates a loop

        parent = [i for i in range(len(edges) + 1)]
        rank = [1 for i in range(len(edges) + 1)]

        def union(n1 , n2):
            # returns true if they are not connected, else false, perform union by rank
            # make the smaller component have the same root as the bigger component

            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False
            rank1, rank2 = rank[p1], rank[p2]
            if rank1 > rank2:
                parent[p2 ] = parent[p1]
                rank[p1] += 1
                rank[p2]= rank[p1]
            else:
                parent[p1] = parent[p2]
                rank[p2] += 1
                rank[p1]= rank[p2]

            return True
        
        def find(node):
            if node == parent[node]:
                return parent[node]
            return find(parent[node])
            

        for a in edges:
            # initially all nodes are parents of themselves,
            # we then determine for each edge what the root parent is and if that 
            # parent is a part of a set we've already visited, we directly join if it is
            # for the later node in a set, connect it to the root of the initail node, 
            # connect smaller to bigger set 
            # we return if the root_ai == root_bi
            print(a)
            if not union(a[0],a[1]):
                return a
            

            






            
