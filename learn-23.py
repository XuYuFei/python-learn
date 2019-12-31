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

# 23.2.5 - 路由（urls）
"""
    Django的URL路由流程：
        - 1、Django查找全局urlpatterns变量（urls.py）;
        - 2、按照先后顺序，对URL逐一匹配urlpatterns每个元素；
        - 3、找到第一个匹配时停止查找，根据匹配结果执行对应的处理函数；
        - 4、如果没有找到匹配或出现异常，Django进行错误处理；
        
    Django支持三种表达格式：
        - 1、精确字符串格式：article/2020/
            - 一个精确URL匹配一个操作函数；
            - 最简单的形式，适合对静态URL的响应；
            - URL字符串不以“/”开头，但要以“/”结尾；
        - 2、Django的转换格式：<类型：变量名>，article/<int:year>/
            - str：匹配除分隔符（/）外的非空字符，默认类型<year>等价于<str:year>;
            - int：匹配0和正整数；
            - slug：匹配字母、数字、横杠、下滑线组成的字符串，str的子集；
            - uuid：匹配格式化的UUID，如234234-23425-234555-102323；
            - path：匹配任何非空字符串，包括路径分隔符，是全集；
        - 3、正则表达式格式：如“article/(?p<year>[0-9]{})/”
            - 借助正则表达式丰富语法表达一类URL;
            - 可以通过 “<>” 提取变量作为处理函数的参数，高级用法；该方法前不能使用path()函数，必须使用re_path()函数；表达的全部是str格式；
            - 使用正则表达式有两种形式：
                - 不能提取参数：如“re_path(articles/([0-9]{4}))/”，表示四位数字，每一位都是0-9的任意数字；
                - 提取参数：命名形式为“(?p<name>pattern)”
                    如“re_path(articles/(?p<year>[0-9]{4}))/”，将正则表达式提取的四位数字，每一个数字都是0-9的任意数字，命名为year;
                    
            注意：功能模块较多时可以在每个模块里建一个urls.py文件，将该模块下URL写在该文件中，然后在全局urls.py中用include实现URL映射分发；
            
            编写URL的三种情况如下：
                - 普通URL：re_path('^index/', view.index)，re_path('^home/', view.Home.as_view())
                - 顺序传参：re_path(r'^detail-(\d+)-(\d+).html/', views.detail)
                - 关键字传参：re_path(r'^detail-(?P<nid>\d+)-(?P<uid>\d+).html/', views.detail)
                
            代码见：
                - learn-23/demo/demo/urls.py
                    ```
                    from django.contrib import admin            # 引入默认后台的模块，其中包括管理界面的urls路由规则
                    from django.urls import path, include       # 引入urls模块中path方法
                    
                    urlpatterns = [
                        path('admin/', admin.site.urls),
                        path('app1/', include('app1.urls'))
                    ]
                    ```

                - learn-23/demo/app1/urls.py
                    ```
                    from app1 import views as app1_views
                    from django.urls import path
                    from django.urls import re_path
                    
                    urlpatterns = [
                        path('articles/2020/', app1_views.special_case_2020),                                               # 精确匹配视频
                        path('articles/<int:year>/', app1_views.year_archive),                                              # 匹配一个整数
                        path('articles/<int:year>/<int:month>/', app1_views.month_archive),                                 # 匹配两个位置的整数
                        path('articles/<int:year>/<int:month>/<slug:slug>/', app1_views.article_detail),                    # 匹配两个位置的整数和一个slug类型的字符串
                        re_path(r'^articles/day/(?P<day>[0-9]{8})/$', app1_views.day_archive),                              # 按照正则表达式匹配8位数字年份
                        re_path(r'^articles/month2/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', app1_views.month2_archive),   # 按照正则表达式匹配4位数字年份和2位数字月份
                        re_path(r'^hello/(?P<year>[0-9]{4})/(?P<slug>[\w-]+)/$', app1_views.hello)                          # 匹配4位年份数字和至少一位slug类型字符串
                    ]
                    ```
                
                - learn-23/demo/app1/views.py
                
                ```
                    from django.shortcuts import render, HttpResponse


                    # Create your views here.
                    
                    def special_case_2020(request):
                        return render(request, '404.html')
                    
                    
                    def year_archive(request, year):
                        context = {'year': year}
                        return render(request, 'year.html', context)
                    
                    
                    def month_archive(request, year, month):
                        context = {
                            'year': year,
                            'month': month
                        }
                        return render(request, 'month.html', context)
                    
                    
                    def article_detail(request, year, month, slug):
                        context = {
                            'year': year,
                            'month': month,
                            'slug': slug
                        }
                        return render(request, 'detail.html', context)
                    
                    
                    def day_archive(request, day):
                        context = {
                            'day': day
                        }
                        return render(request, 'day.html', context)
                    
                    
                    def month2_archive(request, year, month):
                        context = {
                            'year': year,
                            'month': month
                        }
                        return HttpResponse(year)
                    
                    
                    def hello(request, year, slug):
                        return HttpResponse(year + slug)
                ```
"""

# 23.2.6 - 表单（forms）
"""
    新建文件：
        - app1/forms.py
        - app1/templates/name.html
        
    forms.py：
        ```
        from django import forms


        class PersonForm(forms.Form):
            first_name = forms.CharField(label='你的名字', max_length=20)
            last_name = forms.CharField(label='你的姓氏', max_length=20)
        ```
    
    views.py：
        ```
        from django.shortcuts import render
        from django.http import HttpResponse, HttpResponseRedirect
        from app1.forms import PersonForm

        def get_name(request):
            if request.method == 'POST':
                form = PersonForm(request.POST)                                     # 将请求数据填充到PersonForm实例中
                if form.is_valid():
                    first_name = form.cleaned_data['first_name']                    # 使用form.cleaned_data获取请求数据
                    last_name = form.cleaned_data['last_name']
                    return HttpResponse(first_name + '' + last_name)                # 响应拼接后的字符串
                else:
                    return HttpResponseRedirect('/error/')
            else:
                return render(request, 'name.html', {'form': PersonForm()})
        ```
        
    name.html：
        ```
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>forms</title>
        </head>
        <body>
            <form action="/app1/get_name" method="post">{% csrf_token %}
                {{ form }}
                <button type="submit">提交</button>
            </form>
        </body>
        </html>
        ```
        
    urls.py：
        ```
        path('get_name', app1_views.get_name)
        ```
        
    注意：
        - {% csrf_token %}：Django防止跨站请求伪造模板标签
"""

# 23.2.7 - 视图（views）
"""
    基于函数的视图：
        - FBV：Funciton-Based-View
        - 返回一个HttpResponse对象
        - 有一个HttpResponse对象作为参数
        - 代码：
            - app1/views.py：
                ```
                    def current_datetime(request):
                        now = datetime.datetime.now()
                        html = "<html><body>It is now %s.</body></html>" % now
                        return HttpResponse(html)
                ```
            - app1/urls.py：    
                ```
                    app1/urls.py：
                        path('datetime', app1_views.current_datetime)
                ```
            
        - Http404：
            - app1/views.py：
                ```
                    def person_detail(request, pk):
                        try:
                            p = Person.objects.get(pk=pk)
                        except Person.DoesNotExist:
                            raise Http404('Person Does Not Exist')
                        return render(request, 'person_detail.html', {'person': p})
                ```
            - app1/urls.py：
                ```
                    path('person_detail/<int:pk>', app1_views.person_detail)
                ```
            
    基于类的视图实例：
        - CBV：Class-Based-View
        - 所有的类视图都继承自views.View
        - 代码：
            - app1/views.py：
                ```
                    class PersonFormView(View):
                        form_class = PersonForm
                        initial = {'key': 'value'}                                              # 定义表单初始化展示参数
                        template_name = 'name.html'
                    
                        def get(self, request, *args, **kwargs):
                            context = { 'form': self.form_class(initial=self.initial) }
                            return render(request, self.template_name, context)
                    
                        def post(self, request, *args, **kwargs):
                            form = self.form_class(request.POST)
                            if form.is_valid():
                                first_name = form.cleaned_data['first_name']
                                last_name = form.cleaned_data['last_name']
                                return HttpResponse(first_name + '' + last_name)
                            return render(request, self.template_name, {'form': form})
                ```
            - app1/urls.py：
                ```
                    path('get_name1', app1_views.PersonFormView.as_view())
                ```
            
"""

# 23.2.8 - Django模板
"""
    配置文件：settings.py
    配置代码：
        TEMPLATES = [
            {
                'BACKEND': 'django.template.backends.django.DjangoTemplates',
                'DIRS': [],
                'APP_DIRS': True,
                'OPTIONS': {
                    'context_processors': [
                        'django.template.context_processors.debug',
                        'django.template.context_processors.request',
                        'django.contrib.auth.context_processors.auth',
                        'django.contrib.messages.context_processors.messages',
                    ],
                },
            },
        ]
    示例：
        {% extends "base_generic.html" %}
        {% block title %}{{ section.title }}{% endblock %}
        {% block content %}
            <h1>{{ section.title }}</h1>
            
            {% for story in story_list %}
                <h2>
                    {{ story.headline|upper }}
                </h2>
            {% endfor %}
            
        {% endblock %}
    常用过滤器：
        - {{ value|default:'nothing' }}
        - {{ value|length }}：计算返回列表或字符串长度
        - {{ value|filesizeformat }}：将数字转换成可读的文件大小，如10KB,20MB等
        - {{ value|truncatewords:30 }}：获取返回字符串固定长度
        - {{ value|lower }}：字符串转小写
"""


























