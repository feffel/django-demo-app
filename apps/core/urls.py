from django.urls import path

import apps.core.views as views

app_name = 'core'

urlpatterns = [
    path(r'', views.RootView.as_view(), name='root'),
]
