"""
355. Design Twitter

This module implements a simplified version of Twitter supporting:
    - Posting tweets
    - Following/unfollowing users
    - Fetching the 10 most recent tweets from a user's news feed

Problem:
    Design a class Twitter that supports the following APIs:
        postTweet(userId, tweetId):
            Compose a new tweet.

        getNewsFeed(userId):
            Retrieve the 10 most recent tweet IDs in the user's feed.
            The feed should include:
                - The user’s own tweets
                - Tweets from all users they follow
            Tweets must be returned in descending order of time.

        follow(followerId, followeeId):
            Follower subscribes to followee’s tweets.

        unfollow(followerId, followeeId):
            Follower unsubscribes from followee’s tweets.
            Users cannot unfollow themselves.

Key Data Structures:
    - feed:       dict[userId -> List[(time, tweetId)]]
                  Stores each user's tweets along with a global timestamp.

    - followee:   dict[followerId -> Set[followeeIds]]
                  Tracks follow relationships.

    - Global timestamp increments on each post to guarantee ordering.

Core Algorithm:
    - Tweets are stored per user along with a timestamp.
    - In getNewsFeed():
          * Ensure the user follows themselves.
          * For each followee, push their most recent tweet into a max-heap.
          * Pop the heap up to 10 times to build the news feed.
          * Each pop reveals the next-oldest tweet from that same user.

Complexity:
    - postTweet:     O(1)
    - follow:        O(1)
    - unfollow:      O(1)
    - getNewsFeed:   O(k log k)
                     where k = number of followees (including self)

                     Each followee contributes only their most recent tweet,
                     and at most 10 heap pops occur for building the feed.
"""

from collections import defaultdict
import heapq

class Twitter(object):

    def __init__(self):
        self.time = 0
        self.feed = defaultdict(list)
        self.followee = defaultdict(set)
        

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet by userId.
        """
        self.time += 1
        self.feed[userId].append((self.time, tweetId))
        

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweets visible to userId.
        """
        # Always include the user's own tweets
        self.followee[userId].add(userId)

        max_heap = []

        # Push the most recent tweet from each followee into heap
        for fol in self.followee[userId]:
            if self.feed[fol]:
                time, tweetId = self.feed[fol][-1]
                idx = len(self.feed[fol]) - 1
                data = (-time, tweetId, fol, idx)
                heapq.heappush(max_heap, data)

        result = []

        # Extract up to 10 most recent tweets
        while max_heap and len(result) < 10:
            time, tweetid, user, idx = heapq.heappop(max_heap)
            result.append(tweetid)

            # Push the next older tweet from the same user
            idx -= 1
            if idx >= 0:
                time1, tweetId1 = self.feed[user][idx]
                data = (-time1, tweetId1, user, idx)
                heapq.heappush(max_heap, data)

        return result


    def follow(self, followerId, followeeId):
        """
        followerId starts following followeeId.
        """
        if followerId != followeeId:
            self.followee[followerId].add(followeeId)
        

    def unfollow(self, followerId, followeeId):
        """
        followerId stops following followeeId.
        Cannot unfollow self.
        """
        if followerId != followeeId and followerId in self.followee:
            # Use remove() because your original code uses remove
            # (discard() would also be safe)
            if followeeId in self.followee[followerId]:
                self.followee[followerId].remove(followeeId)


tw = Twitter()
tw.postTweet(1, 5)
print(tw.getNewsFeed(1))   # Expected: [5]
tw.follow(1, 2)
tw.postTweet(2, 6)
print(tw.getNewsFeed(1))   # Expected: [6, 5]
tw.unfollow(1, 2)
print(tw.getNewsFeed(1))   # Expected: [5]