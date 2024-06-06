from django.urls import path
from .views import submit_contact_form, submit_career_form

app_name = 'home'

urlpatterns = [
    path('submit-contact/', submit_contact_form, name='submit_contact_form'),
    path('submit-career/', submit_career_form, name='submit_career_form'),
]
