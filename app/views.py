from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse


def insert_topic(request):
    TMFO=TopicModelForm()
    d={'TMFO':TMFO}
    if request.method=='POST':
        TMFD=TopicModelForm(request.POST)
        if TMFD.is_valid():
            TMFD.save()
        else:
            return HttpResponse('in_valid')
        return HttpResponse('topic_name is created')
    return render(request,'insert_topic.html',d)


def insert_webpage(request):
    WMFO=WebpageModelForm()
    w={'WMFO':WMFO}
    if request.method=='POST':
        WMFD=WebpageModelForm(request.POST)
        if WMFD.is_valid():
            WMFD.save()
        else:
            return HttpResponse('in_valid')
        return HttpResponse('webpage is created')
    return render(request,'insert_webpage.html',w)


def insert_access(request):
    ARMFO=AccessRecordModelForm()
    A={'ARMFO':ARMFO}
    if request.method=='POST':
        ARMFD=AccessRecordModelForm(request.POST)
        if ARMFD.is_valid():
            ARMFD.save()
        else:
            return HttpResponse('in_valid')
        return HttpResponse('Accessrecord is created')

    return render(request,'insert_AccessRecord.html',A)