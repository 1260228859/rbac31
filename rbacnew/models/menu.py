from django.db import models
from enum import Enum
from django.contrib.auth.models import AbstractUser
from rbacnew.models.role import Role
from rbacnew.models.foreignkey_table import *  # 循环引用问题


class Menu(models.Model):
    """
    菜单表
    """
    name = models.CharField(max_length=128, verbose_name='前端菜单名称')
    menu_id = models.IntegerField(verbose_name='前端菜单id值')
    menu_num = models.CharField(max_length=128, verbose_name='前端菜单编码')  # 1-1  1-0 2-9-1



