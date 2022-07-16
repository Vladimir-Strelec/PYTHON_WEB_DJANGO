from django.contrib.auth import mixins as auth_mixin, get_user_model
from django.shortcuts import redirect
from django.views import generic as views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy


from parallax.accounts.forms import CreateProfileForm, EditProfileForm, DeleteProfileForm
from parallax.accounts.models import Profile, ShopUser
from parallax.common.view_mixin import RedirectToCatalog


class UserRegisterView(RedirectToCatalog, views.CreateView):
    form_class = CreateProfileForm
    template_name = 'account/registration.html'
    success_url = reverse_lazy('login user')


class UserLoginView(auth_views.LoginView):
    template_name = 'account/login.html'
    success_url = reverse_lazy('catalog')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


# def edit_profile(request):
#     return profile_action(request, EditProfileForm, 'profile details', get_profile(), 'main/profile_edit.html')
#
class EditProfileView(auth_mixin.LoginRequiredMixin, views.UpdateView):
    form_class = EditProfileForm
    template_name = 'account/edit-profile.html'
    success_url = reverse_lazy('index')
    queryset = Profile.objects.all()

# class ChangeUserPasswordView(auth_views.PasswordChangeView):
#     template_name = 'accounts/change_password.html'


class ProfileDetailsView(auth_mixin.LoginRequiredMixin, views.DeleteView):
    template_name = 'account/profile-details.html'
    queryset = Profile.objects.all()

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['object'] = self.object
    #     r = self.request
    #     o = self.object
    #     a=5
    #     return context
    # def form_valid(self, form):
    #     form.instance.user = self.request.user
    #     return super().form_valid(form)


    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     # self.object is a Profile instance
    #     profile = Profile.objects.filter(user_id=self.object.user_id)
    #
    #     context.update({
    #         'is_owner': self.object.user_id == self.request.user.id,
    #         'object': profile,
    #
    #     })
    #
    #     return context

class DeleteProfileView(auth_mixin.LoginRequiredMixin, views.DeleteView):
    model = ShopUser
    template_name = 'account/delete-profile.html'
    success_url = reverse_lazy('index')


class ChangeUserPasswordView(auth_views.PasswordChangeView):
    template_name = 'account/change-password.html'


class LogOutUser(auth_views.LogoutView):
    template_name = 'account/login.html'
