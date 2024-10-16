# employees/urls.py
from django.urls import path
from .views import EmployeeListCreateView, EmployeeRetrieveUpdateDestroyView

urlpatterns = [
    path('', EmployeeListCreateView.as_view(), name='employee-list-create'),  # Root path for listing and creating
    path('<int:pk>/', EmployeeRetrieveUpdateDestroyView.as_view(), name='employee-detail'),  # Detail path for specific employee
]
