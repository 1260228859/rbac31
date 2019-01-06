from django.db import models
from enum import Enum
from rbacnew.models.user import User
from rbacnew.models.role import Role


class UserGroup(models.Model):
    """
    用户组表
    """
    usergroup_id = models.IntegerField(verbose_name='用户组id', unique=True)
    last_user_group_id = models.ForeignKey('self', verbose_name='上级用户组id', null=True, blank=True)


