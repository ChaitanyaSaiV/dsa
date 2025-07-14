""" tolerant teams
Write a function, tolerant_teams, that takes in a list of rivalries as an argument. 

A rivalry is a pair of people who should not be placed on the same team. 

The function should return a boolean indicating whether or not it is possible to separate people into two teams, without rivals being on the same team. 

The two teams formed do not have to be the same size. """


def tolerant_teams(rivalries):
  graph = build_graph(rivalries)

  teamed = {}

  for rival in graph:
    if rival not in teamed:
      if formTeams(graph, rival, teamed, False) == False:
        return False

  return True

def formTeams(graph, rivals, teamed, team):
  if rivals in teamed:
    return team == teamed[rivals]
  
  teamed[rivals] = team

  for rival in graph[rivals]:
    if formTeams(graph, rival, teamed, not team) == False:
      return False
  
  return True

def build_graph(rivalries):
  graph = {}

  for rivals in rivalries:
    a, b = rivals
    if a not in graph:
      graph[a] = []
    if b not in graph:
      graph[b] = []
    
    graph[a].append(b)
    graph[b].append(a)
  
  return graph


print(tolerant_teams([
  ('cindy', 'anj'),
  ('alex', 'matt'),
  ('alex', 'cindy'),
  ('anj', 'matt'),
  ('brando', 'matt')
]))