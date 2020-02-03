# John Zaiss (GitHub id jzaiss1)
# SWDV 630: OBJECT-ORIENTATED CODING 1W 20/SP1
# Week 3 Assignment - Inheritance

# This is the base class that can be used for multiple sports
class Player:

    def __init__(self, name, team, position):
        self.name = name
        self.team = team
        self.position = position

    def changeTeam(self, team):
        self.team = team

    def getStatLine(self):
        raise NotImplementedError()

    def addStatLine(self):
        raise NotImplementedError()

    def validated(self):
        raise NotImplementedError

    def firstName(self):
        return self.name.split(' ')[0]

    def __str__(self):
        return 'something'

# Sub-classes for players, each sub-class processes stats differently 
class Pitcher:
    def __init__(self, name, team, position):
        Player.__init__(self, name, team, position)

    def addStatLine(self, stat1, stat2):
        self.wins = stat1
        self.losses = stat2

    def validated(self):
        if (self.wins + self.losses) > 0:
            return True

    def getStatLine(self):
        if self.validated():
            winPct = self.wins / (self.wins + self.losses)
            return 'Winning percentage is {:2.0f}%\n'.format(winPct*100)
        else:
            return '{} has no decisions\n'.format(Player.firstName(self))

    def __str__(self):
        return '{} {} {}\n'.format(self.name, self.team, self.position) + self.getStatLine()

class Outfielder:
    def __init__(self, name, team, position):
        Player.__init__(self, name, team, position)

    def addStatLine(self, stat1, stat2):
        self.gamesStarted = stat1
        self.gamesFinished = stat2

    def validated(self):
        if self.gamesStarted > 0:
            return True

    def getStatLine(self):
        if self.validated():
            finishPct = self.gamesFinished / self.gamesStarted
            return '{} finishes {:2.0f}% of the games started\n'.format(Player.firstName(self), finishPct*100)
        else:
            return '{} has not started any games.\n'.format(Player.firstName(self))

    def __str__(self):
        return '{} {} {}\n'.format(self.name, self.team, self.position) + self.getStatLine()

class Infielder:
    def __init__(self, name, team, position):
        Player.__init__(self, name, team, position)

    def addStatLine(self, stat1, stat2):
        self.chances = stat1
        self.errors = stat2 

    def validated(self):
        if self.chances > 0:
            return True

    def getStatLine(self):
        if self.validated():
            errorPct = self.errors / self.chances
            return '{} makes and error {:2.1f}% of the time he fields a ball\n'.format(Player.firstName(self), errorPct*100)
        else:
            return '{} has not had any chances.\n'.format(Player.firstName(self))

    def __str__(self):
        return '{} {} {}\n'.format(self.name, self.team, self.position) + self.getStatLine()

class Catcher:
    def __init__(self, name, team, position):
        Player.__init__(self, name, team, position)

    def addStatLine(self, stat1, stat2):
        self.attempts = stat1
        self.caught = stat2

    def validated(self):
        if self.attempts > 0:
            return True

    def getStatLine(self):
        if self.validated():
            caughtPct = self.caught / self.attempts
            return 'Percent of runners caught stealing is {:2.0f}%\n'.format(caughtPct*100)
        else:
            return 'No stolen base attempts against {}\n'.format(Player.firstName(self))

    def __str__(self):
        return '{} {} {}\n'.format(self.name, self.team, self.position) + self.getStatLine()



def testCases():
    # One test case for each sub-class with valid data
    pitcher = Pitcher('Jack Flaherty', 'STL', 'RHP')
    pitcher.addStatLine(11, 8)
    print(pitcher)

    outfielder = Outfielder('Harrison Bader', 'STL', 'CF')
    outfielder.addStatLine(95, 87)
    print(outfielder)

    infielder = Infielder('Kolten Wong', 'STL', '2B')
    infielder.addStatLine(671, 9)
    print(infielder)

    catcher = Catcher('Yadier Molina', 'STL', 'C')
    catcher.addStatLine(30, 8)
    print(catcher)

    # One test case for each sub-class catching divide by zero errors
    pitcher = Pitcher('Jack Flaherty', 'STL', 'RHP')
    pitcher.addStatLine(0, 0)
    print(pitcher)

    outfielder = Outfielder('Harrison Bader', 'STL', 'CF')
    outfielder.addStatLine(0, 10)
    print(outfielder)

    infielder = Infielder('Kolten Wong', 'STL', '2B')
    infielder.addStatLine(0, 0)
    print(infielder)

    catcher = Catcher('Yadier Molina', 'STL', 'C')
    catcher.addStatLine(0, 0)
    print(catcher)    

def main():
    testCases()

main()






