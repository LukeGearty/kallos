from django.shortcuts import render

# Create your views here.

def random_workout(request):
    return render(request, 'random_workout/random_workout.html')