from django.urls import path

from drf_problems.views import ErrorDocumentationView

app_name = 'drf_problems'

urlpatterns = [
    path('problems/<slug:code>/', ErrorDocumentationView.as_view(),
         name='error-documentation')
]
