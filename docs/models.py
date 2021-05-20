from django.db import models
from django.contrib.auth.models import User


class Document(models.Model):
    allowedTo = models.ManyToManyField(User, related_name='allowed_docs_to', verbose_name='Разрешено к просмотру')
    name = models.CharField(max_length=64, verbose_name='Название документа')
    addedBy = models.ForeignKey(User, related_name='added_docs_set', on_delete=models.CASCADE, editable='False',
                                null=True, blank=True, verbose_name='Автор')
    createdAt = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updatedAt = models.DateTimeField(auto_now=True, verbose_name='Последнее обновление')

    def __str__(self):
        return self.name


class DocumentFile(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    file = models.FileField(upload_to='files/', verbose_name='файл')

    def __str__(self):
        return self.file.name.split('/')[-1]
