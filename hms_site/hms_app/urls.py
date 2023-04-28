from django.urls import path
from . import views
urlpatterns = [
    path('',views.login_view,name="login_view"),
    path('signup/',views.signup_view,name="signup_view"),
    path('book/',views.book_view,name="book_view"),
    path('dashboard/',views.dashboard_view,name="dashboard_view"),
    path('hosteladmin/',views.hosteladmin_view,name='hosteladmin_view'),
    path('hosteladminpage/',views.hosteladminpage_view,name="hosteladminpage_view")
]