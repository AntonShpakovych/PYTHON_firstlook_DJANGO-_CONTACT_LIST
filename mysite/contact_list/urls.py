from django.urls import path
from django.urls.conf import include

from contact_list.views import ContactListView


urlpatterns = [
    path('', ContactListView.as_view(), name='contact-list')
]
