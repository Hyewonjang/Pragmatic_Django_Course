from django.contrib.auth.forms import UserCreationForm

class AccountUpdateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].disabled = True     # id(username)칸이 바꿀 수 없도록 비활성화시킴. / 브라우저창을 통해 username을 다른 것으로 바꿔도 disabled가 True되어 있는 한 반영되지 않는다.