from django import forms

class indexForm(forms.Form):
    category = forms.ChoiceField(choices=[(x,x) for x in range(1, 32)])