from django.db import models
from enum import Enum
from django.contrib.auth.models import AbstractUser
# Create your models here.
# todo: 代码调整语句模式 废弃穷举法(url拼接)采用分层过滤具体需要研究下淘宝的实现原理i
# todo： 将url转换为类名或者model名称   以url为组判断
# TODO: 在代码级别再次封装request.user

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


class RecourseType(Enum):
    """
    资源权限
    """
    API = 1
    MENU = 2
    ICON = 3
    FILE = 4

    @classmethod
    def choices(cls):
        return (
            (RecourseType.API.value, "接口资源"),
            (RecourseType.MENU.value, "菜单资源"),
            (RecourseType.ICON.value, "标签资源"),
            (RecourseType.FILE.value, "文件资源")
        )

class User(AbstractUser):
    """
    User INFO
    """
    user_model = models.CharField(choices=UserTypeModel.choices(), verbose_name='用户类型', default=0)


    def get_user_obj(self):
        try:
            return getattr(User,self.user_model)
        except Exception as e:
            raise Exception
        finally:
            pass  # TODO: 日志记录

class Admin(User):
    pass

class Customer(User):
    pass

class Group(models.Model):
    group_name = models.CharField(max_length=128, verbose_name='组名')

class Role(models.Model):
    name = models.CharField(max_length=128, verbose_name='角色名称')
    last_name = models.

class Permission(models.Model): # 角色拥有的资源类型
    resouce_type = models.IntegerField(choices=RecourseType.choices(), verbose_name='资源类型')

class Menu(models.Model):
    title = models.CharField(max_length=128, verbose_name='标题页')

class Api(models.Model):
    url = models.CharField(max_length=128, verbose_name='根路径')

class Recourse(models.Model):
    pass