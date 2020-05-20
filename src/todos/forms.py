from django import forms
from django.utils import timezone

from .models import Todo


class DateInput(forms.DateInput):
    input_type = 'date'


class TodoModelForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['text', 'slug']
        widgets = {
            'text': forms.TextInput(attrs={'class': 'form-control mb-2 mr-sm-2', 'placeholder': 'Enter To Do Item'}),
            'slug': forms.TextInput(attrs={'class': 'form-control mb-2 mr-sm-2', 'placeholder': 'Enter Slug'}),
        }

    def clean_slug(self, *args, **kwargs):
        slug = self.cleaned_data.get('slug')
        if len(slug) < 3:
            raise forms.ValidationError(
                "The slug needs to be at-least 6 characters in length or above")
        if slug.find('-') == -1:
            raise forms.ValidationError(
                "The slug needs to have a '-' character in it.")
        qs = Todo.objects.filter(slug__iexact=slug)
        if qs.exists():
            raise forms.ValidationError("The slug has already been used")
        return slug
