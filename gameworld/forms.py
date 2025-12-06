from django import forms

class GameForm(forms.Form):
    title = forms.CharField(max_length=150)
    desc = forms.CharField(widget=forms.Textarea)
    category = forms.CharField(widget=forms.Select)
    price = forms.IntegerField()
    image = forms.ImageField()

    
