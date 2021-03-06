# Generated by Django 3.1.5 on 2021-05-14 07:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Название документа')),
                ('createdAt', models.DateTimeField(auto_now=True, verbose_name='Создан')),
                ('updatedAt', models.DateTimeField(auto_now_add=True, verbose_name='Последнее обновление')),
                ('addedBy', models.ForeignKey(blank=True, editable='False', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='added_docs_set', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('allowedTo', models.ManyToManyField(related_name='allowed_docs_to', to=settings.AUTH_USER_MODEL, verbose_name='Разрешено к просмотру')),
            ],
        ),
    ]
