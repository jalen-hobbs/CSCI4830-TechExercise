from django.db import models
from django.core.exceptions import ValidationError
from django.urls import reverse

class Event(models.Model):
    CATEGORY_CHOICES = [
        ('school', 'School'),
        ('work', 'Work'),
        ('personal', 'Personal'),
    ]

    STATUS_CHOICES = [
        ('upcoming', 'Upcoming'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    location = models.CharField(max_length=200, blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='personal')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='upcoming')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["start_datetime"]

    def __str__(self):
        return self.title

    def clean(self):
        super().clean()
        if self.end_datetime <= self.start_datetime:
            raise ValidationError("End date/time must be after start date/time.")

    def get_absolute_url(self):
        return reverse("event_detail", kwargs={"pk": self.pk})