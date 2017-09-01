import requests as rq

from scrapyinfo import models as info_models


def run_spider(spider):
    """
    运行一个爬虫
    :param spider:爬虫
    :return: {"status": "ok", "jobid": "6487ec79947edab326d6db28a2d86511e8247444"}
    """
    scrapyd = spider.project.scrapyd
    url = 'http://{}:{}/schedule.json'.format(scrapyd.ip, scrapyd.port)
    response = rq.post(url, data={
        'project': spider.project.name,
        'spider': spider.name,
    })
    data = response.json()
    status = data.get('status')
    if status != 'ok':
        raise ValueError('请求参数错误')
    else:
        return data


def cancel_spider(spider, job_id):
    """
    取消一个爬虫
    :param job_id: 任务ID
    """
    scrapyd = spider.project.scrapyd
    url = 'http://{}:{}/cancel.json'.format(scrapyd.ip, scrapyd.port)
    response = rq.post(url, data={
        'project': spider.project.name,
        'job': job_id,
    })
    data = response.json()
    status = data.get('status')
    if status != 'ok':
        print(data)
        raise ValueError('请求参数错误')
    else:
        return data


def query_spiders_log(project):
    """
    查看某一project下的爬虫运行记录
    :param project: 需要查询记录的project
    :return:
                {"status": "ok",
                 "pending": [{"id": "78391cc0fcaf11e1b0090800272a6d06", "spider": "spider1"}],
                 "running": [{"id": "422e608f9f28cef127b3d5ef93fe9399", "spider": "spider2", "start_time": "2012-09-12 10:14:03.594664"}],
                 "finished": [{"id": "2f16646cfcaf11e1b0090800272a6d06", "spider": "spider3", "start_time": "2012-09-12 10:14:03.594664", "end_time": "2012-09-12 10:24:03.594664"}]}
    """
    url = 'http://{}:{}/listjobs.json?project={}'.format(project.scrapyd.ip,
                                                         project.scrapyd.port,
                                                         project.name,
                                                         )
    response = rq.get(url)
    data = response.json()
    status = data.get('status')
    if status != 'ok':
        raise ValueError('请求参数错误')
    else:
        return data


def query_all_spiders_log():
    """
    查看所有
    :return:
                {"project_id": 1,
                 "status": "ok",
                 "pending": [{"id": "78391cc0fcaf11e1b0090800272a6d06", "spider": "spider1"}],
                 "running": [{"id": "422e608f9f28cef127b3d5ef93fe9399", "spider": "spider2", "start_time": "2012-09-12 10:14:03.594664"}],
                 "finished": [{"id": "2f16646cfcaf11e1b0090800272a6d06", "spider": "spider3", "start_time": "2012-09-12 10:14:03.594664", "end_time": "2012-09-12 10:24:03.594664"}]}
    """
    projects = info_models.Project.objects.all()

    status_list = list()
    for project in projects:
        status = query_spiders_log(project)
        status['project_id'] = project.id
        status_list.append(status)
    return status_list
