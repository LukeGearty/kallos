from django import forms

class StretchingWorkoutForm(forms.Form):
    WORKOUT_CHOICES = [
        ('gentle', 'Gentle Stretching'),
        ('challenging', 'Challenging Stretching'),
        ('intense', 'Intense Stretching'),
    ]

    workout_type = forms.ChoiceField(choices=WORKOUT_CHOICES, label="Choose Workout Type")