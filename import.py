import json
from worldcupapp.models import Player


with open('playerdata.json') as data_file:
    data = json.load(data_file)

for player in data:
    obj=player
    if(('FullName' in obj)!=""):
        p = Player(Competition=obj['Competition'],Year=obj['Year'],Team=obj['Team'],Position=obj['Position'], FullName=obj['FullName'], Club=obj['Club'],ClubCountry=obj['ClubCountry'],IsCaptain=obj['IsCaptain'])
    p.save()


 

