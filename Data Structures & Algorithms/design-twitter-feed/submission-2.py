class Twitter:

    def __init__(self):
        self.time = 0
        # use list to maintain the chronological order
        self.tweets = defaultdict(list) # userId -> list of [time, tweetId]
        # use set to maintain a unique group of IDs
        self.following = defaultdict(set) # userId -> set of followeeId

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.time, tweetId])
        # record the negative number to simulate the maxHeap
        # so the top value is always the most recent tweet
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        self.following[userId].add(userId)
        # first store the data into the minHeap(outer level)
        for followeeId in self.following[userId]:
            if followeeId in self.tweets:
                # get the idx of the latest tweet
                index = len(self.tweets[followeeId]) - 1
                # retrieve the time and tweetId 
                time, tweetId = self.tweets[followeeId][index]
                # attatch the value on the minHeap, update the index
                heapq.heappush(minHeap, [time, tweetId, followeeId, index - 1])
        
        # now walk through the minHeap and update the res
        while minHeap and len(res) < 10:
            time, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            
            # if there are some tweets posted by this specific userId left
            if index >= 0:
                time, tweetId = self.tweets[followeeId][index]
                heapq.heappush(minHeap, [time, tweetId, followeeId, index - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
