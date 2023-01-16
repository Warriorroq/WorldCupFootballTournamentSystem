from FootballObj.Team import *


class Group:
    def __init__(self, teams=None):
        self.teams = [Team(i[0], int(i[1])) for i in teams]

    def getTwoBestTeams(self):
        return sorted(self.teams, key=lambda x: x.goals, reverse=True)[:2]

    def __str__(self):
        return f"\nGroup: {[str(i) for i in self.teams]}"