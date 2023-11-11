from django.urls import path
from complaint_review.views import show_complaint_form

app_name = 'complaint_review'

urlpatterns = [
    path('complaint', show_complaint_form, name = 'show_complaint'),
]
