"""
爬虫信息模块
与Scrapyd通信的功能函数
"""
import requests as rq
import logging


from scrapyinfo import models


def refresh_all_project_and_scrapy():
    """
    刷新所有scrapyd下的project和scrapy
    """
    scrapyds = models.Scrapyd.objects.all()
    for scrapyd in scrapyds:
        refresh_project_and_scrapy(scrapyd)


def refresh_project_and_scrapy(scrapyd):
    """
    根据scrapyd刷新project和scrapy
    """
    projects = fetch_projects(scrapyd)
    update_projects(projects)

    projects = models.Project.objects.filter(scrapyd=scrapyd)
    for p in projects:
        spiders = fetch_spiders(p)
        update_spiders(spiders)


def fetch_projects(scrapyd):
    """
    从scrapyd中拉取project
    :return: project数组
    """
    response = rq.get('http://{}:{}/listprojects.json'.format(scrapyd.ip, scrapyd.port))
    data = response.json()
    status = data.get('status')
    if status == 'ok':
        return data['projects']
    else:
        logging.warning('{} {}拉取project列表失败'.format(scrapyd.id, scrapyd.name))
        raise ValueError('未知错误，无法拉取project列表')


def update_projects(scrapyd, projects):
    """
    更新某个Scrapyd属下的project
    """
    pjs = models.Project.objects.filter(scrapyd=scrapyd)
    pjs_set = set(map(lambda x: x.name, pjs))
    projects_set = set(projects)
    deprecated_projects = pjs_set - projects_set
    new_projects = projects_set - pjs_set

    for p in deprecated_projects:
        models.Project.objects.filter(name=p).delete()
    for p in new_projects:
        pj = models.Project()
        pj.name = p
        pj.scrapyd = scrapyd
        pj.save()


def fetch_spiders(project):
    """
    从scrapyd中拉取spider
    :return: spider数组
    """
    response = rq.get('http://{}:{}/listspiders.json?project={}'.format(project.scrapyd.ip,
                                                                        project.scrapyd.port,
                                                                        project.name))
    data = response.json()
    status = data.get('status')
    if status == 'ok':
        return data['spiders']
    else:
        logging.warning('{} {}拉取spider列表失败'.format(project.id, project.name))
        raise ValueError('未知错误，无法拉取spider列表')


def update_spiders(project, spiders):
    """
    更新某个project下的spider
    :param project: 所属的项目
    :param spiders: 爬虫名字列表
    """
    sps = models.Spider.objects.filter(project=project)
    sps_set = set(map(lambda x: x.name, sps))
    spiders_set = set(spiders)
    deprecated_spiders = sps_set - spiders_set
    new_spiders = spiders_set - sps_set

    for s in deprecated_spiders:
        models.Spider.objects(name=s).delete()
    for s in new_spiders:
        sp = models.Spider()
        sp.name = s
        sp.project = project
        sp.save()