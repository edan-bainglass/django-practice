from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (View, TemplateView, ListView, DetailView,
                                  CreateView, UpdateView, DeleteView)
from . import models

# Create your views here.


class CBView(View):
    """docstring"""

    def get(self, request: HttpRequest) -> HttpResponse:
        return HttpResponse("CLASS BASED VIEWS ARE COOL!")


class IndexView(TemplateView):
    """docstring"""

    template_name = 'basic_app/index.html'

    def get_context_data(self, **kwargs) -> None:
        """Injects context to template."""
        context = super().get_context_data(**kwargs)
        context['inject_me'] = "BASIC INJECTION!"
        return context


class SchoolListView(ListView):
    """docstring"""

    context_object_name = 'schools'  # overrides default 'school_list'
    model = models.School


class SchoolDetailView(DetailView):
    """docstring"""

    model = models.School
    template_name = 'basic_app/school_detail.html'


class SchoolCreateView(CreateView):
    """docstring"""

    fields = ('name', 'principal', 'location')
    model = models.School


class SchoolUpdateView(UpdateView):
    """docstring"""

    fields = ('name', 'principal')
    model = models.School


class SchoolDeleteView(DeleteView):
    """docstring"""

    model = models.School
    success_url = reverse_lazy('basic_app:list')


class StudentCreateView(CreateView):
    """docstring"""

    fields = ('name', 'age')
    model = models.Student

    def form_valid(self, form):
        print(form)
        form.instance.school = self.request.school
        return super().form_valid(form)


class StudentUpdateView(UpdateView):
    """docstring"""

    fields = ('age')
    model = models.Student


class StudentDeleteView(DeleteView):
    """docstring"""

    model = models.Student
    success_url = reverse_lazy('basic_app:list')
