from django.db import models
from enum import Enum


class RoleType(Enum):
    """
    角色类型
    """
    pass


class Role(models.Model):
    """
    角色类
        角色id自行新建字段，使用默认id会增加后续迁移的难度
    """

    name = models.CharField(max_length=128, verbose_name='角色名称')
    role_id = models.IntegerField(unique=True, verbose_name='角色唯一id')
    role_type = models.IntegerField(choices=RoleType.choices(), verbose_name='角色类型', default=0)
    last_id = models.ForeignKey('self', to_field=role_id, verbose_name='上级角色id', null=True, blank=True)

