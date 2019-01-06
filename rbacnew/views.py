from django.shortcuts import render
from django.views import View
from rbacnew.models.menu import Menu
from rbacnew.models.foreignkey_table import *

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
        return Menu.get_all_sort_menu()

