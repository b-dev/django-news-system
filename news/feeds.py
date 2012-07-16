from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Atom1Feed, Rss201rev2Feed
from news.models import News
from news.settings import FEED_TITLE, FEED_LINK, FEED_DESCRIPTION, FEED_COUNT

class RssLatestNewsFeed(Feed):
    feed_type = Rss201rev2Feed
    title = FEED_TITLE
    link = FEED_LINK
    description = FEED_DESCRIPTION

    def items(self):
        return News.pubs_objects.all()[:FEED_COUNT]

class AtomLatestNewsFeed(RssLatestNewsFeed):
    feed_type = Atom1Feed
    subtitle = RssLatestNewsFeed.description

