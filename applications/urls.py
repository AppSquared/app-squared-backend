from django.urls import path
from . import views

urlpatterns = [
    path('applications/', views.ApplicationList.as_view(), name='application_list'),
    path('applications/<int:pk>', views.ApplicationDetail.as_view(), name='application_detail'),
    path('contacts/', views.ContactList.as_view(), name='contact_list'),
    path('contacts/<int:pk>', views.ContactDetail.as_view(), name='contact_detail'),
]
