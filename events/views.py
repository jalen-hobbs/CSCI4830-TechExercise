from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
import calendar
from datetime import datetime, timedelta, date
from django.utils import timezone
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

class EventListView(ListView):
    model = Event
    template_name = "events/event_list.html"
    context_object_name = "events"

    def get_queryset(self):
        queryset = Event.objects.all().order_by("start_datetime")

        category = self.request.GET.get("category")
        search = self.request.GET.get("q")

        if category:
            queryset = queryset.filter(category=category)

        if search:
            queryset = queryset.filter(title__icontains=search)

        return queryset


class DayView(TemplateView):
    template_name = "events/day_view.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        year = int(self.kwargs["year"])
        month = int(self.kwargs["month"])
        day = int(self.kwargs["day"])
        selected_date = date(year, month, day)

        events = Event.objects.filter(
            start_datetime__date=selected_date
        ).order_by("start_datetime")

        context["selected_date"] = selected_date
        context["events"] = events
        return context


class WeekView(TemplateView):
    template_name = "events/week_view.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        year = int(self.kwargs["year"])
        month = int(self.kwargs["month"])
        day = int(self.kwargs["day"])
        selected_date = date(year, month, day)

        start_of_week = selected_date - timedelta(days=selected_date.weekday())
        end_of_week = start_of_week + timedelta(days=6)

        events = Event.objects.filter(
            start_datetime__date__range=[start_of_week, end_of_week]
        ).order_by("start_datetime")

        days = []
        for i in range(7):
            current_day = start_of_week + timedelta(days=i)
            day_events = [event for event in events if timezone.localtime(event.start_datetime).date() == current_day]
            days.append({
                "date": current_day,
                "events": day_events,
            })

        context["start_of_week"] = start_of_week
        context["end_of_week"] = end_of_week
        context["days"] = days
        return context


class MonthView(TemplateView):
    template_name = "events/month_view.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        year = int(self.kwargs["year"])
        month = int(self.kwargs["month"])

        cal = calendar.Calendar(firstweekday=6)  # Sunday start
        month_days = cal.monthdatescalendar(year, month)

        start_date = month_days[0][0]
        end_date = month_days[-1][-1]

        events = Event.objects.filter(
            start_datetime__date__range=[start_date, end_date]
        ).order_by("start_datetime")

        weeks = []
        for week in month_days:
            week_data = []
            for day_obj in week:
                day_events = [event for event in events if timezone.localtime(event.start_datetime).date() == day_obj]
                week_data.append({
                    "date": day_obj,
                    "in_month": day_obj.month == month,
                    "events": day_events,
                })
            weeks.append(week_data)

        context["year"] = year
        context["month"] = month
        context["month_name"] = calendar.month_name[month]
        context["weeks"] = weeks
        return context