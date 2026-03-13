from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Event
from .forms import EventForm


class EventListView(ListView):
    model = Event
    template_name = "events/event_list.html"
    context_object_name = "events"


class EventDetailView(DetailView):
    model = Event
    template_name = "events/event_detail.html"
    context_object_name = "event"


class EventCreateView(CreateView):
    model = Event
    form_class = EventForm
    template_name = "events/event_form.html"


class EventUpdateView(UpdateView):
    model = Event
    form_class = EventForm
    template_name = "events/event_form.html"


class EventDeleteView(DeleteView):
    model = Event
    template_name = "events/event_confirm_delete.html"
    success_url = reverse_lazy("event_list")