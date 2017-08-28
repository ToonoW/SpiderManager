# -*- coding: utf-8 -*-
import json
from django.test import TestCase
from django.http import HttpRequest

from backend import models
from backend import api_views


class ScrapydModelTest(TestCase):

    def test_saving_and_retrieving_scrapyd(self):
        """
        测试Scrapyd模型的存取
        """
        first_scrapyd = models.Scrapyd()
        first_scrapyd.name = '1.24'
        first_scrapyd.ip = '192.168.1.24'
        first_scrapyd.port = '8600'
        first_scrapyd.comment = '部署在内网1.24的爬虫部署平台'
        first_scrapyd.save()

        second_scrapyd = models.Scrapyd()
        second_scrapyd.name = '阿里云的一个服务器'
        second_scrapyd.ip = '110.110.120.2'
        second_scrapyd.port = '6800'
        second_scrapyd.comment = '这是一个假的阿里云服务器'
        second_scrapyd.save()

        saved_scrapyds = models.Scrapyd.objects.all()
        self.assertEqual(saved_scrapyds.count(), 2)

        first_saved_scrapyd = saved_scrapyds[0]
        self.assertEqual(first_saved_scrapyd.name, '1.24')
        self.assertEqual(first_saved_scrapyd.ip, '192.168.1.24')
        self.assertEqual(first_saved_scrapyd.port, '8600')
        self.assertEqual(first_saved_scrapyd.comment, '部署在内网1.24的爬虫部署平台')

        second_saved_scrapyd = saved_scrapyds[1]
        self.assertEqual(second_saved_scrapyd.name, '阿里云的一个服务器')
        self.assertEqual(second_saved_scrapyd.ip, '110.110.120.2')
        self.assertEqual(second_saved_scrapyd.port, '6800')
        self.assertEqual(second_saved_scrapyd.comment, '这是一个假的阿里云服务器')


class APIViewsTest(TestCase):
    """
    测试API
    """
    def test_scrapyd_add_node(self):
        """
        测试API增加节点
        :return:
        """
        request = HttpRequest()
        request.method = 'POST'
        request._body = json.dumps({
            'name': '1.24',
            'ip': '192.168.1.24',
            'port': '8600',
            'comment': '内网的服务器'
        })

        api_views.ScrapydView.as_view()(request)
        item = models.Scrapyd.objects.all().last()
        self.assertEqual(item.name, '1.24')

    def test_scrapyd_query_node(self):
        """
        测试API查询节点
        :return:
        """
        request = HttpRequest()
        request.method = 'GET'
        print(api_views.ScrapydView.as_view()(request))