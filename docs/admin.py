from django.contrib import admin

from .models import Document, DocumentFile


class DocumentFileAdmin(admin.StackedInline):
    model = DocumentFile
    verbose_name = 'Файл'
    verbose_name_plural = 'Файлы'
    extra = 1

    def has_delete_permission(self, request, obj=None):
        if obj is not None and not request.user.is_superuser and obj.addedBy != request.user:
            return False
        else:
            return True

    def has_change_permission(self, request, obj=None):
        if obj is not None and not request.user.is_superuser and obj.addedBy != request.user:
            return False
        else:
            return True

    def has_add_permission(self, request, obj=None):
        if obj is not None and not request.user.is_superuser and obj.addedBy != request.user:
            return False
        else:
            return True


class DocumentAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Общая инофрмация', {
            'fields': (
                'name', 'allowedTo',
            )
        }),
        ('Служебная информация', {
            'fields': (
                'addedBy', 'createdAt', 'updatedAt'
            )
        })
    )
    readonly_fields = ('addedBy', 'createdAt', 'updatedAt')
    search_fields = ('name',)
    list_display = ('name',)
    inlines = [DocumentFileAdmin, ]

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            # Only set added_by during the first save.
            obj.addedBy = request.user
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(allowedTo=request.user)

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser

        if obj is not None and not is_superuser:
            if not obj.addedBy == request.user:
                # self.readonly_fields += ('name', 'allowedTo')
                form.base_fields['name'].disabled = True
                form.base_fields['allowedTo'].disabled = True

        return form


admin.site.register(Document, DocumentAdmin)
