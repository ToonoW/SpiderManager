import json

from public.views import APIView
from scrapycmd.utils import scrapycmd as scrapycmd_utils
from scrapyinfo import models as info_models


class QuerySpidersLog(APIView):
    """
    查询一个project的爬虫运行记录
    """

    def get(self, request):
        project_id = request.GET.get('project_id')
        if project_id is None or not project_id.isdigit():
            self.status = False
            self.msg = '提供参数错误'
            return self.json_response()
        else:
            project_id = int(project_id)
            project = info_models.Project.objects.filter(id=project_id).first()
            if project is None:
                self.status = False
                self.msg = '项目不存在'
                return self.json_response()
            data = scrapycmd_utils.query_spiders_log(project)

            self.status = data['status'] == 'ok'
            if data['status'] == 'ok':
                self.msg = '项目{}记录查询成功'.format(project.name)
                return self.json_response(data)
            else:
                self.msg = '项目{}记录查询失败'.format(project.name)
                return self.json_response()


class QueryAllSpidersLog(APIView):
    """
    查询所有项目的爬虫运行记录
    """

    def get(self, _):
        data = scrapycmd_utils.query_all_spiders_log()

        if len(data) > 0:
            self.status = True
            return self.json_response(data)
        else:
            self.status = False
            self.msg = '未知错误'
            return self.json_response()


class RunSpider(APIView):
    """
    运行一个爬虫
    """

    def get(self, request):
        spider_id = request.GET.get('spider_id')
        if spider_id is None or not spider_id.isdigit():
            self.status = False
            self.msg = '提供参数错误'
            return self.json_response()
        else:
            spider_id = int(spider_id)
            spider = info_models.Spider.objects.filter(id=spider_id).first()
            if spider is None:
                self.status = False
                self.msg = '爬虫不存在'
                return self.json_response()
            data = scrapycmd_utils.run_spider(spider)

            self.status = data['status'] == 'ok'
            if data['status'] == 'ok':
                self.msg = '爬虫{}启动成功'.format(spider.name)
            else:
                self.msg = '爬虫启动失败'
            return self.json_response()


class RunGroupSpiders(APIView):
    """
    运行一个分组的爬虫
    """
    def get(self, request):
        group_id = request.GET.get('group_id')
        if group_id is None or not group_id.isdigit():
            self.status = False
            self.msg = '提供参数错误'
            return self.json_response()
        else:
            group_id = int(group_id)
            group = info_models.Group.objects.filter(id=group_id).first()
            if group is None:
                self.status = False
                self.msg = '分组不存在'
                return self.json_response()

            success = 0
            failure = 0
            datas = list()
            for spider in group.spiders.all():
                data = scrapycmd_utils.run_spider(spider)
                data['name'] = spider.name
                data['id'] = spider.id
                datas.append(data)
                if data['status'] == 'ok':
                    success += 1
                else:
                    failure += 1

            self.status = True
            self.msg = '总共{}，启动成功{}个，启动失败{}'.format(group.spiders.count(),
                                                    success,
                                                    failure)
            return self.json_response({
                'data': datas,
                'total': group.spiders.count(),
                'success': success,
                'failure': failure,
            })


class CancelSpider(APIView):
    """
    取消一个爬虫计划
    """
    def get(self, request):
        spider_id = request.GET.get('spider_id')
        if spider_id is None or not spider_id.isdigit():
            self.status = False
            self.msg = '提供参数错误'
            return self.json_response()
        else:
            spider_id = int(spider_id)
            spider = info_models.Spider.objects.filter(id=spider_id).first()
            if spider is None:
                self.status = False
                self.msg = '爬虫不存在'
                return self.json_response()

            # 取消这个爬虫的所有job
            content = scrapycmd_utils.query_spiders_log(spider.project)
            if content['status'] != 'ok':
                self.status = False
                self.msg = '未知错误'
                return self.json_response()
            jobs = content.get('pending') + content.get('running')
            aim_jobs = scrapycmd_utils.filter_spider_job_id(jobs, spider)

            success = 0
            failure = 0
            datas = list()
            for job in aim_jobs:
                data = scrapycmd_utils.cancel_spider(spider, job)
                data['name'] = spider.name
                data['id'] = spider.id
                datas.append(data)
                if data['status'] == 'ok':
                    success += 1
                else:
                    failure += 1

            self.status = True
            self.msg = '爬虫{}取消成功'.format(spider.name)

            return self.json_response({
                'data': datas,
                'total': len(jobs),
                'success': success,
                'failure': failure,
            })


class CancelGroupSpiders(APIView):
    """
    取消一个分组爬虫计划
    """
    def get(self, request):
        group_id = request.GET.get('group_id')
        if group_id is None or not group_id.isdigit():
            self.status = False
            self.msg = '提供参数错误'
            return self.json_response()
        else:
            group_id = int(group_id)
            group = info_models.Group.objects.filter(id=group_id).first()
            if group is None:
                self.status = False
                self.msg = '分组不存在'
                return self.json_response()

            success = 0
            failure = 0
            datas = list()
            for spider in group.spiders.all():
                # 取消这个爬虫的所有job
                content = scrapycmd_utils.query_spiders_log(spider.project)
                if content['status'] != 'ok':
                    self.status = False
                    self.msg = '未知错误'
                    return self.json_response()
                jobs = content.get('pending') + content.get('running')
                aim_jobs = scrapycmd_utils.filter_spider_job_id(jobs, spider)

                for job in aim_jobs:
                    data = scrapycmd_utils.cancel_spider(spider, job)
                    data['name'] = spider.name
                    data['id'] = spider.id
                    datas.append(data)
                    if data['status'] == 'ok':
                        success += 1
                    else:
                        failure += 1

            self.status = True
            self.msg = '爬虫分组{}取消成功'.format(group.name)

            return self.json_response({
                'data': datas,
                'total': success + failure,
                'success': success,
                'failure': failure,
            })