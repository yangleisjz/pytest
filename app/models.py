from django.db import models

# 定义图书模型类BookInfo
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20, db_column='title')
    bpub_date = models.DateField()            #发布日期
    bread = models.IntegerField(default=0)    #阅读量
    bcomment = models.IntegerField(default=0) #评论量
    isDelete = models.BooleanField(default=False) #逻辑删除

# 定义人物模型类PersonInfo （pname pgender isDelete pcomment）
class PersonInfo(models.Model):
    pname = models.CharField(max_length=20)
    pgender = models.BooleanField(default=False)
    isDelete = models.BooleanField(default=False)
    pcomment = models.CharField(max_length=200, blank=False, null=True )
    hbooks = models.ForeignKey('BookInfo', on_delete=models.CASCADE)

class TypeInfo(models.Model):
    tname = models.CharField(max_length=20)  #新闻类别

class NewInfo(models.Model):
    ntitle = models.CharField(max_length=20)
    ncontent = models.CharField(max_length=100)
    npub_date = models.DateTimeField(auto_now_add=True)

    typeinfo = models.ManyToManyField('TypeInfo')

