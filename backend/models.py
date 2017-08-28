# -*- coding: utf-8 -*-
from django.db import models


class Scrapyd(models.Model):
    """
    部署平台
    """
    name = models.CharField(max_length=45, unique=True, verbose_name='部署平台名称')
    ip = models.CharField(max_length=45, blank=False, verbose_name='IP')
    port = models.CharField(max_length=45, verbose_name='端口')
    comment = models.CharField(max_length=128, blank=True, null=True, verbose_name='简介')

    def __str__(self):
        return "{} ({} : {})".format(self.name, self.ip, self.port)


class Project(models.Model):
    """
    爬虫项目
    """
    name = models.CharField(max_length=45, verbose_name='项目名称')
    scrapyd = models.ForeignKey('Scrapyd')
    comment = models.CharField(max_length=128, blank=True, null=True, verbose_name='简介')

    def __str__(self):
        return "{} : {}".format(self.scrapyd.name, self.name)


class Spider(models.Model):
    """
    爬虫
    """
    name = models.CharField(max_length=45, verbose_name='爬虫名称')
    project = models.ForeignKey('Project')
    comment = models.CharField(max_length=128, blank=True, null=True, verbose_name='简介')

    def __str__(self):
        return "{} : {}".format(self.project.name, self.name)


class Group(models.Model):
    """
    分组
    """
    name = models.CharField(max_length=45, verbose_name='分组名称')
    spider = models.ForeignKey('Spider')
    comment = models.CharField(max_length=128, blank=True, null=True, verbose_name='简介')