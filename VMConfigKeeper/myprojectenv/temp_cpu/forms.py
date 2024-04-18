from django import forms
from .models import vmconfig
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class AddPostForm(forms.ModelForm):
    
    
    class Meta:
        model = vmconfig
        fields = ['title', 'public_user', 'slug', 'content', 'file', 'is_published']

        wigets = {
            'title': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'type':"text", 'placeholder':".form-control-lg", 'aria-label':"Пример .form-control-lg"}),
            'public_user': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'type':"text", 'placeholder':".form-control-lg", 'aria-label':"Пример .form-control-lg"}),
            'slug': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'type':"text", 'placeholder':".form-control-lg", 'aria-label':"Пример .form-control-lg"}),
            'content': forms.Textarea(attrs={'class': 'form-control form-control-lg', 'type':"text", 'placeholder':".form-control-lg", 'aria-label':"Пример .form-control-lg"}),
            'file': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'type':"text", 'placeholder':".form-control-lg", 'aria-label':"Пример .form-control-lg"}),
            'is_published': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'type':"text", 'placeholder':".form-control-lg", 'aria-label':"Пример .form-control-lg"}),
        }
        labels = {
            'title': "Название конфигурации", 
            'public_user': 'Имя пользователя',
            'slug': 'URL',
            'content': 'Описание конфигурации',
            'file' : 'Конфигурационный файл',
            'is_published': 'Соглашение на публикацию'
        }


