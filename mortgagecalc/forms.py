from django import forms


class CalcForm(forms.Form):
    estate_price = forms.IntegerField()
    first_pay = forms.IntegerField()
