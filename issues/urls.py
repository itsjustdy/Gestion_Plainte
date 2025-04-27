from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('report/', views.report_issue, name='report_issue'),
    path('issues/', views.issue_list, name='issue_list'),
    path('issues/<int:issue_id>/', views.issue_detail, name='issue_detail'),
    path('issues/<int:issue_id>/update_status/', views.update_issue_status, name='update_issue_status'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', views.logout_views, name='logout'),
]