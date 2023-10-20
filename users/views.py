from django.shortcuts import render
from django.views import generic
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import CustomUser


class SighUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'sighup.html'

    def form_valid(self, form):
        if 'image' in self.request.FILES:
            form.instance.image = self.request.FILES['image']

        return super().form_valid(form)


class CustomUserUpdate(LoginRequiredMixin, generic.UpdateView):
    model = CustomUser
    template_name = 'custom_user_edit.html'
    success_url = reverse_lazy('profile')
    fields = ['username', 'email', 'image']


class CustomUserDelete(LoginRequiredMixin, generic.DeleteView):
    model = CustomUser
    template_name = 'custom_user_delete_confirm.html'
    success_url = reverse_lazy('profile')


@login_required
def profile(request):
    user = request.user
    return render(request, 'profile.html',
                  context={user: 'user'})
