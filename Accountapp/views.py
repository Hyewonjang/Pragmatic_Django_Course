
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from Accountapp.models import HelloWorld


def hello_world(request):
    #return HttpResponse('Hello world!')  # HttpResponse는 views에서 직접적으로 response해주는 것.

    if request.method == "POST":

        temp = request.POST.get('hello_world_input')

        new_hello_world = HelloWorld()  # 새로운 HelloWorld 객체 생성
        new_hello_world.text = temp    # 새로운 HelloWorld 객체의 text 속성 작성
        new_hello_world.save()    # 새로운 HelloWorld 객체 DB에 저장

        #hello_world_list = HelloWorld.objects.all()
        #return render(request, 'Accountapp/hello_world.html', context={'hello_world_list': hello_world_list})
        # f5키 눌러도 POST한 결과가 중복되어 나타나지 않도록 하기 위함. 아래 redirect를 통해서 request.method는 post가 아닌 get인 상황으로 재연결된다.
        return HttpResponseRedirect(reverse('Accountapp:hello_world'))
    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'Accountapp/hello_world.html', context={'hello_world_list': hello_world_list})