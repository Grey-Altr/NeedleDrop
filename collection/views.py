from django.shortcuts import render, redirect
from .models import Release
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin


# Views ------------------------------

# Home CBV
class Home(LoginView):
    template_name = 'home.html'
    
# Release CBV
class ReleaseList(LoginRequiredMixin, ListView):
    model = Release
    template_name = 'releases/release_list.html'
    
    def get_queryset(self):
        return Release.object.filter(user=self.request.user)
    
# Detail CBV
class ReleaseDetail(LoginRequiredMixin, DetailView):
    model = Release
    template_name = 'releases/detail.html'
    
# Create CBV
class ReleaseCreate(LoginRequiredMixin, CreateView):
    model = Release
    fields = ['title', 'artist', 'label', 'media_format', 'cover_image', 'description']
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
# Update CBV
class ReleaseUpdate(LoginRequiredMixin, UpdateView):
    model = Release
    fields = ['title', 'artist', 'label', 'media_format', 'cover_image', 'description']
    
# Delete CBV
class ReleaseDelete(LoginRequiredMixin, DeleteView):
    model = Release
    success_url = '/releases/'
    
# signup FBV
def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('release-index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)