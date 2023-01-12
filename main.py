import FootballObj.Team
import FootballObj.Group
import FootballObj.Round16
import FootballObj.QuarterFinal
import FootballObj.SemiFinal
import FootballObj.Final


teams = [32]

#Реализация, при которой пользователь вводит все переменные вручную
# while True:
#     user_county = input("Which county would you like to add? (Enter 'q' to quit)")
#     if user_county == 'q':
#         break
#     teams.append(FootballObj.Team.Team(user_county))
for i in teams:
    user_country = input("Which county would you like to add? (Enter 'q' to quit) ")
    if user_country == 'q':
        break
    teams.append((FootballObj.Team.Team(user_country)))


groups = [
    FootballObj.Group.Group("Group A", teams[:4]),
    FootballObj.Group.Group("Group B", teams[4:8]),
    FootballObj.Group.Group("Group C", teams[8:12]),
    FootballObj.Group.Group("Group D", teams[12:16]),
    FootballObj.Group.Group("Group F", teams[20:24]),
    FootballObj.Group.Group("Group G", teams[24:28]),
    FootballObj.Group.Group("Group H", teams[28:32])
]

round16 = FootballObj.Round16.Round16()

qfinal = FootballObj.QuarterFinal.QFinal()

sfinal = FootballObj.SemiFinal.SFinal()

final = FootballObj.Final.Final()


