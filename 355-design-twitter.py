"""
  355. Design Twitter
  [ Medium ] | [ 37.2% ] -- Solved 19/03/2023 -- [ Hash Table, Heap, Linked List ]
  LESS SPACE THAN: 96.0%
  FASTER THAN: 66.4%

  Problem Statement:
  - Design a simple version of Twitter, where users can follow each other, and can see a feed that contains the top 10
    most recent tweets from the people they're following, including their own tweets
  - All operations will be called up to 3x10^4 times, so you can assume they will all be called with roughly equal freq

  Broad Approach:
  - There are two broad approaches:
    - Maintain the correct news feed in a concrete form for each user at every step
    - Build the news feed when it needs to be fetched
  - Compare the two approaches:
    - To maintain the news feed, we need to fan out both post updates, and updates in links in the social graph to all
      m followers
        - postTweet - O(m) - update the feed of m followers
        - unfollow - O(m*n) - go through your feed and remove posts by a particular user
        - follow - go through your feed and insert posts by a user while maintaining sorted order
        - getFeed - O(10) - feed is already maintained, so just fetch the first 10 elements
    - Building the feed when fetched:
      - Apart from getFeed, everything else is O(1) since we just need to update user - followee mappings, or append
        tweet to our list of tweets
      - getFeed - will be O(m*n + 10log(m*n)) - (get all tweets by all followees, heapify, then use nlargest)
  - In reality, many more users read than post on Twitter, so we'd optimize for getFeed
  - However, here there is no difference in the frequency in which any of the 4 ops may be called

  - So its better to go for the first approach that optimizes 3/4 operations

  Specific Approach: Build feed when fetched
  - Build a hashmap that stores userId -> (set of followees (people userId follows), list of tweets)
  - follow/unfollow - add/discard from set
  - postTweet - just append to the list
  - getFeed - get all tweets by all followees, get the nlargest

  Optimizations
  - getFeed - can maintain a heap of size 10, time complexity goes from O(N) to O(Nlog10), but space complexity drops
    from O(N) to O(log(10)) - do this by heapifying at length = 10, then using heappushpop
  - postTweet - we know that in getFeed, we will only get the 10 most recent tweets
    - so, for any user, we also only need to maintain a list of the 10 most recent tweets, since the ones beyond those
      will never be used in the result of getFeed
    - these 10 may be used if this user is the only contributor to some user's news feed
    - a linked list / deque / array with the length capped at 10 can be used

  Time Complexity: getNewsFeed - O(M) (from M*10log(10)), everything else - O(1) - where M is num followees for a user
  Space Complexity: O(N) (from 10N) - where N is the total number of users, M <= N
  # time: k + nlogk vs n*k, space: k, n
"""


from heapq import heapify, heappushpop, nlargest
from collections import deque
class Twitter:

    def __init__(self):
        self.users = {}
        self.time = 0

    def createUser(self, userId):
        if userId not in self.users:
            self.users[userId] = ({userId}, deque()) # Followees, Tweets - user follows itself by default to get own twts

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.createUser(userId)
        self.users[userId][1].append((self.time, tweetId))
        if len(self.users) == 11:
            self.users[userId][1].popLeft()
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        self.createUser(userId)
        followees = self.users[userId][0]
        hp = []
        hp_limited = False
        for followee in followees:
            for post in self.users[followee][1]:
                if len(hp) == 10:
                    heapify(hp)
                    hp_limited = True
                if hp_limited:
                    heappushpop(hp, post)
                    continue
                hp.append(post)
        return [e[1] for e in nlargest(10, hp)]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.createUser(followerId)
        self.createUser(followeeId)
        self.users[followerId][0].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.createUser(followerId)
        self.createUser(followeeId)
        self.users[followerId][0].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
