from django.urls import path
from .views import (
    EventListView,
    EventDetailView,
    EventCreateView,
    EventUpdateView,
    EventDeleteView,
    DayView,
    WeekView,
    MonthView,
)

urlpatterns = [
    path("", EventListView.as_view(), name="event_list"),
    path("event/<int:pk>/", EventDetailView.as_view(), name="event_detail"),
    path("event/add/", EventCreateView.as_view(), name="event_create"),
    path("event/<int:pk>/edit/", EventUpdateView.as_view(), name="event_edit"),
    path("event/<int:pk>/delete/", EventDeleteView.as_view(), name="event_delete"),

    path("calendar/day/<int:year>/<int:month>/<int:day>/", DayView.as_view(), name="day_view"),
    path("calendar/week/<int:year>/<int:month>/<int:day>/", WeekView.as_view(), name="week_view"),
    path("calendar/month/<int:year>/<int:month>/", MonthView.as_view(), name="month_view"),
]