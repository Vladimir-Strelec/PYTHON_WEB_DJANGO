from django import forms

from common.helpers import BootstrapFormMixin
from parallax.web.models import AbstractProduct, CommentsProducts


class CreateProductForm(forms.ModelForm):
    class Meta:
        model = AbstractProduct
        fields = '__all__'


class EditProductForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = AbstractProduct
        fields = '__all__'


class DeleteProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, fild in self.fields.items():
            fild.widget.attrs['disabled'] = 'disabled'
            fild.required = False

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = AbstractProduct
        fields = '__all__'


class CreateReviewProductForm(forms.ModelForm):
    text = forms.TextInput()

    class Meta:
        model = CommentsProducts
        fields = ('text',)
        # widgets = {
        #     'text': forms.Textarea(attrs={'class': 'form-control'}),
        # }