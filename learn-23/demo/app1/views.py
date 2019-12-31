from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from app1.forms import PersonForm
import datetime
from app1.models import Person
from django.views import View


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


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


def person_detail(request, pk):
    try:
        p = Person.objects.get(pk=pk)
    except Person.DoesNotExist:
        raise Http404('Person Does Not Exist')
    return render(request, 'person_detail.html', {'person': p})


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


























