from table import Table
from table.columns import Column
from .player import Player


class PlayerTable(Table):
    FullName = Column(field='FullName', header="FullName")
    NationalTeam = Column(field='Team', header="Team")
    Competition = Column(field='Competition', header="Competition")
    Position = Column(field='Position', header="Position")

    class Meta:
        model = Player


        