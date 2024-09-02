from django.shortcuts import render
from .utils import format_date
from .forms import StretchingWorkoutForm, StrengthWorkoutForm
from .stretching import stretch_choice
from .strength import strength_choice

# Create your views here.


date = format_date()
def random_workout(request):
    return render(request, 'random_workout/random_workout.html', {
        'formatted_date': date
    })

def stretch_view(request):

    if request.method == 'POST':
        after_message = "Hold each pose for 30 seconds"
        form = StretchingWorkoutForm(request.POST)
        if form.is_valid():
            workout_type = form.cleaned_data['workout_type']
            if workout_type == 'gentle':
                workout = stretch_choice(1)
            elif workout_type == 'challenging':
                workout = stretch_choice(2)
            else:
                workout = stretch_choice(3)

            
            return render(request, 'random_workout/stretch.html', {
                'formatted_date': date,
                'workout_today': workout,
                'after_message': after_message,
            })
    else:
        return render(request, 'random_workout/stretch.html', {
            'formatted_date': date
        })


def strength_view(request):
    if request.method == "POST":
        form = StrengthWorkoutForm(request.POST)
        if form.is_valid():
            workout_type = form.cleaned_data['workout_type']
            if workout_type == "beginner":
                workout = strength_choice(1)
            elif workout_type == "intermediate":
                workout = strength_choice(2)
            else:
                workout = strength_choice(3)

            return render(request, 'random_workout/strength.html', {
                'formatted_date': date,
                'workout_today': workout
            })
    else:
        return render(request, 'random_workout/strength.html', {
            'formatted_date': date
        })