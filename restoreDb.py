from datetime import date
from tic import data as db

oldHistory=[
    {
        "played_date":date(year=2017,month=3,day=3),
        "player1":"A1",
        "player2":"A2",
        "win_player":1
    },
     {
        "played_date":date(year=2017,month=3,day=3),
        "player1":"A1",
        "player2":"A2",
        "win_player":1
    },
     {
        "played_date":date(year=2017,month=3,day=3),
        "player1":"A1",
        "player2":"A2",
        "win_player":0
    },
     {
        "played_date":date(year=2017,month=3,day=3),
        "player1":"A1",
        "player2":"A2",
        "win_player":0
    },
     {
        "played_date":date(year=2017,month=3,day=3),
        "player1":"A1",
        "player2":"A2",
        "win_player":2
    },
     {
        "played_date":date(year=2017,month=3,day=3),
        "player1":"A1",
        "player2":"A2",
        "win_player":1
    }


]
def importDb():
    db.restoreDb(oldHistory)


if __name__=="__main__":
    importDb()
