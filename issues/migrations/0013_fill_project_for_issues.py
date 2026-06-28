from django.db import migrations

def fill_project(apps, schema_editor):
    Project = apps.get_model('issues', 'Project')
    Issue = apps.get_model('issues', 'Issue')

    project = Project.objects.create(
        name='Основной проект',
        description='Проект для существующих задач',
        start_date='2026-01-01',
        end_date='2026-12-31'
    )

    Issue.objects.update(project=project)


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0011_project_issue_project'),
    ]

    operations = [
        migrations.RunPython(fill_project),
    ]