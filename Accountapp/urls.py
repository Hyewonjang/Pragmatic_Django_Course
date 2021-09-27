from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from Accountapp.views import hello_world, AccountCreateView, AccountDetailView, AccountUpdateView

app_name = "Accountapp"

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),

    path('login/', LoginView.as_view(template_name='Accountapp/login.html'), name='login'), # 원래 views.py에서 LoginView를 상속받아 상세 설정해야 하는데 따로 설정할 내용이 크게 없기 때문에 바로 url로 기존에 제공되는 LoginView 연결해도 됨. LogoutView도 같음.
    path('logout/', LogoutView.as_view(), name='logout'),

    path('create/', AccountCreateView.as_view(), name='create'), # class view를 불려오려면 함수 view와 달리 뒤에 .as_view()를 붙여야 한다.
    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'),  # class view를 불려오려면 함수 view와 달리 뒤에 .as_view()를 붙여야 한다.
    path('update/<int:pk>', AccountUpdateView.as_view(), name='update'),

]