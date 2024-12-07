from django.urls import path
from . import views
from .views import feedback_view, contact_view, success_view, submit_feedback, Messagesuccess_view

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('events/', views.events, name='events'),
    path('booking/', views.booking, name='booking'),
    path('contact/', views.contact_view, name='contact'),
path('bookingsuccess/', views.bookingsuccess, name='bookingsuccess'),
    path('feedback/', feedback_view, name='feedback'),
    path('success/', success_view, name='success'),\
    path('Message_success/', views.Messagesuccess_view, name='Message_success'),
    path('submit_feedback/', views.submit_feedback, name='submit_feedback'),
path('Event1/', views.event1_description, name='event1_description'),
path('Event2/', views.event2_description, name='event2_description'),
path('Event3/', views.event3_description, name='event3_description'),
path('Event4/', views.event4_description, name='event4_description'),
path('Event5/', views.event5_description, name='event5_description'),
path('chatbot/', views.chatbot, name='chatbot'),
]
