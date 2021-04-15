from django.core.exceptions import ValidationError


class ExtendedValidationError(ValidationError):
    pass
