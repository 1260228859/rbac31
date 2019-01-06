from django.db import models
from enum import Enum
from django.contrib.auth.models import AbstractUser
from rbacnew.models.role import Role
from rbacnew.models.foreignkey_table import *  # 循环引用问题


class UserTypeModel(Enum):
    """
    用户模型表
    """
    NOTGROUPUSER = 'NotGroup'
    ADMIN = 'Admin'
    CUSTOMER = 'Customer'

    @classmethod
    def choices(cls):
        return (
            (UserTypeModel.NOTGROUPUSER.value, "游客表"),
            (UserTypeModel.ADMIN.value, "管理员表"),
            (UserTypeModel.CUSTOMER.value, "客户表")
        )


class User(AbstractUser):
    """
    User INFO

        用户 -- 角色 多对多
    """
    user_id = models.IntegerField(verbose_name='用户id')
    user_model = models.CharField(choices=UserTypeModel.choices(), max_length=128, verbose_name='用户类型', default=0)

    def get_user_obj(self):
        try:
            return getattr(User, self.user_model)  # Todo: 如何获取到类名
        except Exception as e:
            raise Exception
        finally:
            pass  # TODO: 日志记录

    def get_all_usergroup_role(self):
        """
        获取用户所有的用户组
        :return:
        """
        # 中间表中获取所有的用户组id列表
        usergroup_id_list = User2Group.objects.filter(user_id_id=self.user_id).value_list('usergroup_id')
        return UserGroup2Role.objects.filter(usergroup_id_id__in=usergroup_id_list).value_list('role_id')

    def get_all_user_role(self):
        """
        获取当前用户所有的角色
        :return:
        """
        return User2Role.objects.filter(user_id_id=self.user_id).value_list('role_id')

    def get_all_role_id_list(self):
        """
        获取所有的用户角色(用户角色+用户组角色)
        :return:
        """
        # 获取用户所属用户组角色列表
        usergroup_list = self.get_all_usergroup()
        # 获取用户所属角色列表
        user_role = self.get_all_user_role()

        return list(set(user_role.extend(usergroup_list)))

    def get_all_permissions_id(self):
        """
            获取所有的权限id  有待商榷 计划采用相位值进行转换
        :return:
        """
        pass

    def get_all_permissions_mask(self):
        """
        获取所有的权限mask值
        :return:
        """
        pass

    def get_all_recourse(self):
        """
        获取当前用户所有的资源   该用户前端拥有的相关资源
        :return:
        """
        # 获取所有的权限列表
        permission_id_list = Role2Permission.objects.filter(role_id_id__in=self.get_all_role_id_list()).values_list(
            'permission_id')

        # 获取所有的权限类型分别对应的表名 方便后续进行反射使用  他的权限对应的几个表 这一步可以不必使用
        # permission_type_list = Permission.objects.filter(permission_id__in=permission_id_list).values(
        #     'permission_type').annotate()

        menu_id_list = Menu2Permission.objects.filter(permission_id_id__in=permission_id_list).values_list('menu_id')

        return menu_id_list