from django.conf import settings

#### Default number of news per page
NEWS_PER_PAGE = getattr(settings, "NEWS_PER_PAGE", 4)

#### Number of truncate words in news
NUMBER_TRUNCATE_WORDS = getattr(settings, "NUMBER_TRUNCATE_WORDS", '40')

#### Configuration for feeds
FEED_TITLE =  getattr(settings, "FEED_TITLE", "News sample application")
FEED_LINK = getattr(settings, "FEED_LINK", "news/")
FEED_DESCRIPTION = getattr(settings, "FEED_DESCRIPTION", "Updates on changes and additions to sample application.")
FEED_COUNT = getattr(settings, "FEED_COUNT", 5)

#### News media path 
NEWS_MEDIA_URL = getattr(settings, "NEWS_MEDIA_URL", "/media/news/")