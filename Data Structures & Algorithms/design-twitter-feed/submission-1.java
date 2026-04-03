
class Twitter {

    // userId -> list of [time, tweetId]
    Map<Integer, List<int[]>> tweetMap;

    // followerId -> set of followeeIds
    Map<Integer, Set<Integer>> followMap;

    int count;

    public Twitter() {
        count = 0;
        followMap = new HashMap<>();
        tweetMap = new HashMap<>();
    }

    public void postTweet(int userId, int tweetId) {
        tweetMap.putIfAbsent(userId, new ArrayList<>());
        tweetMap.get(userId).add(new int[]{count++, tweetId});
    }

    public List<Integer> getNewsFeed(int userId) {
        List<Integer> ret = new ArrayList<>();

        // Min-heap by time; keep ONLY the 10 most recent tweets
        PriorityQueue<int[]> minHeap =
            new PriorityQueue<>((a, b) -> Integer.compare(a[0], b[0]));

        // Build sources: self + followees
        Set<Integer> sources = new HashSet<>();
        sources.add(userId);
        sources.addAll(followMap.getOrDefault(userId, Collections.emptySet()));

        // Add all tweets from sources, but keep heap size <= 10
        for (int uid : sources) {
            List<int[]> tweets = tweetMap.getOrDefault(uid, Collections.emptyList());
            for (int[] tw : tweets) {
                minHeap.offer(tw);
                if (minHeap.size() > 10) {
                    minHeap.poll(); // remove oldest among kept tweets
                }
            }
        }

        // Heap currently has up to 10 most recent, but in ascending time.
        // Pop into a list then reverse to get most recent -> least recent.
        List<int[]> tmp = new ArrayList<>();
        while (!minHeap.isEmpty()) tmp.add(minHeap.poll());
        for (int i = tmp.size() - 1; i >= 0; i--) {
            ret.add(tmp.get(i)[1]); // tweetId
        }

        return ret;
    }

    public void follow(int followerId, int followeeId) {
        if (followerId == followeeId) return;

        followMap.putIfAbsent(followerId, new HashSet<>());
        followMap.get(followerId).add(followeeId);
    }

    public void unfollow(int followerId, int followeeId) {
        if (followerId == followeeId) return;
        Set<Integer> set = followMap.get(followerId);
        if (set == null) return;
        set.remove(followeeId);
    }
}