from django.contrib.auth import get_user_model
from django.contrib.auth import mixins as auth_mixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as auth_views
from django.views import generic as views

from parallax.accounts.models import Profile, ShopUser
from parallax.common.view_mixin import RedirectToCatalog
from parallax.web.forms import CreateProductForm, EditProductForm, DeleteProductForm, \
    CreateReviewProductForm
from parallax.web.models import AbstractProduct, CommentsProducts


class HomeTemplateView(RedirectToCatalog, views.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['valid_register'] = False
        return context


class CreateProductView(auth_views.CreateView):
    template_name = 'product/create_product.html'
    form_class = CreateProductForm
    success_url = reverse_lazy('catalog')


class EditProductView(auth_views.UpdateView):

    template_name = 'product/edit-product.html'
    form_class = EditProductForm
    queryset = AbstractProduct.objects.all()
    success_url = reverse_lazy('catalog')


class InfoProductView(auth_views.DeleteView):
    model = AbstractProduct
    template_name = 'product/ditailes-product.html'
    queryset = AbstractProduct.objects.all()


class DeleteProductView(auth_views.DeleteView):
    model = AbstractProduct
    template_name = 'product/delete-product.html'
    queryset = AbstractProduct.objects.all()
    form_class = DeleteProductForm
    success_url = reverse_lazy('catalog')


class CatalogView(auth_views.ListView):
    model = AbstractProduct
    template_name = 'product/catalog.html'
    context_object_name = 'objects'


def add_comments_product(request, pk):
    current_product_object = AbstractProduct.objects.get(pk=pk)
    if request.method == 'POST':
        form = CreateReviewProductForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            review_user = request.user.id
            review = CommentsProducts(text=text, user_id=review_user, product_id=current_product_object.id)
            review.save()
            return redirect('catalog')
    form = CreateReviewProductForm()
    context = {
        'form': form,
        'object': current_product_object
    }
    return render(request, 'comments/add-comments.html', context)


class AllCommentsView(auth_views.TemplateView):
    model = CommentsProducts
    template_name = 'comments/all-comments-product.html'

    def get_context_data(self, **kwargs):
        all_comments_in_product = sorted(set(CommentsProducts.objects.filter(user__commentsproducts__product_id=kwargs['pk'])), key=lambda kvp: [-kvp.id])

        context = super().get_context_data(**kwargs)
        context['all_comments_in_product'] = all_comments_in_product
        return context
