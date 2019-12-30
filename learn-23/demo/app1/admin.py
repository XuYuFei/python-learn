from django.contrib import admin                        # 引入admin模块

# Register your models here.
from app1.models import Person, Order                   # 引入数据模型类


class PersonAdmin(admin.ModelAdmin):
    """
    创建PersonAdmin类，继承于admin.ModelAdmin
    """
    list_display = ('first_name', 'last_name')          # 配置展示列表，在Person板块下的列表展示
    list_filter = ('first_name', 'last_name')           # 配置过滤查询字段，在Person板块下右侧过滤框
    search_fields = ('first_name',)                     # 配置可以搜索的字段，在Person板块下右侧搜索框
    readonly_fields = ('created_at', 'updated_at')      # 配置只读字段展示，设置后该字段不可编辑


admin.site.register(Person, PersonAdmin)                # 绑定Person模型到PersonAdmin管理后台
