import csv
from django.contrib import admin

from customer.models import Customer

from django.http import HttpResponse
# Register your models here.

# admin.site.register(Customer)

class ExportCsvMixin:
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        print(meta.fields)
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected"


@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin,ExportCsvMixin):
    list_display = ['id','full_name','email','vat_number']
    actions = ['export_as_csv']