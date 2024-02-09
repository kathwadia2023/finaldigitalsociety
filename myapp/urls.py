from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('',views.index, name='index'),
    path('contact/', views.contact_us),
    path('go_green/', views.go_green),
    path('event/', views.event),
    path('com_member/', views.com_member),
    path('otp_verify/',views.otp,name='otp'),
    path('member_page/', views.member_page, name="member_page"),
    path('user_logout/', views.user_logout),
    path('profile/', views.profile),
    path('complaint/', views.complaint_reg, name='complaint'),
    path('maintenance/', views.maintenance_pay),
    path('residence_det/', views.residence_detail),
    # path('status_update/<int:id>', views.status_up),
    path('status_up/<int:id>', views.status_up ),
    path('inquiry_data/', views.inq_data),
    path('global_mail_send/', views.global_mail),

    path('resetpass/',views.resetpass, ),
    path('newpass/',views.newpass, name='newpass'),

]