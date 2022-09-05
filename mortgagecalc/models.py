from django.db import models


class InputData(models.Model):
    home_price = models.IntegerField(max_length=20, help_text='Введите стоимость недвижимости в рублях без копеек',
                                     verbose_name='Стоимость объекта недвижимости')
    first_pay = models.IntegerField(max_length=20, help_text='Введите первоночальный взнос в рублях без копеек',
                                    verbose_name='Первоночальный взнос')
    time_of_pay = models.IntegerField(max_length=3, help_text='Введите срок ипотеки', verbose_name='Срок ипотеки')


class BanksBase(models.Model):
    payment = models.IntegerField(max_length=20, null=True, verbose_name='Платеж в месяц')
    bank_name = models.CharField(max_length=20, verbose_name='Название банка')
    term_min = models.IntegerField(max_length=3, verbose_name='Срок ипотеки, ОТ')
    term_max = models.IntegerField(max_length=3, verbose_name='Срок ипотеки, ДО')
    rate_min = models.FloatField(max_length=5, verbose_name='Ставка, ОТ')
    rate_max = models.FloatField(max_length=5, verbose_name='Ставка, ДО')
    payment_min = models.IntegerField(max_length=20, verbose_name='Ставка кредита, ОТ')
    payment_max = models.IntegerField(max_length=20, verbose_name='Ставка кредита, ДО')

    def __str__(self):
        return self.bank_name

