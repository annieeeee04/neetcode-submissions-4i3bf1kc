class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list) # userId -> (time, tweetId)
        self.following = defaultdict(set) # userId -> [followeeId]

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        maxHeap = []
        self.following[userId].add(userId)

        for followeeId in self.following[userId]:
            if followeeId in self.tweets:
                idx = len(self.tweets[followeeId]) - 1
                time, tweetId = self.tweets[followeeId][idx]
                maxHeap.append((time, tweetId, followeeId, idx - 1))
            heapq.heapify(maxHeap)
        
        while maxHeap and len(res) < 10:
            time, tweetId, followeeId, idx = heapq.heappop(maxHeap)
            res.append(tweetId)
            if idx >= 0:
                time, tweetId = self.tweets[followeeId][idx]
                heapq.heappush(maxHeap, (time, tweetId, followeeId, idx-1))
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
