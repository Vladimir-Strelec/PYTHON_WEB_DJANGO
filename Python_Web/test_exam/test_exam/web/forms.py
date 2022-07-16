from django import forms

from test_exam.web.models import Profile, Note


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class CreateNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = '__all__'


class EditNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = '__all__'


class DeleteNoteForm(forms.ModelForm):
    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Note
        fields = '__all__'
