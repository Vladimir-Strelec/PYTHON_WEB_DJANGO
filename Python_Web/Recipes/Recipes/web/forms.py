from django import forms

from Recipes.web.models import Recipe


class CreatePicaForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter title'}),
            'image_url': forms.TextInput(attrs={'placeholder': 'Enter image_url'}),
            'description': forms.Textarea(attrs={'placeholder': 'Enter Description'}),
            'ingredients': forms.TextInput(attrs={'placeholder': 'Enter Ingredients'}),
            'time': forms.TimeInput(attrs={'min': '00:00:00'}),
        }


class EditPicaForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'


class DeletePicaForm(forms.ModelForm):
    def save(self, commit=True):
        instance = self.instance.delete()
        return instance

    class Meta:
        model = Recipe
        fields = '__all__'
