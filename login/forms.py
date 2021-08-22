from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.contrib.auth.models import User
from django import forms

class ChangeUserPassword(PasswordChangeForm):

    class Meta:
        model = User

    def __init__(self, *args, **kwargs):
        super(PasswordChangeForm,self).__init__(*args,*kwargs)
        self.fields['old_password'].widget.attrs['class']='form-control'
        self.fields['old_password'].widget.attrs['placeholder']='Enter Password'
        self.fields['old_password'].label=''
        self.fields['old_password'].help_text=''
        self.fields['new_password1'].widget.attrs['class']='form-control'
        self.fields['new_password1'].widget.attrs['placeholder']='Confirm Password'
        self.fields['new_password1'].label=''
        self.fields['new_password1'].help_text=''
        self.fields['new_password2'].widget.attrs['class']='form-control'
        self.fields['new_password2'].widget.attrs['placeholder']='Enter Password'
        self.fields['new_password2'].label=''
        self.fields['new_password2'].help_text=''


class EditProfileForm(UserChangeForm):
    email = forms.EmailField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':"Enter Email"}))
    first_name = forms.CharField(max_length=255,label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':"Enter Firstname"}))
    last_name  = forms.CharField(max_length=255,label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':"Enter Lastname"}))

    password = forms.CharField(label="",widget=forms.TextInput(attrs={'type':'hidden'}))

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password',)

    def __init__(self, *args, **kwargs):
        super(EditProfileForm,self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['username'].widget.attrs['placeholder']='Enter Username'
        self.fields['username'].label=''
        self.fields['username'].help_text=''


class SignUpForms(UserCreationForm):
    email = forms.EmailField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':"Enter Email"}))
    first_name = forms.CharField(max_length=255,label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':"Enter Firstname"}))
    last_name  = forms.CharField(max_length=255,label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':"Enter Lastname"}))

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')

    def __init__(self, *args, **kwargs) -> None:
        super(SignUpForms,self).__init__(*args,**kwargs)


        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['username'].widget.attrs['placeholder']='Enter Username'
        self.fields['username'].label=''
        self.fields['username'].help_text=''
        self.fields['password1'].widget.attrs['class']='form-control'
        self.fields['password1'].widget.attrs['placeholder']='Enter Password'
        self.fields['password1'].label=''
        self.fields['password1'].help_text=''
        self.fields['password2'].widget.attrs['class']='form-control'
        self.fields['password2'].widget.attrs['placeholder']='Confirm Password'
        self.fields['password2'].label=''
        self.fields['password2'].help_text=''
