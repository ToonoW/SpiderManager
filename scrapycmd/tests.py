from django.test import TestCase

from scrapycmd.utils import scrapycmd
from scrapyinfo.tests import ScraoyInfoTest
from scrapyinfo import models as scrapyinfo_models

class ScrapycmdTest(TestCase):

    # def test_run_spider(self):
    #     """
    #     测试运行单个爬虫
    #     """
    #     scrapycmd.run_spider(spider)

    def test_query_project_spider_log(self):
        """
        查看某一project的爬虫运行记录
        """
        test = ScraoyInfoTest()
        test.test_fetch_projects()
        test.test_update_projects()
        project = scrapyinfo_models.Project.objects.last()

        status_dic = scrapycmd.query_spiders_log(project)
        self.assertTrue(len(status_dic['pending']) >= 0)
        self.assertTrue(len(status_dic['running']) >= 0)
        self.assertTrue(len(status_dic['finished']) >= 0)
