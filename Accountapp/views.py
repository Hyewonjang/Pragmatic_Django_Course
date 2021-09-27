from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView

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

# 함수형 뷰로 표현한다면 더 길어졌을 것임.
class AccountCreateView(CreateView):
    model = User    # 장고에서 기본으로 제공해주는 model인 User 사용
    form_class = UserCreationForm   # 장고에서 기본적으로 제공해주는 Form - 패스퉈드 1,2 입력 및 확인/검증작업
    success_url = reverse_lazy('Accountapp:hello_world')    # reverse_lazy는 클래스형 뷰에서 사용하고, reverse는 함수형 뷰에서 사용 / 그리고 다음 코드는 성공시 돌아갈 페이지 url을 설정하는 것임.
    template_name = 'Accountapp/create.html'    # 회원가입을 할 때 보일 html 비주얼

class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user' # detail.html에서 user정보 보여줄 때 user라고 쓰면 다른 사람이 해당 사이트를 사용할 때 보여주는 정보가 해당 유저의 정보가 아니라 내 정보일 가능성이 있기 떄문에 다음과 같이 대상 유저를 가리키는 명칭을 target_user 등으로 바꿔준다. 바꾸면 앞의 우려를 예방할 수 있다.
    template_name = 'Accountapp/detail.html'