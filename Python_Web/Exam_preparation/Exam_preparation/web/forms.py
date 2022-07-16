import os

from django import forms

from Exam_preparation.web.models import Profile, Expense


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class CreateExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'


class DeleteProfile(forms.ModelForm):
    def save(self, commit=True):
        # image_path = self.instance.image.path
        self.instance.delete()
        # os.remove(image_path)
        return self.instance

    class Meta:
        model = Profile
        fields = ()


class DeleteExpense(forms.ModelForm):
    def save(self, commit=True):
        # image_path = self.instance.image.path
        self.instance.delete()
        # os.remove(image_path)
        return self.instance

    class Meta:
        model = Profile
        fields = ()