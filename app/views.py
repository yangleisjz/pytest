from django.shortcuts import render
from django.http import HttpResponse
from app.models import BookInfo, PersonInfo
from datetime import date
from django.db.models import F, Sum

def index(request):
    # list = BookInfo.objects.all()[0:2]
    # for book in list:
    #     print(book.btitle, book.bread, book.bcomment, book.bpub_date)
    # list2 = PersonInfo.objects.all()[0:4]
    # for person in list2:
    #     print(person.pname, person.pcomment, person.hbooks.btitle)

    # list = BookInfo.objects.aggregate(Sum('bread'))
    # print(list['bread__sum'])
    # for book in list:
    #     print(book.btitle, book.bread, book.bcomment, book.bpub_date)
    # list = BookInfo.objects.filter(bpub_date__gte=date(1980, 1, 1))
    # for book in list:
    #     print(book.btitle, book.bcomment, book.bpub_date)
    # list2 = PersonInfo.objects.filter(pcomment__contains='字')
    # for person in list2:
    #     print(person.pname, person.pgender, person.pcomment)
    
    # return HttpResponse('<h1>Index</h1>')
    # book = BookInfo.objects.get(id=1)
    # person = book.personinfo_set.all()
    #
    # ret =''
    # for p in person:
    #     ret += str(p.id) + "." + p.pname + "." +p.pcomment +"." +str(p.hbooks_id)
    #     ret += '<br>'

    person1 = PersonInfo.objects.get(id=18)
    p1 = person1.hbooks
    ret2 =p1.btitle + "," + str(p1.bpub_date)

    return HttpResponse(ret2)
    # return render(request, 'app/index.html')

