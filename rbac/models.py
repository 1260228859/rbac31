from django.db import models
from enum import Enum
from django.contrib.auth.models import AbstractUser
# Create your models here.
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

