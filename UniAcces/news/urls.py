from django.urls import path
from news.views import *

urlpatterns=[
    path('',homepage,name='index-page'),
    path('about/',about,name='about-page'),
    path('contact/',contact,name='contact-page'),
    path('signup/',signup_page,name='signup-page'),
    path('<slug:slug>/',post_detail,name='post_detail-page'),
]