import requests as rq


def query_spiders_log(project):
    """
    查看某一project下的爬虫运行记录
    :param project: 需要查询记录的project
    """
    url = 'http://{}:{}/listjobs.json?project={}'.format(project.scrapyd.ip,
                                           project.scrapyd.port,
                                           project.name,
                                           )
    response = rq.get(url)
    data = response.json()
    status = data.get('status')
    print(status)
    if status != 'ok':
        raise ValueError('请求参数错误')
    else:
        return data
