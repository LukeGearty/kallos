from django import forms


class StretchingWorkoutForm(forms.Form):
    WORKOUT_CHOICES = [
        ('gentle', 'Gentle Stretching'),
        ('challenging', 'Challenging Stretching'),
        ('intense', 'Intense Stretching'),
    ]

    workout_type = forms.ChoiceField(choices=WORKOUT_CHOICES, label="Choose Workout Type")


class StrengthWorkoutForm(forms.Form):
    WORKOUT_CHOICE = [
        ('beginner', 'Beginner Workout'),
        ('intermediate', 'Intermediate Workout'),
        ('advanced', 'Advanced Workout')
    ]

    workout_type = forms.ChoiceField(choices=WORKOUT_CHOICE, label="Choose Workout Type")


class CardioWorkoutForm(forms.Form):
    WORKOUT_CHOICE = [
        ('light', 'Light Intensity'),
        ('medium', 'Medium Intensity'),
        ('high', 'High Intensity')
    ]
    workout_type = forms.ChoiceField(choices=WORKOUT_CHOICE, label="Choose Workout Type")