from django import forms

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class AddPostForm(forms.Form):
    title = forms.CharField(max_length=255)
    public_user = forms.CharField(max_length=255)
    content = forms.CharField(widget=forms.Textarea())
    file = forms.FileField()
    is_published = forms.BooleanField()

