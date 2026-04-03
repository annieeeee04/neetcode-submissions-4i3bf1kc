class Twitter:

    def __init__(self):
        self.time = 0
        # userId -> list of tweets
        self.tweets = defaultdict(list) 
        # userId -> set of [time, followeeID]
        self.following = defaultdict(set) 
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.time, tweetId])
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        self.following[userId].add(userId)

        for followeeId in self.following[userId]:
            if followeeId in self.tweets:
                index = len(self.tweets[followeeId]) - 1
                time, tweetId = self.tweets[followeeId][index]
                heapq.heappush(minHeap, [time, tweetId, followeeId, index - 1])
        
        while minHeap and len(res) < 10:
            time, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)

            if index >= 0:
                time, tweetId = self.tweets[followeeId][index]
                heapq.heappush(minHeap, [time, tweetId, followeeId, index - 1])
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
