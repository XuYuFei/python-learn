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
    re_path(r'^hello/(?P<year>[0-9]{4})/(?P<slug>[\w-]+)/$', app1_views.hello),                         # 匹配4位年份数字和至少一位slug类型字符串
    path('get_name', app1_views.get_name),
    path('get_name1', app1_views.PersonFormView.as_view()),
    path('datetime', app1_views.current_datetime),
    path('person_detail/<int:pk>', app1_views.person_detail)
]