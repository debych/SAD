from django.contrib import admin
from .models import Document


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

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            # Only set added_by during the first save.
            obj.addedBy = request.user
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(allowedTo=request.user)

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser

        if not is_superuser:
            if not obj.addedBy == request.user:
                #self.readonly_fields += ('name', 'allowedTo')
                form.base_fields['name'].disabled = True
                form.base_fields['allowedTo'].disabled = True

        return form


admin.site.register(Document, DocumentAdmin)
