from django import forms
from django.conf import settings
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string

from news.settings import NEWS_MEDIA_URL

class WYMEditor(forms.Textarea):
    class Media:
        js = (
            'jquery/jquery.js',
            'news/wymeditor/jquery.wymeditor.pack.js',
        )

    def __init__(self, language=None, attrs=None):
        self.language = language or settings.LANGUAGE_CODE[:2]
        self.attrs = {'class': 'wymeditor'}
        if attrs:
            self.attrs.update(attrs)
        super(WYMEditor, self).__init__(attrs)

    def render(self, name, value, attrs=None):
        rendered = super(WYMEditor, self).render(name, value, attrs)
        context = {
            'name': name,
            'lang': self.language[:2],
            'language': self.language,
            'NEWS_MEDIA_URL': NEWS_MEDIA_URL,
        }
        context['page_link_wymeditor'] = 0

        context['filebrowser'] = 0
            
        return rendered + mark_safe(render_to_string(
            'admin/news/widgets/wymeditor.html', context))