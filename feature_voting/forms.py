from django import forms
from .models import FeatureRequest

class FeatureForm(forms.ModelForm):
    class Meta:
        model = FeatureRequest
        fields = ['title', 'description']