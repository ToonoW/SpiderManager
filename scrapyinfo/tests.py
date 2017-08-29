import json
from django.test import TestCase, Client
from django.core.urlresolvers import reverse

from scrapyinfo import models, api_views
from scrapyinfo.utils import scrapyinfo


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


class ScraoyInfoTest(TestCase):

    def test_fetch_projects(self):
        """
        测试拉取project信息
        """
        scrapyd = self.create_scrapyd()

        projects = scrapyinfo.fetch_projects(scrapyd)
        self.assertEqual(type(projects), list)

    def test_update_projects(self):
        """
        测试存储project
        """
        scrapyd = self.create_scrapyd()
        scrapyd.save()

        projects = scrapyinfo.fetch_projects(scrapyd)
        scrapyinfo.update_projects(scrapyd, projects)

        pjs = models.Project.objects.all()
        self.assertEqual(len(projects), pjs.count())
        for p in pjs:
            self.assertTrue(p.name in projects)

    def test_fetch_spiders(self):
        """
        测试拉取spider信息
        """
        self.test_fetch_projects()
        self.test_update_projects()
        project = models.Project.objects.all().last()

        spiders = scrapyinfo.fetch_spiders(project)
        self.assertEqual(type(spiders), list)

    def test_update_spiders(self):
        """
        测试存储spider
        """
        self.test_fetch_projects()
        self.test_update_projects()
        project = models.Project.objects.all().last()

        spiders = scrapyinfo.fetch_spiders(project)
        scrapyinfo.update_spiders(project, spiders)

        sps = models.Spider.objects.all()
        self.assertEqual(len(spiders), sps.count())
        for s in sps:
            self.assertTrue(s.name in spiders)

    def test_refresh_project_and_scrapy(self):
        """仅进行运行测试"""
        scrapyd = models.Scrapyd.objects.all().last()
        if scrapyd is not None:
            scrapyinfo.refresh_project_and_scrapy(scrapyd)

    def test_refresh_all_project_and_scrapy(self):
        """仅进行运行测试"""
        scrapyinfo.refresh_all_project_and_scrapy()

    def create_scrapyd(self):
        scrapyd = models.Scrapyd()
        scrapyd.name = '1.24'
        scrapyd.ip = '192.168.1.24'
        scrapyd.port = '8600'
        return scrapyd


class APITest(TestCase):

    def test_refresh_platform_information(self):
        """
        测试刷新平台信息API
        """
        c = Client()
        print(reverse('refresh-platform-information'))
        response = c.get(reverse('refresh-platform-information'))
