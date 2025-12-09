from django import forms
import math

OPERATIONS = (
    ('add', '+'),
    ('sub', '-'),
    ('mul', '*'),
    ('div', '/'),
    ('pow', '^'),
    ('sqrt', '√'),
)

class CalculatorForm(forms.Form):
    a = forms.FloatField(label='Число A', required=True)
    b = forms.FloatField(label='Число B', required=False)
    operation = forms.ChoiceField(label='Операция', choices=OPERATIONS)

    def clean(self):
        cleaned_data = super().clean()
        op = cleaned_data.get('operation')
        b = cleaned_data.get('b')

        if op != 'sqrt' and b is None:
            raise forms.ValidationError("Число B обязательно для этой операции.")
        if op == 'div' and b == 0:
            raise forms.ValidationError("Деление на ноль невозможно.")
        if op == 'sqrt' and cleaned_data.get('a') < 0:
            raise forms.ValidationError("Невозможно вычислить квадратный корень из отрицательного числа.")
        return cleaned_data
