from django import forms
from editinfo.models import Developer


class DeveloperForm(forms.ModelForm):
    class Meta:
        model = Developer
        fields = '__all__'