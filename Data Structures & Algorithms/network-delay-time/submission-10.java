
class Solution {
    
    public int networkDelayTime(int[][] times, int n, int k) {
        // create adjacency list
        // create a hashmap of nodes to min time
        // run dijsktra's
        // return maximum time from hashmap of min times
        Map<Integer, Integer> nodeToMinTime = new HashMap<>();
        // {1 : [[2, 1],  ...
        Map<Integer, List<int[]>> nodeToEdges = new HashMap<>();
        for (int i = 1; i <= n ; i ++){
            nodeToMinTime.putIfAbsent(i, Integer.MAX_VALUE/2);
        }
        for (int i = 0 ; i < times.length; i ++){
            int[] edge = times[i];
            List<int[]> nodeEdges = nodeToEdges.getOrDefault(edge[0], new ArrayList<int[]>());
            nodeEdges.add(new int[]{edge[1], edge[2]});
            nodeToEdges.put(edge[0], nodeEdges);
        }
        // Now the nodes are made and edges are noted
        //initialise distance for source to 0
        nodeToMinTime.put(k, 0);

        //initialise the min heap 
        PriorityQueue<int[]> heap = new PriorityQueue<>((a,b) -> Integer.compare(a[0], b[0]));
        Set<Integer> visited = new HashSet<>();
        // Add [currDistToSource, Node] to PQ
        heap.offer(new int[]{0, k});
        while (heap.size() > 0){
            int[] edge = heap.poll();
            int dist = edge[0];
            int node = edge[1];
            if (visited.contains(node)){
                continue;
            }
            List<int[]> edgeLst = nodeToEdges.getOrDefault(node, new ArrayList<>());
            for ( int[] neighborAndWeights : edgeLst){
                int neighNode = neighborAndWeights[0];
                int weight = neighborAndWeights[1];

                if (weight + dist < nodeToMinTime.get(neighNode)){
                    nodeToMinTime.put(neighNode, weight + dist);
                    heap.offer(new int[]{weight + dist, neighNode});
                }
            }
            visited.add(node);
        }

        int ret =0;
        for (int i = 1; i <= n ; i ++){
            int val = nodeToMinTime.get(i);
            if (val == Integer.MAX_VALUE/2){
                return -1;
            }
            ret = Math.max(ret, val);

        }
        return ret; 
    }

}
