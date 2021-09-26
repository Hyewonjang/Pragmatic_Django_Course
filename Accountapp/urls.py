from django.urls import path

from Accountapp.views import hello_world, AccountCreateView

app_name = "Accountapp"

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),

    path('create/', AccountCreateView.as_view(), name='create'), # class view를 불려오려면 함수 view와 달리 뒤에 .as_view()를 붙여야 한다.


]