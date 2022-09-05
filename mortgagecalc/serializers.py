from rest_framework import serializers
from .models import BanksBase


class BankSerializer(serializers.Serializer):
    payment = serializers.IntegerField(default=None)
    bank_name = serializers.CharField(max_length=20)
    term_min = serializers.IntegerField()
    term_max = serializers.IntegerField()
    rate_min = serializers.FloatField()
    rate_max = serializers.FloatField()
    payment_min = serializers.IntegerField()
    payment_max = serializers.IntegerField()

    def create(self, validated_data):
        return BanksBase.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.payment = validated_data.get('payment', instance.payment)
        instance.bank_name = validated_data.get('bank_name', instance.bank_name)
        instance.term_min = validated_data.get('term_min', instance.term_min)
        instance.term_max = validated_data.get('term_max', instance.term_max)
        instance.rate_min = validated_data.get('rate_min', instance.rate_min)
        instance.rate_max = validated_data.get('rate_max', instance.rate_max)
        instance.payment_min = validated_data.get('payment_min', instance.payment_min)
        instance.payment_max = validated_data.get('payment_max', instance.payment_max)
        instance.save()
        return instance