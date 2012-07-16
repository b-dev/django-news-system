from django.conf.urls.defaults import *
from news.feeds import RssLatestNewsFeed, AtomLatestNewsFeed


urlpatterns = patterns('news.views',
    url(r'^$', 'listing', name='list-news'),
    url(r'^(?P<page>\d+)/$', 'listing', name='list-news'),
    url(r'^(?P<slug>[\w-]+)/(?P<page_id>\d+)/$', 'news_details', name='news-details'),
)

urlpatterns += patterns('',
    # RSS
    (r'feeds/rss/$', RssLatestNewsFeed()),
    (r'feeds/atom/$', AtomLatestNewsFeed())
)
