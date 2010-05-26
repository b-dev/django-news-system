'''
Created on May 18, 2010

@author: grokrz
'''
from django import forms
from news.models import News
from news.widgets import WYMEditor

class NewsAdminModelForm(forms.ModelForm):
    body = forms.CharField(widget=WYMEditor())

    class Meta:
        model = News