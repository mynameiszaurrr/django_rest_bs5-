from datetime import datetime
from django.forms import model_to_dict
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import BanksBase
from .forms import CalcForm
from .serializers import BankSerializer

now = datetime.now()


def index(request):
    banks = BanksBase.objects.all()
    banks_count = banks.values().count()
    calc_form = CalcForm()
    data = {
        'city': "Москве", # список городов, где можно проводить поиск
        'year': now.year,
        'date': now.strftime("%d.%m.%Y"),
        'calc_form': calc_form,
        'banks': banks,
        "banks_count": banks_count,
    }
    return render(request, 'mortgagecalc/index.html', context=data)


def index_search(request):
    if request.method == 'POST':
        banks = BanksBase.objects.all()
        calc_form = CalcForm()
        get_price = request.POST.get('price')
        get_rate = request.POST.get('rate')
        price = BanksBase.objects.filter(payment_min__lt=int(get_price), rate_min__lt=int(get_rate))
        banks_count = BanksBase.objects.filter(payment_min__lt=int(request.POST.get('price')), rate_min__lt=int(request.POST.get('rate'))).values().count()
        # pay_in_mouth =
        data = {
            'city': "Москве", # список городов, где можно проводить поиск
            'year': now.year,
            'date': now.strftime("%d.%m.%Y"),
            'calc_form': calc_form,
            'banks': banks,
            "banks_count": banks_count,
            'price': price
        }
        return render(request, 'mortgagecalc/index_search.html', context=data)
    else:
        return HttpResponseRedirect('http://127.0.0.1:8000/')


class BanksAPIWiew(APIView):
    def get(self, request):
        banks = BanksBase.objects.all()
        return Response(BankSerializer(banks, many=True).data)

    def post(self, request):
        selializer = BankSerializer(data=request.data)
        selializer.is_valid(raise_exception=True)
        selializer.save()
        return Response(selializer.data)

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': "Ключа pk нет в запросе"})
        try:
            instance = BanksBase.objects.get(pk=pk)
        except:
            return Response({'error': "Метод изменить не применим"})

        serializer = BankSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': "Ключа pk нет в запросе"})
        try:
            instance = BanksBase.objects.get(pk=pk)
        except:
            return Response({'error': "Ключа pk нет в БД"})
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
