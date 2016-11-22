from django.shortcuts import render
from django.shortcuts import HttpResponse
from myapp import models

# Create your views here.

user_list = [
    {'name':'Jack','age':'16'},
    {'name':'Tom','age':'20'},
    {'name':'Alex','age':'26'}
]



def index(request):
    # request.POST
    # request.GET
    #return HttpResponse('hello world!')
    if request.method == 'POST':
        name = request.POST.get('name',None)
        age = request.POST.get('age',None)
        #print(name,age)
        #temp = {'name':name,'age':age}
        #user_list.append(temp)
        # 添加数据到数据库
        models.UserInfo.objects.create(name=name,age=age)
    # 从数据库中读取所有数据
    user_list = models.UserInfo.objects.all()
    return render(request,'index.html',{'data':user_list})

