# 推特时间线问题有两大类解决途径：1. 推模式push，2. 拉模式pull
# 这里使用pull模式：如果某个用户关注了 k 个用户，我们就可以用合并 k 个有序链表的算法合并出有序的推文列表，正确地 getNewsFeed
# 【注意各种细节性问题】
class Tweet:
    def __init__(self, id_, timestamp):
        # nonlocal timestamp   # 这里有两种选择，1. 时间戳设置为全局变量
        self.id = id_
        self.time = timestamp
        self.next = None

class User:
    def __init__(self, id):
        self.userID = id
        self.tweets = Tweet(None, None)
        self.followings = {id, }
    def post(self, tweetID, timestamp):
        new_tweet = Tweet(tweetID, timestamp)
        new_tweet.next = self.tweets.next  
        self.tweets.next = new_tweet   # 推特链表前边新
        return new_tweet

class Twitter:

    def __init__(self):
        self.timestamp = 0
        self.user_set = {}
        self.ID_to_twitter = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        timestamp = self.timestamp
        if userId not in self.user_set:
            user = User(userId)
            self.user_set[userId] = user
        else:
            user = self.user_set[userId]
        self.ID_to_twitter[tweetId] = user.post(tweetId, timestamp)
        self.timestamp += 1   # 注意这里不能再timestamp上边递增，应该在self.timestamp这个全局变量里边递增

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.user_set: return []
        # n = len(self.user_set[userId].followings)
        if self.user_set[userId].followings is None:
            return []
        queue = []
        for followings_id in iter(self.user_set[userId].followings):   
            if self.user_set[followings_id].tweets.next:
                # 误区：不用分别按照用户新建list，只需要维护一个heapq
                # queues.append(self.user_set[followings_id].tweets)
                time = self.user_set[followings_id].tweets.next.time
                tweetId = self.user_set[followings_id].tweets.next.id
                # 直接存tweet引用不行，指向tweet对象的引用之间不能比较大小
                # tweet = self.user_set[followings_id].tweets.next
                heapq.heappush(queue, (-time, tweetId))
        i = 0
        res = []
        while queue and  i < 10:
            # print(queue)
            time, curr_tweet_id = heapq.heappop(queue)
            time = -time
            curr_tweet = self.ID_to_twitter[curr_tweet_id]
            res.append(curr_tweet.id)
            i += 1
            if curr_tweet.next:
                time = curr_tweet.next.time
                heapq.heappush(queue, (-time, curr_tweet.next.id))
        return res
            # for followings_id in iter(self.user_set[userId].followings):
            #     new_time = self.user_set[followings_id].tweets.next.time
        # n = len(queues)
        # q = []



    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.user_set: 
            follower = User(followerId)
            self.user_set[followerId] = follower
        if followeeId not in self.user_set: 
            followee = User(followeeId)
            self.user_set[followeeId] = followee
        follower = self.user_set[followerId]
        followee = self.user_set[followeeId]
        follower.followings.add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        # if followerId not in self.user_set: follower = User(followerId)
        # if followeeId not in self.user_set: followee = User(followeeId)
        follower = User(followerId) if followerId not in self.user_set else self.user_set[followerId]
        if followeeId in follower.followings:
            follower.followings.remove(followeeId)



# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)