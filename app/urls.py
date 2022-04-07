from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name = 'INDEX'),
    path('login/',views.login, name = 'login'),
    path('about/',views.about, name = 'about'), 
    path('blog-details/',views.blogdetails, name = 'blog-details'),
    path('blog-home/',views.bloghome, name = 'blog-home'),
    path('contact/',views.contact,name = 'contact'),
    path('departments/',views.departments, name = 'departments'),
    path('signup/',views.signup, name = 'signup'),
    path('otp/',views.otp, name = 'otp'),
    path('forgot-pass/',views.forgot_pass , name = 'forgot-pass'),
    path('forgot-otp/',views.forgot_otp, name = 'forgot-otp'),
    path('change-passowrd/',views.change_password, name = 'change-password')
]
