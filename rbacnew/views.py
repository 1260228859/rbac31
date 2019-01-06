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

    def post(self, request, *args, **kwargs):
        """
        添加菜单添加用户权限 三张表存储
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        # 获取权限id
        menu_sort_id = self.request.POST.get('sort_id')
        role_id = self.request.POST.get('role_id')
        menu_id = Menu.sort_id_change_menu_id(menu_sort_id)

        # 添加到数据中间表
        obj = Menu2Permission.objects.create(role_id_id=role_id, menu_id_id=menu_id)
        if not obj:
            return {'msg': '添加失败'}

        return {'msg': '添加成功'}
