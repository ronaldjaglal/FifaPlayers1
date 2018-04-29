

from django.shortcuts import render
from rest_framework import viewsets
from .players import Player 
from .players import PlayerTable
from .players import playerSerializer
from rest_framework import generics
'''
def deleteAllPlayer(request):
    Player.objects.all().delete()

'''

'''
def deleteAllBlankName(request):
    Player.objects.filter(FullName='').delete()

'''

def pTable(request):
    player = PlayerTable(Player.objects.all())
    return render(request, 'datatable.html', {'player':player})


def playerRange(request, offset, limit):
    offset = int(offset)
    limit = int(limit)
    print(limit)
    player = Player.objects.all()[offset:limit]
    return render(request, 'listing.html', {'player':player})



class PlayerRUDView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field='pk'
    queryset= Player.objects.all()
    serializer_class=playerSerializer

class PlayerAPIView(generics.CreateAPIView):
    lookup_field='pk'
    queryset= Player.objects.all()
    serializer_class=playerSerializer

    def perform_create(self,serializer):
        serializer.save(user=self.request.user)


    