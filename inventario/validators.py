from django.core.exceptions import ValidationError

def validar_celular(value):
    if len(str(value)) <= 7:
        raise ValidationError(
            '%(value)s no es un celular, debe tener 8 digitos',
            params={'value': value}
        )

def validar_pais(value):
    if any(chr.isdigit() for chr in value):
        raise ValidationError(
            '%(value)s no es un pais, no debe tener numeros',
            params={'value': value}
        )