from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth.models import User
from .models import Account
from django import forms

# ログインフォームクラス
class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label   

# アカウント登録フォームクラス（メイン情報）
class AccountForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(),label="パスワード")

    class Meta():
        model = User
        fields = ('username','email','password')
        labels = {'username':'ユーザーID','email':'メール','password':'パスワード'}

# ログインフォームクラス（追加情報）
class AddAccountForm(forms.ModelForm):
    class Meta():
        model = Account
        fields = ('account_image',)
        labels = {'account_image':'アイコン画像',}