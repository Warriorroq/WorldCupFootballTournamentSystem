import FootballObj.Team
import FootballObj.Group
import FootballObj.Round16
import FootballObj.QuarterFinal
import FootballObj.SemiFinal
import FootballObj.Final


teams = [
    FootballObj.Team.Team("Qatar"),
    FootballObj.Team.Team("Brazil"),
    FootballObj.Team.Team("Belgium"),
    FootballObj.Team.Team("France"),
    FootballObj.Team.Team("Argentina"),
    FootballObj.Team.Team("England"),
    FootballObj.Team.Team("Spain"),
    FootballObj.Team.Team("Croatia"),
    FootballObj.Team.Team("Portugal"),
    FootballObj.Team.Team("Mexico"),
    FootballObj.Team.Team("Netherlands"),
    FootballObj.Team.Team("Denmark"),
    FootballObj.Team.Team("Germany"),
    FootballObj.Team.Team("Uruguay"),
    FootballObj.Team.Team("Switzerland"),
    FootballObj.Team.Team("United States"),
    FootballObj.Team.Team("Croatia"),
    FootballObj.Team.Team("Senegal"),
    FootballObj.Team.Team("Iran"),
    FootballObj.Team.Team("Japan"),
    FootballObj.Team.Team("Morocco"),
    FootballObj.Team.Team("Serbia"),
    FootballObj.Team.Team("Poland"),
    FootballObj.Team.Team("South Korea"),
    FootballObj.Team.Team("Cameroon"),
    FootballObj.Team.Team("Tunisia"),
    FootballObj.Team.Team("Canada"),
    FootballObj.Team.Team("Ecuador"),
    FootballObj.Team.Team("Saudi Arabia"),
    FootballObj.Team.Team("Ghana"),
    FootballObj.Team.Team("Wales"),
    FootballObj.Team.Team("Costa Rica"),
    FootballObj.Team.Team("Australia")
]

# Реализация, при которой пользователь вводит все переменные вручную
# while True:
#     user_county = input("Which county would you like to add? (Enter 'q' to quit)")
#     if user_county == 'q':
#         break
#     teams.append(FootballObj.Team.Team(user_county))
#
#

groups = [
    FootballObj.Group.Group("Group A", teams[:4]),
    FootballObj.Group.Group("Group B", teams[4:8]),
    FootballObj.Group.Group("Group C", teams[8:12]),
    FootballObj.Group.Group("Group D", teams[12:16]),
    FootballObj.Group.Group("Group F", teams[20:24]),
    FootballObj.Group.Group("Group G", teams[24:28]),
    FootballObj.Group.Group("Group H", teams[28:])
]

round16 = FootballObj.Round16.Round16()

qfinal = FootballObj.QuarterFinal.QFinal()

sfinal = FootballObj.SemiFinal.SFinal()

final = FootballObj.Final.Final()


