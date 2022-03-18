from django import forms

class sign_in(forms.Form):
    Username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control',
    'placeholder':'Username',
    'type':'text',
    'required':True}))
    Password = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control',
    'placeholder':'Password',
    'type':'password',
    'required':True}))

class sign_up(forms.Form):
    username = forms.CharField(widget = forms.TextInput(attrs=
    {'class':'form-control','placeholder':'Username','type':'text','required':True
    }))
    email = forms.CharField(widget = forms.TextInput(attrs={
        'class':'form-control','placeholder':'Email','type':'text','required':True
          }))
    password = forms.CharField(widget = forms.TextInput(attrs={
        'class':'form-control','placeholder':'password','required':True,'type':'password'
        }))
    Firstname = forms.CharField(widget = forms.TextInput(attrs={
        'class':'form-control','placeholder':'First Name','required':True,'type':'text'
        }))
    Lastname = forms.CharField(widget = forms.TextInput(attrs={
        'class':'form-control','placeholder':'Last Name','required':True,'type':'text'
        }))
