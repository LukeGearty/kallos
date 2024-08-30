import random


def gentle_stretch():
    stretches = ['Downward Facing Dog', 'Cat Cow', 'Standing Calf Raise', 'Shoulder Rolls', 'Shoulder Reaches']
    return random.choice(stretches)


def intermediate_stretches():
    stretches = ['Standing Forward Fold', 'Lying Forward Fold','Deep Squat', 'Deep Lunges', 'Bridge', 'Supine Spinal Twists', 'Pigeon Pose']
    return random.choice(stretches)


def advanced_stretch():
    stretches = ['Origami Stretch', 'Twisting Pec Stretch', 'Forward Fold', 'Triangle Stretch', 'Heart Opener', 'Lunge with Spinal Twist', 'Piriformis Stretch']
    return random.choice(stretches)


def generate_stretch_workout(stretch_function):
    stretches = []
    for i in range(3):
        current_stretch = stretch_function()
        while current_stretch in stretches:
            current_stretch = stretch_function()
        stretches.append(current_stretch)
    return stretches


