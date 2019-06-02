from django.shortcuts import render
from .models import Upload
import random

# Create your views here.
def main(request):
    return render(request, 'word/main.html')

def upload(request):
    return render(request, 'word/upload.html')

def upload_DB(request):
    word = request.GET.get('word')
    mean = request.GET.get('mean')
    # upload = Upload(
    #     word = word,
    #     mean = mean
    # )    
    # upload.save()
    new_upload = Upload.objects.create(word = word, mean = mean)

    return render(request,'word/upload.html')

def word(request):
    word = request.GET.get('word')
    mean = request.GET.get('mean')

    dic = Upload.objects.all()

    dic ={'dic': dic}
    return render(request,'word/word.html', dic)

def test(reqeust):
    cnt = Upload.objects.count()
    pk = random.randrange(4, cnt+4)
    word = Upload.objects.get(pk = pk)
    context ={'word' : word, 'pk' : pk}
    return render(reqeust, 'word/test.html', context)

def check(request):
    pk = request.GET.get('pk')
    word = Upload.objects.get(pk = pk)
    sol = request.GET.get('sol')

    if word.mean == sol:
        message ='정답'
    else: 
        message ='오답'

    context={'message': message}

    return render(request, 'word/check.html',context)
