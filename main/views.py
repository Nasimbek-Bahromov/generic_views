from django.shortcuts import render
from typing import Any
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView,  DeleteView, FormView, DayArchiveView, WeekArchiveView
from .form import WorkCreateForm, ContactForm, WorkUpdateForm
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from . import models


# def main(request):
#     return render(request, 'index.html')

# def login(request):
#     return render(request, 'login-register.html')


# def register(request):
#     return render(request, 'login-register.html')



""" generic view """





def home(request):
    work = models.Work.objects.all()
    context = {
        'work': work
    }
    return render(request, 'index.html', context)


class WorkListView(ListView):
    model = models.Work
    template_name = 'index.html'
    paginate_by = 3
    context_object_name = 'works'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset


class WorkDetailView(DetailView):
    model = models.Work
    template_name = 'index.html'
    context_object_name = 'work'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    

class WorkCreateView(CreateView):
    model = models.Work
    form_class = WorkCreateForm
    success_url = reverse_lazy('work_list')


class WorkDayArchiveView(DayArchiveView):
    queryset = models.Work.objects.all()
    date_field = 'pub_date'


class WorkWeekArchiveView(WeekArchiveView):
    queryset = models.Work.objects.all()
    date_field = 'pub_date'


class ContactView(FormView):
    template_name = 'index.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact_success')

    def form_valid(self, form):
        return super().form_valid(form)


class WorkDeleteView(DeleteView):
    model = models.Work
    success_url = reverse_lazy('work_list')


class WorkUpdateView(UpdateView):
    model = models.Work
    form_class = WorkUpdateForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('work_detail', kwargs={'pk': self.object.pk})