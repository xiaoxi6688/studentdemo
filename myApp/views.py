import io
import os
import random
import time

from django.contrib.auth import logout
from django.core.paginator import Paginator
from django.db.models import Max, F
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from myApp.models import Grade, Student
from studentdemo import settings


def index(request):
    return render(request, 'myApp/index.html',{"code":"<h1>hello world</h1>"})


def detail(request,num):
    return HttpResponse("detail-%s"%num)


def grade(request):
    gradeList=Grade.objects.all()
    return render(request,'myApp/grades.html',
                  {"grades":gradeList})


def student(request,pageid):
    studentsList=Student.objects.all()
    paginator=Paginator(studentsList,3)
    page=paginator.page(pageid)
    return render(request,'myApp/students.html',
                  {"students":page})


def gradeStudents(request,num):
    grade=Grade.objects.get(pk=num)
    studentsList=grade.student_set.all()
    return render(request,'myApp/students.html',
                  {"students":studentsList})


def addstu(request):
    grade = Grade.objects.get(pk=1)
    stu=Student.createStudent("财富自由",'100',True,"潇洒人生，财务自由",grade)
    stu.save()
    return HttpResponse("添加学生成功")

def addstu2(request):
    grade2 = Grade.objects.get(pk=3)
    stu = Student.stuObject.createStudent("小溪",True,35,"小溪财务自由",False,"2020-11-2","2020-11-2",grade2)
    stu.save()
    return HttpResponse("添加学生成功")


def stupage(request,page):
    page=int(page)
    studentsList = Student.objects.all()[(page-1)*2:page*2]
    return render(request, 'myApp/students.html',
                  {"students": studentsList})


def stusearch(request):
    studentsList=Student.objects.filter(sage__gte=35)
    maxage=Student.objects.aggregate(Max('sage'))
    print(maxage)
    return render(request, 'myApp/students.html',
                  {"students": studentsList})


def grades(request):
    #g=Grade.objects.filter(ggirlnum__gt=F('gboynum'))
    g=Grade.objects.filter(student__scontent__contains='时间')
    print(g)
    return HttpResponse(g)


def attrib(request):
    print(request.path)
    print(request.method)
    print(request.GET)
    print(request.POST)
    print(request.FILES)
    print(request.COOKIES)
    print(request.session)
    return HttpResponse("attributes")


def get1(request):
    a=  request.GET.get('a')
    b = request.GET.get('b')
    c = request.GET.get('c')
    return HttpResponse(a+""+b+""+c)


def register(request):
    name=request.GET.get('name')
    request.session['name'] = name
    gender=request.POST.get('gender')
    request.session['gender'] = gender
    age=request.POST.get('age')
    hobby=request.POST.getlist('hobby')
    print(name)
    print(gender)
    print(age)
    print(hobby)
    #return HttpResponse("注册成功！"+name+gender+age+hobby)
    return HttpResponse("注册成功！")


def showregister(request):
    return render(request,'myApp/register.html')


def cookietest(request):
    resp=HttpResponse()
    cookie=request.COOKIES
    resp.write("<h1>"+cookie["sunck"]+"</h1>")
    #cookie=resp.set_cookie("sunck","good")
    return resp


def main(request):
    username=request.session.get('username',"游客")
    return render(request,'myApp/main.html',{'username':username})


def login(request):
    return render(request,'myApp/login.html')


def showmain(request):
    username=request.POST.get('username')
    request.session['username']=username
    #request.session.set_expiry(10)
    return redirect('/main')


def quit(request):
    #logout(request)
    request.session.clear()
    return redirect('/main')


def good(request,id):
    return render(request, 'myApp/good.html',{"num":id})


def main2(request):
    return render(request, 'myApp/main2.html')


def postfile(request):
    return render(request, 'myApp/postfile.html')


def showpost(request):
    name=request.POST.get('username')
    pwd = request.POST.get('password')
    return render(request, 'myApp/showpost.html',{"username":name,"password":pwd})

from PIL import Image,ImageDraw,ImageFont
def verifycode(request):
    bgcolor=(random.randrange(20,100),random.randrange(20,100),random.randrange(20,100))
    width=100
    height=50
    img=Image.new('RGB',(width,height),bgcolor)
    draw=ImageDraw.Draw(img)
    for i in range(0,100):
        xy=(random.randrange(0,width),random.randrange(0,height))
        fill=(random.randrange(0,255),255,random.randrange(0,255))
        draw.point(xy,fill=fill)
    str='1234567890QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm'
    rand_str=''
    for i in range(0,4):
        rand_str+=str[random.randrange(0,len(str))]
    font=ImageFont.truetype(r'C:\Windows\Fonts\AdobeGothicStd-Bold.otf',40)
    fontcolor1 = (255,random.randrange(0,255),random.randrange(0,255))
    fontcolor2 = (255, random.randrange(0, 255), random.randrange(0, 255))
    fontcolor3 = (255, random.randrange(0, 255), random.randrange(0, 255))
    fontcolor4 = (255, random.randrange(0, 255), random.randrange(0, 255))
    draw.text((5,2),rand_str[0],font=font,fill=fontcolor1)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor2)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor3)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor4)
    del draw
    request.session['verify']=rand_str
    buf=io.BytesIO()
    img.save(buf,'png')
    return HttpResponse(buf.getvalue(),'image/png')


def verifycodepost(request):
    f = request.session.get('flag',True)
    str=''
    if f==False:
        str='请重新输入验证码'
    request.session.clear()
    return render(request, 'myApp/verifycodepost.html',{"flag":str})


def verifycodecheck(request):

    code1=request.POST.get("verifycode").upper()
    code2 = request.session.get("verify").upper()
    if code1==code2:
        return render(request, 'myApp/success.html')
    else:
        request.session['flag']=False
        return redirect('/verifycodepost/')


def upfile(request):
    return render(request, 'myApp/upfile.html')


def savefile(request):
    if request.method=='POST':
        f=request.FILES['file']
        filePath=os.path.join(settings.MDEIA_ROOT,f.name)
        with open(filePath,'wb') as fp:
            for info in f.chunks():
                fp.write(info)
        return HttpResponse("上传成功！")
    else:
        return HttpResponse("上传失败！")


def ajastu(request):
    return render(request, 'myApp/ajastu.html')


def studentinfo(request):
    stus=Student.objects.all()
    list=[]
    for stu in stus:
        list.append([stu.sname,stu.sage])
    return JsonResponse({"data":list})


def edit(request):
    return render(request, 'myApp/edit.html')


def celery(request):
    print("sun is the entry")
    time.sleep(8)
    print("sun is the entry")
    return render(request, 'myApp/celery.html')