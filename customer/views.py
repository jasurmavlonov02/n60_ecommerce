import csv
import json
from django.views.generic import ListView

from django.shortcuts import render
from django.http import HttpResponse

from customer.models import Customer
from django.forms.models import model_to_dict


# Create your views here.


class CustomerListView(ListView):
    template_name = 'customer/customer-list.html'
    queryset = Customer.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CustomerListView, self).get_context_data(**kwargs)
        context['customers'] = Customer.objects.all()
        return context



def export_data(request):
    format = request.GET.get('format')
    if format == 'csv':
        meta = Customer._meta
        field_names = [field.name for field in meta.fields]
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=customer_list.csv'
        writer = csv.writer(response)
        writer.writerow(field_names)
        for obj in Customer.objects.all():
            row = writer.writerow([getattr(obj,field) for field in field_names])
        return response

    elif format == 'json':
        response = HttpResponse(content_type='application/json')
        data = list(Customer.objects.all().values('id','full_name', 'email', 'phone_number', 'address','joined'))
        # response.content = json.dumps(data, indent=4)
        response.write(json.dumps(data, indent=4,default=str))
        response['Content-Disposition'] = 'attachment; filename=customers.json'
        return response
    
    elif format == 'xlsx':
        pass
    else:
        response =  HttpResponse(status=404)
        response.content = 'Bad request'
        return response
    