from django.db import models

# Create your models here.
from tinymce.models import HTMLField


class Grade(models.Model):
    #gid=models.AutoField(primary_key=True)
    gname   =models.CharField(max_length=20)
    gdate   =models.DateTimeField()
    ggirlnum=models.IntegerField()
    gboynum =models.IntegerField()
    isDel   =models.BooleanField(default=False)
    def __str__(self):
        return "%s"%(self.gname)
    class Meta:
        db_table="grades"
        ordering = ['-id']
class StudentManager(models.Manager):
    def createStudent(self,name,gender,age,content,isD,last,create,grade):
        stu=self.model()
        stu.sname=name
        stu.sgender = gender
        stu.sage=age
        stu.scontent=content
        stu.isDel = isD
        stu.lastTime=last
        stu.createTime=create
        stu.sgrade = grade
        return stu
    def get_queryset(self):
        return super(StudentManager,self).get_queryset().filter(isDel=False)
class Student(models.Model):
    stuObject=StudentManager
    sname=models.CharField(max_length=20)
    sgender=models.BooleanField(default=True)
    sage=models.IntegerField(db_column="age")
    scontent=models.CharField(max_length=20)
    isDel = models.BooleanField(default=False)
    lastTime=models.DateTimeField(auto_now=True)
    createTime=models.DateTimeField(auto_now_add=True)
    sgrade=models.ForeignKey(Grade,on_delete=models.CASCADE,default='')
    class Meta:
        db_table="students"
        ordering=['id']
    def __str__(self):
        return self.sname
    @classmethod
    def createStudent(cls,name,age,gender,content,grade):
        stu=cls(sname=name,sage=age,sgender=gender,scontent=content,
                    sgrade=grade)
        return stu
class Text(models.Model):
    str=HTMLField()