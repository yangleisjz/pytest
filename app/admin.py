from django.contrib import admin
from app.models import BookInfo, PersonInfo

class BookinfoaAdmin(admin.ModelAdmin):
    list_display = ['id', 'btitle', 'bpub_date','bcomment', 'isDelete']

class PersonInfoAdmin(admin.ModelAdmin):
    list_display = ['pname', 'pgender', 'isDelete', 'pcomment']


#将模型类添加到后台页面中
#默认表中的数据以对象的形式显示
#可以定义管理类来设置以字段方式显示
admin.site.register(BookInfo, BookinfoaAdmin) #  (BookInfo, BookinfoaAdmin)关联两个参数 类
admin.site.register(PersonInfo, PersonInfoAdmin)