from django import forms
from .models import Event


class EventForm(forms.ModelForm):
    start_datetime = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={"type": "datetime-local"}, input_formats=["%Y-%m-%dT%H:%M"])
    )
    end_datetime = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={"type": "datetime-local"}, input_formats=["%Y-%m-%dT%H:%M"])
    )

    class Meta:
        model = Event
        fields = [
            "title",
            "description",
            "start_datetime",
            "end_datetime",
            "location",
            "category",
            "is_cancelled",
        ]