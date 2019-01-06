from django.db import models
from enum import Enum
from django.contrib.auth.models import AbstractUser
from rbacnew.models.role import Role
from rbacnew.models.foreignkey_table import *  # 循环引用问题


class Menu(models.Model):
    """
    菜单表
        sort_id 用来做排序
        取出所有 返回给前端

        1、返回用户配置界面是先进行一次整体查询  在进行现有权限进行查询  最后得出对应表
        2、扁平化的表如何转变为嵌套格式 # todo: 等待商榷
    """
    name = models.CharField(max_length=128, verbose_name='前端菜单名称')
    menu_id = models.IntegerField(verbose_name='前端菜单id值')
    sort_id = models.CharField(max_length=128, verbose_name='前端菜单排序编码')  # 1-1  1-0 2-9-1

    @classmethod
    def get_all_sort_menu(cls):
        """
        获取所有有序的菜单
        :return:
        """
        menu_all = cls.objects.all().values('name', 'sort_id')
        sorted(menu_all, key=lambda x: x['sort_id'])
        return {i['sort_id']: i['name'] for i in menu_all}
