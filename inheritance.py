# John Zaiss (GitHub id jzaiss1)
# SWDV 630: OBJECT-ORIENTATED CODING 1W 20/SP1
# Week 3 Assignment - Inheritance

class Player:
    def __init__(self, name, team, position):
        self.name = name
        self.team = team
        self.position = position

    def changeTeam(self, team):
        self.team = team

    def printStatistica(self):
         raise NotImplementedError()

    def __str__(self):
        print('something')
        
class Statistics:
    def __init__(self, ):

class Pitcher:
    def __init__(self, ):
        Player.__init__(self, )

class Outfielder:
    def __init__(self, ):
        Player.__init__(self, )

class Infielder:
    def __init__(self, ):
        Player.__init__(self, )

class Catcher:
    def __init__(self, ):
        Player.__init__(self, )