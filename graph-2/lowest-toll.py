""" lowest toll
You are given the tolls for different highways. Each highway connects a pair of cities and has a particular cost that must be paid to use it.

Each highway toll is a triplet (cityA, cityB, cost). Every highway can be traveled in either direction.

Write a function that takes in highway tolls and two cities. 

The function should return the lowest cost required to travel between the two cities. You can assume that there exists at least one way to travel between the two cities. """

def build_graph(highway_tolls):
    graph = {}
    for city_a, city_b, distance in highway_tolls:
        if city_a not in graph:
            graph[city_a] = {}
        if city_b not in graph:
            graph[city_b] = {}
        graph[city_a][city_b] = distance
        graph[city_b][city_a] = distance
    return graph


def lowest_toll(highway_tolls, start_city, end_city):
  highway_graph = build_graph(highway_tolls)
  return _lowest_toll(highway_graph, set(), start_city, end_city)

def _lowest_toll(highway_graph, visited, start_city, end_city):
  if start_city == end_city:
    return 0
  
  if start_city in visited:
    return float("inf")

  visited.add(start_city)

  minimum_distance = float("inf")

  for highway_neighbor in highway_graph[start_city]:
    if highway_neighbor not in visited:
      distance = highway_graph[start_city][highway_neighbor]
      distance_end_city = distance + _lowest_toll(highway_graph, visited, highway_neighbor, end_city)
      minimum_distance = min(minimum_distance, distance_end_city)
  
  visited.remove(start_city)

  return minimum_distance


highway_tolls = [
  ("Hampton", "Fairfax", 7.50),
  ("Roanoake", "Alexandria", 4.20),
  ("Alexandria", "Hampton", 14.50),
  ("Hampton", "Roanoake", 8.90),
  ("Alexandria", "Fairfax", 5.90),
  ("Hampton", "Manassas", 3.50),
  ("Fairfax", "Manassas", 2.20),
]
print(lowest_toll(highway_tolls, "Alexandria", "Hampton")) # -> 11.60