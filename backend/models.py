# -*- coding: utf-8 -*-
from django.db import models


class Scrapyd(models.Model):
    name = models.CharField(max_length=45, unique=True, verbose_name='部署平台名称')
    ip = models.CharField(max_length=45, blank=False, verbose_name='IP')
    port = models.CharField(max_length=45, verbose_name='端口')
    comment = models.CharField(max_length=128, blank=True, null=True, verbose_name='简介')