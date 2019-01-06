from django.db import models
from enum import Enum
from django.contrib.auth.models import AbstractUser
from rbacnew.models.role import Role
from rbacnew.models.foreignkey_table import *  # 循环引用问题


class PermissionType(Enum):
    """
    权限类型
    """
    MENU = 1
    API = 2
    ICON = 3
    FILE = 4

    @classmethod
    def choices(cls):
        return (
            (PermissionType.MENU.value, "菜单表"),
            (PermissionType.API.value, "api接口表"),
            (PermissionType.ICON.value, "标签表"),
            (PermissionType.FILE.value, "文件表")
        )


class Permission(models.Model):
    """
    权限总表
    """
    permission_id = models.IntegerField(verbose_name='权限id')
    permission_type = models.IntegerField(choices=PermissionType.choices(), verbose_name='权限类型')