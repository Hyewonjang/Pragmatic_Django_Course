from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from Accountapp.models import HelloWorld


def hello_world(request):
    #return HttpResponse('Hello world!')  # HttpResponse는 views에서 직접적으로 response해주는 것.

    if request.method == "POST":

        temp = request.POST.get('hello_world_input')

        new_hello_world = HelloWorld()  # 새로운 HelloWorld 객체 생성
        new_hello_world.text = temp    # 새로운 HelloWorld 객체의 text 속성 작성
        new_hello_world.save()    # 새로운 HelloWorld 객체 DB에 저장

        return render(request, 'Accountapp/hello_world.html', context={'hello_world_output': new_hello_world})
    else:
        return render(request, 'Accountapp/hello_world.html', context={'text': 'GET METHOD!!!'})