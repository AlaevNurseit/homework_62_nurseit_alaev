from django import forms
from .models import Issue, Status, Type, Project


class IssueForm(forms.ModelForm):
    summary = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}),required=True,label="Краткое описание",error_messages={"required": "Обязательное поле"})
    description = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control", "rows": "5"}),required=False,label="Полное описание" )
    status = forms.ModelChoiceField(queryset=Status.objects.all(),widget=forms.Select(attrs={"class": "form-select"}),label="Статус")
    types = forms.ModelMultipleChoiceField(queryset=Type.objects.all(),widget=forms.CheckboxSelectMultiple,label="Типы")
    class Meta:
        model = Issue
        fields = ('summary', 'description', 'status', 'types')


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="")

class ProjectForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}), required=True,label="название проекта")
    description = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control", "rows": "5"}), required=False,label="описание")
    start_date = forms.DateField(widget=forms.DateInput(attrs={"class": "form-control", "type": "date"}),label="Дата начала")
    end_date = forms.DateField(widget=forms.DateInput(attrs={"class": "form-control", "type": "date"}), required=False,label="Дата начала")

    class Meta:
        model = Project
        fields = ('name', 'description', 'start_date', 'end_date')

