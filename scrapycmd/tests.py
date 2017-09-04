import json
from django.test import TestCase
from django.core.urlresolvers import reverse

from public.test import APITestCase
from scrapycmd.utils import scrapycmd
from scrapyinfo.tests import ScraoyInfoTest
from scrapyinfo import models as info_models
from scrapyinfo.utils.scrapyinfo import refresh_all_project_and_scrapy


class ScrapycmdTest(TestCase):

    def setUp(self):
        test = ScraoyInfoTest()
        test.test_fetch_projects()
        refresh_all_project_and_scrapy()

    def test_run_and_cancel_spider(self):
        """
        运行单个爬虫然后取消运行计划
        """

        spider = info_models.Spider.objects.last()
        job = scrapycmd.run_spider(spider)

        status = scrapycmd.cancel_spider(spider, job['jobid'])
        self.assertEqual(status['status'], 'ok')

    def test_query_project_spiders_log(self):
        """
        查看某一project的爬虫运行记录
        """
        test = ScraoyInfoTest()
        test.test_fetch_projects()
        test.test_update_projects()
        project = info_models.Project.objects.last()

        status_dic = scrapycmd.query_spiders_log(project)
        self.assertTrue(len(status_dic['pending']) >= 0)
        self.assertTrue(len(status_dic['running']) >= 0)
        self.assertTrue(len(status_dic['finished']) >= 0)

    def test_query_all_project_spiders_log(self):
        """
        查看所有project的爬虫运行记录
        """
        test = ScraoyInfoTest()
        test.test_fetch_projects()
        test.test_update_projects()

        status_list = scrapycmd.query_all_spiders_log()
        for status in status_list:
            self.assertTrue(status['project_id'] is not None)
            self.assertTrue(len(status['pending']) >= 0)
            self.assertTrue(len(status['running']) >= 0)
            self.assertTrue(len(status['finished']) >= 0)


class APITest(APITestCase):

    def setUp(self):
        test = ScraoyInfoTest()
        test.test_fetch_projects()
        refresh_all_project_and_scrapy()

        self.c.post(reverse('group-list'), data={
            'name': '新闻分组',
            'spiders': [1, 2],
            'comment': '两个爬虫',
        })

    def test_query_spiders_log(self):
        """
        测试查询某个project下的爬虫信息
        """
        # 正常请求
        response = self.c.get(reverse('query-spiders-log') + '?project_id=1')
        self.assert_status_true(response)

        # 参数不正确
        response = self.c.get(reverse('query-spiders-log') + '?project=wer')
        self.assert_status_false(response)

        # 参数缺失
        response = self.c.get(reverse('query-spiders-log'))
        self.assert_status_false(response)

    def test_query_all_spiders_log(self):
        """
        测试查询所有爬虫运行记录
        """
        response = self.c.get(reverse('query-all-spiders-log'))
        self.assert_status_true(response)

    def test_run_and_cancel_spider(self):
        """
        测试运行单个爬虫
        """
        # 正常请求
        response = self.c.get(reverse('run-spider')+'?spider_id=1')
        self.assert_status_true(response)

        # 取消爬虫
        response = self.c.get(reverse('cancel-spider')+'?spider_id=1')
        self.assert_status_true(response)

        # 参数不正确
        response = self.c.get(reverse('run-spider')+'?spider_id=gouzi')
        self.assert_status_false(response)

        # 参数缺失
        response = self.c.get(reverse('run-spider'))
        self.assert_status_false(response)

    def test_run_group_spiders(self):
        """
        测试运行分组爬虫
        """
        # 正常请求
        response = self.c.get(reverse('run-group-spiders')+'?group_id=1')
        self.assert_status_true(response)

        # 取消爬虫
        response = self.c.get(reverse('cancel-group-spiders') + '?group_id=1')
        self.assert_status_true(response)

        # 参数不正确
        response = self.c.get(reverse('run-group-spiders') + '?group_id=sdf')
        self.assert_status_false(response)

        # 参数缺失
        response = self.c.get(reverse('run-group-spiders'))
        self.assert_status_false(response)