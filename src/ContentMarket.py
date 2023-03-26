from typing import List, Tuple
from ContentMarketConsumer import ContentMarketConsumer
from ContentMarketProducer import ContentMarketProducer
from ContentMarketCoreNode import ContentMarketCoreNode
import datetime


class ContentMarket:
    """
    A class that represents the a content market and calculates information about
    users/tweets demands, supplies and causations
    """

    consumers: List[ContentMarketConsumer]
    producers: List[ContentMarketProducer]
    core_node: ContentMarketCoreNode
    computed_causations: List[float]

    def __init__(self, users, core_node):
        self.consumers, self.producers = self.split_users(users)
        self.core_node = core_node
        self.computed_causations = []

    """
    Decide when we see data
    """

    def split_users(self, users):
        return [], []

    def calulate_demand(self, content: TweetContent, content_radius: int, user_ids: List[str], time_range: Tuple(datetime)):
        demand = 0
        for user_id in user_ids:
            user_tweets = get_tweets(user_id, time_range)  # db query
            for tweet in user_tweets:
                if tweet.type == TweetContent.TWEET and norm(tweet.content - content) < content_radius:
                    demand += 1
        return demand

    def calculate_supply(self, content: TweetContent, content_radius: int, user_ids: List[str], time_range: Tuple(datetime)):
        supply = 0
        for user_id in user_ids:
            user_tweets = get_tweets(user_id, time_range)  # db query
            for tweet in user_tweets:
                if tweet.type == TweetContent.RETWEET and norm(tweet.content - content) < content_radius:
                    supply += 1
        return supply

    def calculate_causation(self):
        pass
