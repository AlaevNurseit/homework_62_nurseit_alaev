from django.urls import path
from issues.views.issues_tracker import IssueCreateView, IssueDeleteView, IssueUpdateView, IssueDetailView
from issues.views.project_views import ProjectView, ProjectDetailView, ProjectCreateView, ProjectUpdateView, ProjectDeleteView

app_name = "issues"

urlpatterns = [
    path("<int:pk>/", IssueDetailView.as_view(), name="issue_detail"),
    path("projects/<int:project_pk>/issues/create/", IssueCreateView.as_view(), name="issue_create"),
    path("<int:pk>/update/", IssueUpdateView.as_view(), name="issue_update"),
    path("<int:pk>/delete/", IssueDeleteView.as_view(), name="issue_delete"),

    path("projects/", ProjectView.as_view(), name="project_list"),
    path("projects/create/", ProjectCreateView.as_view(), name="project_create"),
    path("projects/<int:pk>/", ProjectDetailView.as_view(), name="project_detail"),
    path("projects/<int:pk>/update/", ProjectUpdateView.as_view(), name="project_update"),
    path("projects/<int:pk>/delete/", ProjectDeleteView.as_view(), name="project_delete"),
]