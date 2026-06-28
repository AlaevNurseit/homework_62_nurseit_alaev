from django.db import migrations


def transfer_types(apps, schema_editor):
    Issue = apps.get_model('issues', 'Issue')
    for issue in Issue.objects.all():
        if issue.old_type:
            issue.types.add(issue.old_type)


def rollback_transfer(apps, schema_editor):
    Issue = apps.get_model('issues', 'Issue')
    for issue in Issue.objects.all():
        first_type = issue.types.first()
        if first_type:
            issue.old_type = first_type
            issue.save()


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0005_issue_types_remove_issue_old_type_issue_old_type'),
    ]

    operations = [
        migrations.RunPython(transfer_types, rollback_transfer),
    ]