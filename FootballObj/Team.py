class Team:
    def __init__(self, country, goals=0):
        self.country = country
        self.goals = goals

    def __str__(self):
        return f"{self.country},{self.goals}"


