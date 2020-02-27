import unittest
from typing import List


class TweetCounts:

    def __init__(self):
        self.time_map = {
            'minute': 60,
            'hour': 60 * 60,
            'day': 24 * 60 * 60,
        }
        self.tweeters: [str, List] = {}

    def recordTweet(self, tweetName: str, time: int) -> None:
        l = self.tweeters.setdefault(tweetName, [])
        l.append(time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        l = self.tweeters[tweetName]
        f = self.time_map[freq]
        count = {}
        for t in l:
            if startTime <= t <= endTime:
                count.setdefault((t - startTime) // f, 0)
                count[(t - startTime) // f] += 1

        curr = 0
        res = []
        while curr <= endTime - startTime:
            if curr // f in count:
                res.append(count[curr // f])
            else:
                res.append(0)
            curr += f

        return res


class Test(unittest.TestCase):

    def test(self):
        tweet_counts = TweetCounts()
        tweet_counts.recordTweet("tweet3", 0)
        tweet_counts.recordTweet("tweet3", 60)
        tweet_counts.recordTweet("tweet3", 10)

        self.assertEqual([2], tweet_counts.getTweetCountsPerFrequency("minute", "tweet3", 0, 59))
        self.assertEqual([2, 1], tweet_counts.getTweetCountsPerFrequency("minute", "tweet3", 0, 60))

        tweet_counts.recordTweet("tweet3", 120)
        self.assertEqual([4], tweet_counts.getTweetCountsPerFrequency("hour", "tweet3", 0, 210))


if __name__ == '__main__':
    unittest.main()
