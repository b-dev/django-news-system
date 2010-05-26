from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from news.models import News
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from news.settings import NEWS_PER_PAGE, NUMBER_TRUNCATE_WORDS
from django.http import Http404

def listing(request, page=None):
    news_list = News.pubs_objects.all()
    paginator = Paginator(news_list, NEWS_PER_PAGE)
    
    # Make sure page request is an int. If not, deliver first page.
    if page is None:
        page = 1

    # If page request (9999) is out of range, deliver last page of results.
    try:
        news = paginator.page(page)
    except (EmptyPage, InvalidPage):
        news = paginator.page(paginator.num_pages)

    return render_to_response('news/news_listing.html',
        {
         'news': news,
         'words': NUMBER_TRUNCATE_WORDS,
        },
        context_instance=RequestContext(request))
    
def news_details(request, slug=None, page_id=None):
    news = get_object_or_404(News, slug=slug)
    
    if news.published != True:
        raise Http404
    
    # Make sure page request is an int. If not, deliver first page.
    try:
        page_id = int(request.GET.get('page', '1'))
    except ValueError:
        page_id = 1
    
    return render_to_response('news/news_detail.html',
        {
         'news': news,
         'page_id': page_id,
        },
        context_instance=RequestContext(request))