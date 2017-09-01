from django.test import TestCase

from scrapycmd.utils import scrapycmd
from scrapyinfo.tests import ScraoyInfoTest, ScrapydModelTest
from scrapyinfo import models as info_models
from scrapyinfo.utils.scrapyinfo import refresh_all_project_and_scrapy


class ScrapycmdTest(TestCase):

    def test_run_and_cancel_spider(self):
        """
        运行单个爬虫然后取消运行计划
        """
        test = ScraoyInfoTest()
        test.test_fetch_projects()
        refresh_all_project_and_scrapy()

        spider = info_models.Spider.objects.last()
        job = scrapycmd.run_spider(spider)
        print(job)

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

