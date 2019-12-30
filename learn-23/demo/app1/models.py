from django.db import models


# Create your models here.
# class Person(models.Model):
#     """
#     编写Person模型类，数据模型应该继承于models.Model或其子类
#     """
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)

class CreateUpdate(models.Model):                           # 创建抽象数据模型
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:                                             # 元数据，除了字段以外的所有属性
        abstract = True                                     # 设置model为抽象类，指定该表不应该在数据库中创建


class Person(CreateUpdate):                                 # 继承CreateUpdate基类
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


class Order(CreateUpdate):
    order_id = models.CharField(max_length=30, db_index=True)
    order_desc = models.CharField(max_length=120)