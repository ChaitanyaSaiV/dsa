def semesters_required(num_courses, prereqs):
  graph = build_graph(prereqs)
  print(graph)


def build_graph(prereqs):
  graph = {}

  for prereq in prereqs:
    a, b = prereq
    if a not in graph:
      graph[a] = []
    if b not in graph:
      graph[b] = []
    graph[a].append(b)
    graph[b].append(a)
  return graph


num_courses = 6
prereqs = [
  (1, 2),
  (2, 4),
  (3, 5),
  (0, 5),
]
semesters_required(num_courses, prereqs)