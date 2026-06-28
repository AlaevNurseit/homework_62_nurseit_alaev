from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import DetailView, DeleteView, CreateView, UpdateView
from issues.models import Issue, Project
from issues.forms import IssueForm

class IssueDetailView(DetailView):
    template_name = "issues/issue_detail.html"
    model = Issue
    context_object_name = "issue"

class IssueCreateView(LoginRequiredMixin,CreateView):
    template_name = "issues/issue_create.html"
    model = Issue
    form_class = IssueForm

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs['project_pk'])
        form.instance.project = project
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('issues:project_detail', kwargs={'pk': self.object.project.pk})


class IssueUpdateView(LoginRequiredMixin,UpdateView):
    template_name = "issues/issue_update.html"
    model = Issue
    context_object_name = "issue"
    form_class = IssueForm

    def get_success_url(self):
        return reverse('issues:issue_detail', kwargs={'pk': self.object.pk})

class IssueDeleteView(LoginRequiredMixin,DeleteView):
    template_name = "issues/issue_confirm_delete.html"
    model = Issue


    def form_valid(self, form):
        self.project_pk = self.object.project.pk
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('issues:project_detail', kwargs={'pk': self.project_pk})




