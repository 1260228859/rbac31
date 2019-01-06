from django.shortcuts import render
from django.views import View
# Create your views here.


class MenuPermissionView(View):

    def get(self, request, *args, **kwargs):
        """
        获取前端所有展示页面
        :param request:
        :param args:
        :param kwargs:
        :return:
        """

        # 获取前端菜单所有的数据

