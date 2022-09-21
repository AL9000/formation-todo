from django.core.exceptions import ValidationError
from django.utils import timezone


def datetime_must_be_in_futur(dt):
    if timezone.now() > dt:
        raise ValidationError(
            "Please enter a date in the futur",
            params={'date': dt},
        )
