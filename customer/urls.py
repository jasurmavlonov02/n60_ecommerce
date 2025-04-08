from django.urls import path, include

from customer import views

app_name = 'customer'

urlpatterns = [
    path('customer-list/', views.CustomerListView.as_view(), name='customer-list'),
    path('export-data/',views.export_data,name='export_data')
]
