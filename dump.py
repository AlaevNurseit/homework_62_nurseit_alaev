import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from issues.models import Issue, Status, Type
from django.core import serializers

data = serializers.serialize('json', [
    *Status.objects.all(),
    *Type.objects.all(),
    *Issue.objects.all(),
], indent=2, ensure_ascii=False)

with open('fixturess/issues.json', 'w', encoding='utf-8') as f:
    f.write(data)

print('Готово!')