from django.urls import path
from apps.leads import views as LeadViews

app_name = 'leads'

urlpatterns = [
    path(r'list/', LeadViews.LeadsListView, name='list-leads'),
    path(r'add/', LeadViews.LeadsAddView, name='add-lead'),
]
