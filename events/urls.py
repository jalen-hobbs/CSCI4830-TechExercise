from django.urls import path
from .views import (
    EventListView,
    EventDetailView,
    EventCreateView,
    EventUpdateView,
    EventDeleteView,
)

urlpatterns = [
    path("", EventListView.as_view(), name="event_list"),
    path("event/<int:pk>/", EventDetailView.as_view(), name="event_detail"),
    path("event/add/", EventCreateView.as_view(), name="event_create"),
    path("event/<int:pk>/edit/", EventUpdateView.as_view(), name="event_edit"),
    path("event/<int:pk>/delete/", EventDeleteView.as_view(), name="event_delete"),
]