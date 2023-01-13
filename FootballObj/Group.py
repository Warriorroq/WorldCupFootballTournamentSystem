class Group:
    def __init__(self, name, teams=None):
        self.name = name
        self.teams = teams or []

    def getTwoBestTeams(self):
        return sorted(self.teams, key=lambda x: x.goals, reverse=True)[:2]

    def __str__(self):
        return f"\n{self.name} {[str(i) for i in self.teams]}"