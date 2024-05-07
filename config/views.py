from rest_framework import generics
from .models import AboutUs, Contacts, Feedback
from .serializers import AboutUsSerializer, ContactsSerializer, FeedbackSerializer
class AboutUsAdd(generics.CreateAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer
class AboutUsUpdate(generics.UpdateAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer
class AboutUsDelete(generics.DestroyAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer
#ContactViews
class ContactsAdd(generics.CreateAPIView):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer
class ContactsUpdate(generics.UpdateAPIView):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer
class ContactsDelete(generics.DestroyAPIView):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer
class FeedbackCreate(generics.CreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

class FeedbackList(generics.ListAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer