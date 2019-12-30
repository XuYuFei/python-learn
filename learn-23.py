# *_* code: UTF-8 *_*
# author:   Beiyu
# datetime: 2019-12-30 8:34
# filename: learn-23.PY
# tool:     PyCharm

# 23 - Django Web框架的使用
"""
    Django是基于Python的重量级开源Web框架。
    特点：
        - 拥有高度定制的ORM
        - 大量API
        - 简单灵活的视图编写
        - 优雅的URL
        - 适于快速开发的模板
        - 强大的管理后台
    谁在用：
        - Instagram
        - FireFox
        - 国家地理杂志
"""

# 23.1 - 安装Django Web框架
"""
    1、使用pip安装Django
        安装命令：pip install django==2.0
        
    2、使用virtualenv安装Django
        同22章安装virtualenv步骤
        安装django：pip install django
"""

# 23.2 - Django框架的使用
"""
    创建项目步骤：
        - 1、新建项目目录：learn-23
        - 2、在项目目录下创建虚拟环境：virtualenv venv
        - 3、激活虚拟环境：venv\Scripts\activate
        - 4、使用“django-admin”创建一个项目：django-admin startproject demo
        - 5、运行项目：python manage.py runserver
        - 6、生成数据表，并创建一个账户名和密码：
            - python manage.py migrate              # 执行数据库迁移并生成数据表
            - python manage.py createsuperuser      # 创建用户
        - 7、访问后台：http://127.0.0.1:8000/admin
        
    Django项目文件说明：
        - manage.py：Django程序执行的入口
        - db.sqlite3：SQLite数据库文件
        - templates：模板文件夹
        - demo：和项目同名的配置文件夹
        - settings.py：Django总配置文件，可以配置App、数据库、中间件、模板等
        - urls.py：默认的路由配置文件
        - wsgi.py：Django实现的WSGI接口的文件，用来处理web请求
"""

# 23.2.2 - 创建App
"""
    在Django项目中，推荐使用App来完成不同模块的任务；
    创建应用程序：python manage.py startapp app1
    
    app1目录文件及说明：
        - migrations：执行数据库迁移生成的脚本；
        - admin.py：配置Django管理后台的文件
        - apps.py：单独配置添加的每个App的文件
        - models.py：创建数据库数据模型对象的文件
        - tests.py：用来编写测试脚本的文件
        - views.py：用来编写视图控制器的文件
    
    将创建的App添加到settings配置文件中，然后将其激活
        INSTALLED_APPS = [
            ......
            'app1'          # 刚刚新建的app1
        ]
"""

# 23.2.3 - 数据模型（models）
"""
    代码见：models.py
    
    1、在App中添加数据模型
    --------------------------------------------
    from django.db import models


    # Create your models here.
    class Person(models.Model):
        '''
        编写Person模型类，数据模型应该继承于models.Model或其子类
        '''
        first_name = models.CharField(max_length=30)
        last_name = models.CharField(max_length=30)
    ---------------------------------------------
        该代码会创建如下表：
        Create TABLE myapp_person (
            "id" serial NOT NULL PRIMARY KEY,
            "first_name" varcahr(30) NOT NULL,
            "last_name" varchar(30) NOT NULL
        );
    
    django.db.models常见字段类型：
        - AutoField
        - BinaryField
        - BooleanField
        - NullBooleanField
        - CharField
        - TextField
        - DateField
        - DateTimeField
        - EmailField
        - FileField
        - ImageField
        - IntegerField
        - FloatField
        - SlugField
        - UUIDField
        - ForeignField
        - ManyToManyField
        - OneToOneField
    
    2、执行数据库迁移
        - 1、将SQLite改为MySQL数据库，修改settings.py配置：
            # DATABASES = {
            #     'default': {
            #         'ENGINE': 'django.db.backends.sqlite3',
            #         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            #     }
            # }
            
            DATABASES = {
                'default': {
                    'ENGINE': 'django.db.backends.mysql',
                    'NAME': 'django_demo1',
                    'USER': 'root',
                    'PASSWORD': ''
                }
            }
        - 2、创建数据库，在终端连接数据库：
            命令：mysql -u root -p
            可能遇到问题：将mysql路径配置到path中即可
        - 3、输入密码，创建数据库
            命令：create database django_demo1 default character set utf8;
        - 4、安装数据库驱动pymysql
            命令：pip install pymysql
            最好：pip install pymysql -i https://mirrors.aliyun.com/pypi/simple/
        - 5、在demo\demo\__init__.py中，添加如下代码：
            import pymysql
            pymysql.install_asMySQLdb()
        - 6、执行以下命令，创建数据表
            python manage.py makemigrations     # 生成迁移文件
            python manage.py migrate            # 迁移数据库，创建新表
        - 7、Django会默认按照“app名称 + 下滑线 + 模型类名称”形式创建数据表
            例：app1_person  app1_order
            
    3、了解Django数据API
        以下都在在Django交互式命令行中执行：
            - 启用交汇命令行：python manage.py shell
            - 导入数据模型命令：from app1.models import Person, Order
            - 创建数据：
                - 方法1：p = Person.objects.create(first_name='hugo', last_name='zhang')
                - 方法2：
                        p = Person(first_name='hugo', last_name='张')
                        p.save()
            - 查询数据：
                - 查询所有数据：Person.objects.all()
                - 查询单个数据：Person.objects.get(first_name='hugo')
                - 查询指定条件数据：
                    - Person.objects.filter(first_name__exact='hugo')                                           # 指定first_name字段值必须为hugo
                    - Person.objects.filter(last_name__iexact='zhang')                                          # 不区分大小写查找值必须为zhang的，如zhanG
                    - Person.objects.filter(id__gt=1)                                                           # 查找所有id值大于1的
                    - Person.objects.filter(id__lt=100)                                                         # 查找所有id值小于100的
                    - Person.objects.exclude(created_at__gt=datetime.datetime.now(tz=datetime.timezone.utc))    # 排除
                    - Person.objects.filter(first_name__contains='h').order_by('id')                            # 包含'h'的
                    - Person.objects.filter(first_name__icontains='h')                                          # 不包含'h'的
            - 修改数据
                p = Person.objects.get(first_name='hugo')
                p.first_name = 'john'
                p.last_name = 'wang'
                p.save()
            - 存在则修改，不存在创建
                p, is_created = Person.objects.get_or_create(
                    first_name = 'hugo',
                    defaults = {'last_name': 'wang'}
                )
            - 删除数据
                Person.objects.get(id=1).delete()
                (1,('app1.Person':1))
"""

# 23.2.4 - 管理后台
"""
    代码见：app1/admin.py
    -----------------------------------------------------------------------------------------------------
    from django.contrib import admin                        # 引入admin模块

    # Register your models here.
    from app1.models import Person, Order                   # 引入数据模型类
    
    
    class PersonAdmin(admin.ModelAdmin):
        '''
        创建PersonAdmin类，继承于admin.ModelAdmin
        '''
        list_display = ('first_name', 'last_name')          # 配置展示列表，在Person板块下的列表展示
        list_filter = ('first_name', 'last_name')           # 配置过滤查询字段，在Person板块下右侧过滤框
        search_fields = ('first_name',)                     # 配置可以搜索的字段，在Person板块下右侧搜索框
        readonly_fields = ('created_at', 'updated_at')      # 配置只读字段展示，设置后该字段不可编辑
    
    
    admin.site.register(Person, PersonAdmin)                # 绑定Person模型到PersonAdmin管理后台
    ----------------------------------------------------------------------------------------------------
"""































