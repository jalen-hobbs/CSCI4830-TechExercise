from django.utils import timezone

def today_date(request):
    return {
        "today": timezone.localdate()
    }