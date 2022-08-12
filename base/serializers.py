from rest_framework import serializers
from .models import Glucose
# from drf_extra_fields.fields import Base64ImageField

class GlucoseSerializer(serializers.ModelSerializer):
    # image_object= Base64ImageField(
    #     max_length=None, use_url=True,
    # )

    class Meta:
        model = Glucose
        fields = '__all__'