from figgis import ValidationError


def Length(min=None, max=None):
    """min <= len(value) <= max"""

    def validator(value, min=min, max=max):
        if min is not None and len(value) < min:
            raise ValidationError('Length is less than {0}'.format(min))

        if max is not None and len(value) > max:
            raise ValidationError('Length is greater than {0}'.format(max))

        return True

    return validator


def Range(min=None, max=None):
    """min <= value <= max"""

    def validator(value, min=min, max=max):
        if min is not None and value < min:
            raise ValidationError('Value is less than {0}'.format(min))

        if max is not None and value > max:
            raise ValidationError('Value is greater than {0}'.format(max))

        return True

    return validator
