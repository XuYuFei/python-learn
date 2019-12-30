""" 22 - Flask Web 框架的使用 """
# 22.1 - Web框架简介
# 22.1.1 - 什么是Web框架
"""
    Web框架是用来简化Web开发的软件框架。
    典型的框架提供了如下常用功能：
        - 管理路由
        - 访问数据库
        - 管理会话和Cookies
        - 创建模板来显示HTML
        - 促进代码的重用
"""

# 22.1.2 - 常用的Web框架
"""
    WSGI：服务器网关接口，是Web服务器和Web应用程序或框架之间的一种简单而通用的接口。
          只要遵循WSGI接口规范，就可以自主开发Web框架。
    主流Web框架：
        - Flask：轻量级Web应用框架；
        - Django
        - Bottle
        - Tornado
"""

# 22.2 - Flask框架的使用
"""
    Flask依赖两个外部库：Werkzeug、Jinja2
        - Werkzeug：是一个WSGI工具集
        - Jinja2：负责渲染模板
    安装Flask前，需要安装这两个外部库。而最简单的方式就是使用Virtualenv创建虚拟环境。
"""

# 22.2.1 - 安装虚拟环境
"""
    安装Flask最便捷的方式就是使用虚拟环境。Virtualenv为每个不同项目提供一份Python安装。
    它并没有真正安装多个Python副本，但是它确实提供了一种巧妙的方式来让各个项目环境保持独立。
    
    1、安装Virtualenv
        pip install virtualenv
        virtualenv --version
    2、创建虚拟环境
        使用Virtual命令在当前文件中创建Python虚拟环境。虚拟环境名，一般被命名为venv。
        virtualenv venv
    3、激活虚拟环境
        在使用虚拟环境之前，需要先将其“激活”。
        激活命令：venv\Scripts\activate
        激活失败参考：https://www.jianshu.com/p/31ea9cce5e47
"""

# 22.2.2 - 安装Flask
"""
    安装命令：pip install flask
    安装完后，查看所有安装包：pip list --format columns
    ****注意：安装时在虚拟环境中安装
"""

# 22.2.3 - 第一个Flask程序
# 见：learn-12/hello.py

# 22.2.4 - 开启调试模式
"""
    开启调试模式后，服务器会在代码修改后自动重新载入，并在发生错误时提供一个有用的调试器。
    两种方法：
        - 1、在应用对象上设置
            app.debug = True
            app.run()
        - 2、作为run方法一个参数传入
            app.run(debug = True)
"""

# 22.2.5 - 路由
"""
    处理URL和函数之间关系的程序称为路由。
    在Flask程序中定义路由的最佳便方式，是使用程序实例提供的app.route修饰器，把修饰器的函数注册为路由。
    例：
        @app.route('/')
        def hello_world():
            return 'Hello World!'
    说明：
        修饰器是Python语言的标准特性，可以使用不同的方式修改函数的行为。
        管用方法是使用修饰器把函数注册为事件的处理程序。
        也可以构造动态URL，在一个函数上附着多个规则。
        
    1、变量规则
        给URL添加变量部分，可以将特殊字段标记为<variable_name>，可以用<converter:variable_name>指定一个可选的转换器
        
        例：
            @app.route('/post/<int:post_id>')
            def show_post(post_id):
                return 'Post %d ' % post_id
        转换器：<converter:variable_name>
            - int：接收整数
            - float：接收浮点数
            - path：和默认的相似，也可接收斜线
            
    2、构造URL
        给指定的函数构造URL：url_for(endpoint, values)
        
        例：
            @app.route('/url/')
            def get_url():
                return url_for('show_post', post_id=2)
    3、HTTP方法
        默认情况下，路由只回应GET请求，可以通过route()装饰器传递methods参数改变这个行为。
        例：@app.route('/login', methods = ['GET', 'POST'])
        常见方法：
            - GET
            - HEAD
            - POST
            - PUT
            - DELETE
            - OPTIONS
"""

# 22.2.6 - 静态文件
"""
    创建static/style.css文件
    给静态文件生成URL，使用特殊的‘static’端点名：
        - url_for('static', filename = 'style.css')
"""

# 22.2.7 - 模板
"""
    渲染：使用真实值替换变量，再返回最终得到的响应字符串的过程。
    Flask模板引擎：Jinja2
    
    1、渲染模板
        见：render.py
        渲染函数：render_template(template_name_or_list, **context)
    
    2、变量
        Jinja2能识别所有类型变量
        例：
            - 从字典冲取一个值：{{ dict['key'] }}
            - 从列表中取一个值：{{ list[3] }} 
            - 从列表中取一个带索引的值：{{ list[var] }}
            - 从对象方法中取一个值：{{ obj.somemethod() }}
            - 使用过滤器修改变量：{{ name|capitalize }}
        常用过滤器：
            - safe：渲染时不转义
            - capitalize：首字母转大写，其他字母转小写
            - lower：把值转换成小写形式
            - upper：把值转换成大写形式
            - title：把值中每个单词的首字母都转换成大写
            - trim：去除首尾空格
            - striptags：渲染之前把值中所有的HTML标签都删掉
            
    3、控制结构
        条件控制语句：
            {% if user %}
                Hello, {{ user }}!
            {% else %}
                Hello, Stranger!
            {% endif %}
        循环语句：
            {% for item in list %}
                {{ item }}
            {% endfor %}
            
        宏【宏类似于Python代码中的函数】：
            {% macro render_comment(comment) %}
                {{ comment }}
            {% endmacro %}
        引入宏文件：
            {% import 'macros.html' as macros %}
        多出使用重复文件：
            {% include 'common.html' %}
        继承模板：
            例：base.html
            <html>
                <head>
                    {% block head %}
                        <title>{% block title %}{% endblock %}</title>
                    {% endblock %}
                </head>
                <body>
                    {% block body %}
                    {% endblock %}
                </body>
            </html>
        衍生模板：
            {% extends "base.html" %}
                {% block title %}Index{% endblock %}
                {% block head %}
                    {{ super() }}
                    <style></style>
                {% endblock %}
                
                {% block body %}
                    <h1>Hello World!</h1>
                {% endblock %}
"""

























