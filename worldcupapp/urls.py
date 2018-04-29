
from django.conf.urls import url,include
from . import views




urlpatterns = [
    #url(r'',views.deleteAllBlankName,name="delete"),
    url(r'^$',views.pTable,name="player_table"),
    url(r'^listing/offset/(?P<offset>\d+)/limit/(?P<limit>\d+)/', views.playerRange, name="player_list"),
    url(r'^api/create/$',views.PlayerAPIView.as_view(),name="player-create"),
    url(r'^api/player/(?P<pk>\d+)/$',views.PlayerRUDView.as_view(),name="player-rud")
]