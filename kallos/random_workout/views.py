from django.shortcuts import render
from .utils import format_date

# Create your views here.


date = format_date()
def random_workout(request):
    return render(request, 'random_workout/random_workout.html', {
        'formatted_date': date
    })

def stretch_view(request):
    return render(request, 'random_workout/stretch.html', {
        'formatted_date': date
    })