

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from audiu_library.web.forms import AddForm
from audiu_library.web.models import Todo


class AbstractClass(views.TemplateView):
    pass


class ListViews(AbstractClass, views.ListView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.model = None
        self.template = None


# class Home(views.View):
#     def get(self, request):
#         return render(request, template_name='home-with-profile.html', context={'obj': Todo.objects.all()})

class Home(AbstractClass):
    template_name = 'home-with-profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['obj'] = Todo.objects.all()
        return context


class AddAlbum(views.CreateView):
    model = Todo
    template_name = 'add-album.html'
    success_url = reverse_lazy('Home')
    # fields = ('title', 'description', 'category',)
    form_class = AddForm

    def get_form_class(self):
        pass #Dinamichno


    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['form'] = AddForm
    #     return context


    # def get_context_data(self, **kwargs):
    #     pass

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #
    #     return queryset

    # def get(self, *args, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['form'] = AddForm
    #     return context


class AlbumDetails(views.DetailView):
    model = Todo
    template_name = 'album-details.html'
    #
    # def get_object(self, queryset=None):
    #     obj = super().get_object(self, queryset=Todo.objects.)
    #     return obj



class EditAlbum():
     pass


class DeleteAlbum():
     pass


class ProfileDetails():
     pass


class DeleteProfile():
     pass

