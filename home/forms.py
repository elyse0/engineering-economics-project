from django import forms
from django.forms.widgets import NumberInput


class InteresForm (forms.Form):

    interes = forms.FloatField(label='Interés', min_value= 0, max_value = 1,
                               widget=NumberInput(attrs={'id': 'form_homework', 'step': "0.01"}))

class ValorPresenteForm (forms.Form):

    valorPresente = forms.FloatField(label='Valor Presente', min_value= 0, max_value = 10000000)

class ValorFuturoForm (forms.Form):

    valorFuturo = forms.FloatField(label='Valor Futuro', min_value= 0, max_value = 10000000)

class NumeroPeriodosForm (forms.Form):

    numeroPeriodos = forms.IntegerField(label='Numero de periodos', min_value= 0, max_value = 1000000,
                               widget=NumberInput(attrs={'id': 'form_homework', 'step': "1"}))

class TipoPeriodosForm (forms.Form):

    tipoPeriodos = forms.ChoiceField(label='Tipo de periodo', choices=[('Años', 'Años'), ('Meses', 'Meses'),
                                                                         ('Dias', 'Dias')])

class ValorSerieForm(forms.Form):

    valorSerie = forms.FloatField(label='Valor de la serie:', min_value= 0, max_value = 10000000)