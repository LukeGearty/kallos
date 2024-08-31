from django.shortcuts import render
from .utils import format_date
from .forms import StretchingWorkoutForm
from .stretching import stretch_choice

# Create your views here.


date = format_date()
def random_workout(request):
    return render(request, 'random_workout/random_workout.html', {
        'formatted_date': date
    })

def stretch_view(request):

    if request.method == 'POST':
        form = StretchingWorkoutForm(request.POST)
        if form.is_valid():
            workout_type = form.cleaned_data['workout_type']
            if workout_type == 'gentle':
                workout = stretch_choice(1)
            elif workout_type == 'intermediate':
                workout = stretch_choice(2)
            else:
                workout = stretch_choice(3)

            
            return render(request, 'random_workout/stretch.html', {
                'formatted_date': date,
                'workout_today': workout
            })
    else:
        return render(request, 'random_workout/stretch.html', {
            'formatted_date': date
        })