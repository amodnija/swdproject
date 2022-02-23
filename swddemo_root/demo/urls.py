from django.urls import path

from . import views
from .views import LeaveList, LeaveView

urlpatterns = [
    path('', views.leave_req, name='leave-request'),
    path('show/<int:pk>', LeaveView.as_view(), name='leave-detail'),
    path('show', LeaveList.as_view(), name='show-leaves'),
]