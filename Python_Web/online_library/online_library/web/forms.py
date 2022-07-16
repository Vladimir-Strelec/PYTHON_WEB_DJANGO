from django import forms

from online_library.web.models import Profile, Book


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {'first_name': forms.TextInput(attrs={'placeholder': 'Enter First Name'}),
                   'last_name': forms.TextInput(attrs={'placeholder': 'Enter Last Name'}),
                   'image_url': forms.TextInput(attrs={'placeholder': 'URL'}),
                   }


class CreateBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        widgets = {'title': forms.TextInput(attrs={'placeholder': 'Title'}),
                   'description': forms.Textarea(attrs={'placeholder': 'Description'}),
                   'image': forms.URLInput(attrs={'placeholder': 'Image'}),
                   'type': forms.TextInput(attrs={'placeholder': 'Type'}),
                   }


class DeleteProfileForm(forms.ModelForm):
    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Profile
        fields = '__all__'


class DeleteBookForm(forms.ModelForm):
    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Book
        fields = '__all__'