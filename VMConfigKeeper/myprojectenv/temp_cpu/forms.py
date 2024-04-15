from django import forms
from .models import vmconfig
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class AddPostForm(forms.ModelForm):
    
    
    class Meta:
        model = vmconfig
        fields = ['title', 'public_user', 'slug', 'content', 'file' ,'is_published']

        wigets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'title': "Название конфигурации", 
            'public_user': 'Имя пользователя',
            'slug': 'URL',
            'content': 'Описание конфигурации',
            'is_published': 'Соглашение на публикацию'
        }

   #file = models.FileField(null=True)

