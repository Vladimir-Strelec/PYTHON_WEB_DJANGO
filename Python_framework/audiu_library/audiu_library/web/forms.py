from django import forms

from audiu_library.web.models import Todo


class AddForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('title',)
