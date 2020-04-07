from rest_framework import serializers

from park.models import Park

class ParkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Park
        fields = '__all__'
        #exclude = []
