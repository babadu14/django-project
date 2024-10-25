from django.urls import path
from .views import main_page_view, students_page_view

urlpatterns =[
    path('main/', main_page_view),
    path('students/', students_page_view)
]