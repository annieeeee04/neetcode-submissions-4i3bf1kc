class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []
        self.following[userId].add(userId)

        for followeeId in self.following[userId]:
            if followeeId in self.tweets:
                idx = len(self.tweets[followeeId]) - 1
                time, tweetId = self.tweets[followeeId][idx]
                minHeap.append([time, tweetId, followeeId, idx - 1])
            heapq.heapify(minHeap)
        while minHeap and len(res) < 10:
            time, tweetId, followeeId, idx = heapq.heappop(minHeap)
            res.append(tweetId)

            if idx >= 0:
                time, tweetId = self.tweets[followeeId][idx]
                heapq.heappush(minHeap, [time, tweetId, followeeId, idx - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
