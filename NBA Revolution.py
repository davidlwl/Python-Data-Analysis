#Roundrobin competition
#You are in charge of writing the program that will generate the regular season schedule every year from now on. The NBA executive committee wants the competition to be as fair as possible, so the round robin tournament has to conform with the below rules:
1 - The number of teams engaged is maintained to 30.
2 - The schedule is composed of 58 rounds of 15 games. Each team plays 2 games against the other teams - one at home and the other away - for a total of 58 games. All teams are playing on the same day within a round.
3 - After the first half of the regular season (29 rounds), each team must have played exactly once against all other teams.
4 - Each team cannot play more than 2 consecutive home games, and playing 2 consecutive home games cannot occur more than once during the whole season.
5 - Rule 4 also applies to away games.
6 - The schedule generated must be different every time the program is launched.

teams = ["Cleveland Cavaliers", "Golden State Warriors", "San Antonio Spurs", \
         "Toronto raptors"]
def fixtures(teams):
    if len(teams) % 2:
        teams.append('Day off')  # if team number is odd - use 'day off' as fake team     

    rotation = list(teams)       # copy the list

    fixtures = []
    for i in range(0, len(teams)-1):
        fixtures.append(rotation)
        rotation = [rotation[0]] + [rotation[-1]] + rotation[1:-1]

    return fixtures

matches = fixtures(teams)
matched = []
for f in matches:
    raises =zip(*[iter(f)]*2)
    matched += set(raises)

for idx, d in enumerate(matched):
    print("Round " + str(idx + 1))
    print(d[0] + " vs " + d[1])
    print(' ')










'''
teams = []
while True:
    team = input('add a team ')
    if team == '0':
        break
    teams.append(team)
print(teams)

For i in teams:'''
    
