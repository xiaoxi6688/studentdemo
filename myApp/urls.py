from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from myApp import views
urlpatterns=[
    url(r'^$',views.index,name="index"),
    url(r'^(\d+)/$',views.detail),
    url(r'^grade/$',views.grade),
    url(r'^grades/$',views.grades),
    url(r'^student/(\d+)$',views.student),
    url(r'^grade/(\d+)$',views.gradeStudents),
    url(r'^addstu/$',views.addstu),
    url(r'^addstu2/$',views.addstu2),
    url(r'^stu/(\d+)$',views.stupage),
    url(r'^stusearch/$',views.stusearch),
    url(r'^attrib/$',views.attrib),
    url(r'^get1/$',views.get1),
    url(r'^register/$',views.register),
    url(r'^showregister/$',views.showregister),
    url(r'^cookietest/$',views.cookietest),
    url(r'^main/$',views.main),
    url(r'^login/$',views.login),
    url(r'^showmain/$',views.showmain),
    url(r'^quit/$',views.quit),
    url(r'^good/(\d+)$',views.good,name="good"),
    url(r'^main2/$',views.main2),
    url(r'^postfile/$',views.postfile),
    url(r'^showpost/$',views.showpost),
    url(r'^verifycode/$',views.verifycode),
    url(r'^verifycodepost/$',views.verifycodepost),
    url(r'^verifycodecheck/$',views.verifycodecheck),
    url(r'^upfile/$',views.upfile),
    url(r'^savefile/$',views.savefile),
    url(r'^ajastu/$',views.ajastu),
    url(r'^studentinfo/$',views.studentinfo),
    url(r'^edit/$',views.edit),
    url(r'^celery/$',views.celery),
]

# urlpatterns+=staticfiles_urlpatterns()