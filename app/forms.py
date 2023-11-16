from django import forms

from app.models import URLShort


class URLShortForm(forms.ModelForm):
    class Meta:
        model = URLShort
        fields = ["long_url"]
