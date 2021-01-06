from django.contrib import admin

# Register your models here.
from .models import Grade, Student, Text


class StudentsInfo(admin.TabularInline):
    model=Student
    extra=2
class GradeAdmin(admin.ModelAdmin):
    inlines=[StudentsInfo]
    list_display= ['pk','gname','gdate','ggirlnum','gboynum','isDel']
    list_filter = ['gname']
    search_fields=['gname']
    list_per_page=5
    #fields=['isDel','gname','gdate','ggirlnum','gboynum']
    fieldsets=[("base",{"fields":['isDel','gname','gdate']}),
        ("num", {"fields": ['ggirlnum', 'gboynum']})]
admin.site.register(Grade,GradeAdmin)
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    def gender(self):
        if self.sgender:
            return "男"
        else:
            return "女"
    gender.short_description = "性别"
    list_display = ['pk','sname','sage',gender,
                    'scontent','sgrade','isDel']
    list_per_page = 3
    actions_on_bottom = True
    actions_on_top = False
#admin.site.register(Student,StudentAdmin)
admin.site.register(Text)
