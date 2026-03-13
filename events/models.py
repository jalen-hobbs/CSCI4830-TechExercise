from django.db import models
from django.core.exceptions import ValidationError
from django.urls import reverse
from django.utils import timezone


class Event(models.Model):
    CATEGORY_CHOICES = [
        ("school", "School"),
        ("work", "Work"),
        ("personal", "Personal"),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    location = models.CharField(max_length=200, blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default="personal")
    is_cancelled = models.BooleanField(default=False, verbose_name="Cancel Event")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["start_datetime"]

    def __str__(self):
        return self.title

    def clean(self):
        super().clean()
        if self.end_datetime <= self.start_datetime:
            raise ValidationError("End date/time must be after start date/time.")

    @property
    def status(self):
        now = timezone.now()
        if self.is_cancelled:
            return "Cancelled"
        if now < self.start_datetime:
            return "Upcoming"
        if self.start_datetime <= now <= self.end_datetime:
            return "In Progress"
        return "Completed"

    def get_absolute_url(self):
        return reverse("event_detail", kwargs={"pk": self.pk})