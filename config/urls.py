from django.urls import path
from . import views

urlpatterns = [
    path('aboutus/add/', views.AboutUsAdd.as_view(), name='about_us-add'),
    path('aboutus/<int:pk>/', views.AboutUsUpdate.as_view(), name='about_us-update'),
    path('aboutus/<int:pk>/', views.AboutUsDelete.as_view(), name='about_us-delete'),
    path('contacts/add/', views.ContactsAdd.as_view(), name='contacts-add'),
    path('contacts/<int:pk>/update/', views.ContactsUpdate.as_view(), name='contacts-update'),
    path('contacts/<int:pk>/delete/', views.ContactsDelete.as_view(), name='contacts-delete'),
    path('Feedback/create/', views.FeedbackCreate.as_view(), name='Feedback-create'),
    path('Feedback/list/', views.FeedbackList.as_view(), name='Feedback-list'),
]
