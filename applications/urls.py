from django.urls import path
from . import views

urlpatterns = [
    path('applications/', views.ApplicationList.as_view(), name='application_list'),
    path('applications/<int:pk>', views.ApplicationDetail.as_view(), name='application_detail'),
    # path('companies/', views.CompanyList.as_view(), name='company_list'),
    # path('companies/<int:pk>', views.CompanyDetail.as_view(), name='company_detail'),
]
