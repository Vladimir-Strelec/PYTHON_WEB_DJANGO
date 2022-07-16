import os
from dataclasses import fields

from django import forms

from exams.web.models import Profile, Expense


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileDeleteForm(forms.ModelForm):
    def save(self, commit=True):
        image_path = self.instance.image.path
        self.instance.delete()
        os.remove(image_path)
        return self.instance

    class Meta:
        model = Profile
        fields = '__all__'


class CreateExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'


class ExpenseEditForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'


class ExpenseDeleteForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for _, field in self.fields.items():
    #         field.widget.attrs['disable'] = 'disable'

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Expense
        fields = '__all__'
