# -*- coding: utf-8 -*-
from django.test import TestCase
from django.test.client import Client

class NewsEmptyTestCase(TestCase):
    
    def test_01_empty_news(self):
        c = Client()
                
        response = c.get('/news/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('No news so far' in response.content)
        
        response = c.get('/news/1', follow=True)
        self.assertEqual(response.status_code, 200)
 
class NewsTestCase(TestCase):
    fixtures = ['test_auth.json', 'test_news.json']

    def test_01_news(self):
        c = Client()
        
        response = c.get('/news/', follow=True)
        self.assertEqual(response.status_code, 200)
        
        response = c.get('/news/1/', follow=True)
        self.assertEqual(response.status_code, 200)

        response = c.get('/news/2/', follow=True)
        self.assertEqual(response.status_code, 200)
        
        response = c.get('/news/?page=3000', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('<a href="/news/2/">2</a>' in response.content)
        
    def test_02_news(self):
        c = Client()
        
        response = c.get('/news/lorem-ipsum-dolor-sit-amet/1/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('<a href="/news/1/">' in response.content)
        
        response = c.get('/news/2/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('<h4><a href="/news/cum-sociis-natoque-penatibus-e/2/">Cum sociis natoque penatibus e</a></h4>' in response.content)

class FeedsTestCase(TestCase):
    fixtures = ['test_auth.json', 'test_news.json']
    
    def test_01_feeds(self):
        c = Client()
        
        response = c.get('/news/feeds/rss/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('<item><title>It is a long established fact </title><link>http://www.test1.pl' in response.content)
