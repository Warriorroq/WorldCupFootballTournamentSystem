class Match:
    def __init__(self, teams):
        self.teams = teams or [] * 2
        for i in self.teams:
            i.goals = 0

    def getWinner(self):
        if self.teams[0].goals > self.teams[1].goals:
            return self.teams[0]
        return self.teams[1]

    def convertToSendableData(self):
        return [self.teams[0].country, self.teams[1].country]

    def __str__(self):
        return f"match: {self.teams[0].country} vs {self.teams[1].country}"
