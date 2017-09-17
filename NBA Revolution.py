#Roundrobin competition
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
    
