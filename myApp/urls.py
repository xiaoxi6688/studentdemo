
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import re_path

# git@github.com:xiaoxi6688/studentdemo.git



from myApp import views
urlpatterns=[
    re_path(r'^$',views.index,name="index"),
    re_path(r'^(\d+)/$',views.detail),
    re_path(r'^grade/$',views.grade),
    re_path(r'^grades/$',views.grades),
    re_path(r'^student/(\d+)$',views.student),
    re_path(r'^grade/(\d+)$',views.gradeStudents),
    re_path(r'^addstu/$',views.addstu),
    re_path(r'^addstu2/$',views.addstu2),
    re_path(r'^stu/(\d+)$',views.stupage),
    re_path(r'^stusearch/$',views.stusearch),
    re_path(r'^attrib/$',views.attrib),
    re_path(r'^get1/$',views.get1),
    re_path(r'^register/$',views.register),
    re_path(r'^showregister/$',views.showregister),
    re_path(r'^cookietest/$',views.cookietest),
    re_path(r'^main/$',views.main),
    re_path(r'^login/$',views.login),
    re_path(r'^showmain/$',views.showmain),
    re_path(r'^quit/$',views.quit),
    re_path(r'^good/(\d+)$',views.good,name="good"),
    re_path(r'^main2/$',views.main2),
    re_path(r'^postfile/$',views.postfile),
    re_path(r'^showpost/$',views.showpost),
    re_path(r'^verifycode/$',views.verifycode),
    re_path(r'^verifycodepost/$',views.verifycodepost),
    re_path(r'^verifycodecheck/$',views.verifycodecheck),
    re_path(r'^upfile/$',views.upfile),
    re_path(r'^savefile/$',views.savefile),
    re_path(r'^ajastu/$',views.ajastu),
    re_path(r'^studentinfo/$',views.studentinfo),
    re_path(r'^edit/$',views.edit),
    re_path(r'^celery/$',views.celery),
]

# urlpatterns+=staticfiles_urlpatterns()