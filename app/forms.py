from django import forms

class FeedForm(forms.Form):
    url = forms.URLField(label='Feed URL', max_length=1024)
