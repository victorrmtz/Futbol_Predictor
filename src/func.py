def goles(season2223_1):
    teams = {}
    for i in season2223_1.groupby('HomeTeam').mean().T.columns:
        teams[i] = []
    print(teams, len(teams))

    for i in range(len(season2223_1)):
        ATGC = season2223_1.iloc[i]['FTHG']
        HTGC = season2223_1.iloc[i]['FTAG']
        teams[season2223_1.iloc[i].HomeTeam].append(HTGC)
        teams[season2223_1.iloc[i].AwayTeam].append(ATGC)
    print(teams, len(list(teams.values())[0]))

    GoalsConceded = pd.DataFrame(data=teams, index = [i for i in range(1,len(list(teams.values())[0])+1)]).T
    GoalsConceded[0] = 0

    for i in range(2,len(list(teams.values())[0])+1):
        GoalsConceded[i] = GoalsConceded[i] + GoalsConceded[i-1]
    GoalsConceded
    teams = {}
    for i in season2223_1.groupby('HomeTeam').mean().T.columns:
        teams[i] = []
    print(teams, len(teams))

    for i in range(len(season2223_1)):
        HTGS = season2223_1.iloc[i]['FTHG']
        ATGS = season2223_1.iloc[i]['FTAG']
        teams[season2223_1.iloc[i].HomeTeam].append(HTGS)
        teams[season2223_1.iloc[i].AwayTeam].append(ATGS)
    print(teams, len(list(teams.values())[0]))

    GoalsScored = pd.DataFrame(data=teams, index = [i for i in range(1,len(list(teams.values())[0])+1)]).T
    GoalsScored[0] = 0

    for i in range(2,len(list(teams.values())[0])+1):
        GoalsScored[i] = GoalsScored[i] + GoalsScored[i-1]
    GoalsScored
    season2223_1 = season2223_1.sort_values(by='Id',ascending=False)
    j = 0
    HTGS = []
    ATGS = []
    HTGC = []
    ATGC = []
    print(season2223_1)
    print(GoalsScored)
    print(len(season2223_1))
    print(len(GoalsScored))
    print(GoalsScored.loc['CD Mirandes'][1])
    for i in range(len(season2223_1)):
        ht = season2223_1.iloc[i].HomeTeam
        at = season2223_1.iloc[i].AwayTeam
        print(ht)
        print(j)
        print(i)
        HTGS.append(GoalsScored.loc[ht][j])
        ATGS.append(GoalsScored.loc[at][j])
        HTGC.append(GoalsConceded.loc[ht][j])
        ATGC.append(GoalsConceded.loc[at][j])

        if ((i + 1)% 10) == 0:
            j = j + 1

    season2223_1['HTGS'] = HTGS
    season2223_1['ATGS'] = ATGS
    season2223_1['HTGC'] = HTGC
    season2223_1['ATGC'] = ATGC

    season2223_1 = season2223_1.sort_values(by='Id',ascending=True)

    return season2223_1

for x in list(data.Div.unique()):
    for e in list(data.Season.unique()):
        data[(data.Div == x) & (data.Season == e)] = goles(data[(data.Div == x) & (data.Season == e)])
data.head()