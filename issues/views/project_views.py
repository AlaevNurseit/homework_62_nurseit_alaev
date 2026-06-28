from urllib.parse import urlencode
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse, reverse_lazy
from django.views.generic import DeleteView, ListView,DetailView,CreateView,UpdateView
from issues.forms import SimpleSearchForm, ProjectForm
from issues.models import Project



class ProjectView(ListView):
    template_name = "project/project_list.html"
    model = Project
    context_object_name = "projects"
    ordering = ['start_date']
    paginate_by = 5
    paginate_orphans = 1

    def dispatch(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().dispatch(request, *args, **kwargs)

    def get_search_form(self):
        return SimpleSearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = self.form

        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
            context['search_value'] = self.search_value
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            queryset = queryset.filter(
                Q(name__icontains=self.search_value) | Q(description__icontains=self.search_value)
            )
        return queryset

class ProjectDetailView(DetailView):
    template_name = "project/project_detail.html"
    model = Project
    context_object_name = "project"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['issues'] = self.object.issues.all()
        return context

class ProjectCreateView(LoginRequiredMixin, CreateView):
    template_name = "project/project_create.html"
    model = Project
    form_class = ProjectForm

    def get_success_url(self):
        return reverse('issues:project_list')


class ProjectUpdateView(LoginRequiredMixin,UpdateView):
    template_name = "project/project_update.html"
    model = Project
    form_class = ProjectForm

    def get_success_url(self):
        return reverse('issues:project_detail', kwargs={'pk': self.object.pk})


class ProjectDeleteView(LoginRequiredMixin,DeleteView):
    template_name = "project/project_delete.html"
    model = Project

    def get_success_url(self):
        return reverse_lazy('issues:project_list')



