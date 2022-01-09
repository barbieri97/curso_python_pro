from django import forms

class UserForm(forms.Form):
    conteudo = forms.CharField(max_length=280)
    observacao = forms.CharField(max_length=280)