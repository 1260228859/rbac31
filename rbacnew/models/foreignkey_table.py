from django.db import models
from enum import Enum

from rbacnew.models.user import User
from rbacnew.models.role import Role
from rbacnew.models.usergroup import UserGroup
from rbacnew.models.permission import Permission
from rbacnew.models.menu import Menu


class User2Role(models.Model):
    """
    用户-角色关联表
    """
    user_id = models.ForeignKey(User, to_field='user_id', related_name='user_id', verbose_name='用户id')
    role_id = models.ForeignKey(Role, to_field='role_id', related_name='role_id', verbose_name='角色id')
    user_role_id = models.IntegerField(verbose_name='用户角色id', default=id)
    # todo: 数据维度拓展 关联或则对应相关业务维度  比如可以添加地区、产品


class User2Group(models.Model):
    """
    用户-用户组关联表
    """
    user_id = models.ForeignKey(User, to_field='user_id', verbose_name='用户关联id')
    user_group_id = models.ForeignKey(UserGroup, to_field='user_id', verbose_name='用户组关联id')


class UserGroup2Role(models.Model):
    """
    用户组-角色关联表
    """
    usergroup_id = models.ForeignKey(UserGroup, to_field='usergroup_id', verbose_name='用户组关联id')
    role_id = models.ForeignKey(Role, to_field='role_id', verbose_name='用户角色关联id')

#
# class Role2Menu(models.Model):
#     """
#     角色菜单关联表
#     """
#     role_id = models.ForeignKey(Role, to_field='role_id', verbose_name='关联角色id')
#     menu_id = models.ForeignKey(Menu, to_field='menu_id', verbose_name='关联菜单id')


class Menu2Permission(models.Model):
    """
    菜单-权限关联表
    """
    permission_id = models.ForeignKey(Permission, to_field='permission_id', verbose_name='关联权限id')
    menu_id = models.ForeignKey(Menu, to_field='menu_id', verbose_name='关联菜单id')


class Role2Permission(models.Model):
    """
    角色-权限关联表
    """
    role_id = models.ForeignKey(Role, to_field='role_id', verbose_name='关联角色id')
    permission_id = models.ForeignKey(Permission, to_field='permission_id', verbose_name='权限名称关联表')


# 用户登陆
# 获取用户的pk值
#   获取用户权限  取中间表中获取用户所有的用户组列表
