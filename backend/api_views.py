import requests as rq
import json
from django.views.generic import View
from django.http import JsonResponse

from backend.scrapy_info import scrapyd


class JSONResponseMixin(object):
    """
    A mixin that can be used to render a JSON response.
    """
    def render_to_json_response(self, context, **response_kwargs):
        """
        Returns a JSON response, transforming 'context' to make the payload.
        """
        return JsonResponse(
            self.get_data(context),
            **response_kwargs
        )

    def get_data(self, context):
        """
        Returns an object that will be serialized as JSON by json.dumps().
        """
        # Note: This is *EXTREMELY* naive; in reality, you'll need
        # to do much more complex handling to ensure that arbitrary
        # objects -- such as Django model instances or querysets
        # -- can be serialized as JSON.
        return context


class APIView(View, JSONResponseMixin):
    """
    API视图的基类

    :param status: 处理的状态
    :param msg: 返回的处理信息
    """
    status = False
    msg = ''

    def get(self, request, *args, **kwargs):
        """
        查询
        """
        pass

    def post(self, request, *args, **kwargs):
        """
        新增
        """
        pass

    def put(self, request, *args, **kwargs):
        """
        修改
        """
        pass

    def delete(self, request, *args, **kwargs):
        """
        删除
        """
        pass

    def json_response(self, context=''):
        response = {
            'status': self.status,
            'msg': self.msg,
            'result': context
        }
        self.render_to_json_response(response)


class ScrapydView(APIView):

    def post(self, request, *args, **kwargs):
        """
        增加Scrapyd节点
        """
        data = json.loads(request.body)
        try:
            s = dict()
            s['name'] = data['name']
            s['ip'] = data['ip']
            s['port'] = data['port']
            s['comment'] = data.get('comment')
            scrapyd.add_node(s)

            self.status = True
        except:
            self.status = False
            self.msg = '节点信息不完整或其他异常'

        return self.json_response()