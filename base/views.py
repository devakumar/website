from django.shortcuts import render
from django.utils import timezone
from django.views import generic

from .models import Event

# Create your views here.
def home(request):
    # Homepage of the base app - Core of website
    upcoming = Event.objects.filter(date__gte=timezone.now()).order_by('-date').reverse()
    return render(request, 'home.html', {'upcoming':upcoming})

class IndexView(generic.ListView):
    template_name = 'base/events.html'
    context_object_name = 'all_events'

    def get_queryset(self):
        """ Return the last five published questions """
        return Event.objects.all().order_by('-date').order_by('-date').reverse()

class DetailView(generic.DetailView):
    model = Event
    template_name = 'base/event_detail.html'

    def get_queryset(self):
        """ Upcoming Events """
        return Event.objects.filter(date__gte=timezone.now()).order_by('-date').reverse()

class PastView(generic.DetailView):
    model = Event
    template_name = 'base/event_detail.html'

    def get_queryset(self):
        """ Upcoming Events """
        return Event.objects.filter(date__lte=timezone.now())