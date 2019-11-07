#from django.http import HttpResponse
from django.shortcuts import render


def home(request):#request用户发出的请求
    return render(request,  'home.html') #render函数需要参数


def count(request):
    user_text=request.GET['text']
    total_count=len(user_text)

    word_dict={}

    for word in user_text:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1
    sorted_dict = sorted(word_dict.items(),key=lambda w:w[1], reverse=True)
    #item将字典里面的键（key ）和值（value），变成了[键，值]，定义一个w[]的列表，取w[1]，就是列表里面的第二个数，也就是字典里面的值

    return render(request, 'count.html',
                  {'count': total_count,'text':user_text,
                   'wordict':word_dict,
                   'sorted':sorted_dict})
def about(request):
    return render(request,'about.html')