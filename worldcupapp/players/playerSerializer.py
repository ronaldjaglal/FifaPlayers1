from rest_framework import serializers
from .player import Player

class playerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Player
        fields=[
            'pk',
            'user',
            'Competition',
            'Year',
            'Team',
            'Number',
            'Position',
            'FullName',
            'Club',
            'ClubCountry',
            'created',
            'IsCaptain',
        ]
        read_only_fields=['user']


        
     