from django.http import HttpResponse

from django.shortcuts import render


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def schedule(request):
    """
    启动爬虫

        启动任意一个爬虫需要项目名称project和爬虫名称spider,
        爬虫加入计划之后会返回jobid及启动状态
    :param request:
    :return:
    """
    pass

