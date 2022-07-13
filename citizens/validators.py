from django.core.exceptions import ValidationError


def validate_interval(value):
    if value < 0 or value > 120:
        raise ValidationError(('%(value)s должно быть в диапазоне [0, 120]'), params={'value': value},)