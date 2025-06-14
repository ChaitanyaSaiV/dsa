""" prereqs possible
Write a function, prereqs_possible, that takes in a number of courses (n) and prerequisites as arguments. Courses have ids ranging from 0 through n - 1. A single prerequisite of (A, B) means that course A must be taken before course B. The function should return a boolean indicating whether or not it is possible to complete all courses. """


def prereqs_possible(num_courses, prereqs):
  courses_taken = set()
  graph = build_graph(prereqs)


  return len(courses_taken) == numCourses

def build_graph(prereqs):
  graph = {}
  for prereq in prereqs:
    a, b = prereq
    if b not in graph:
      graph[a] = []
    if b not in graph:
      graph[b] = []
    graph[b].append(a)

  return graph


numCourses = 6
prereqs = [
  (0, 1),
  (2, 3),
  (0, 2),
  (1, 3),
  (4, 5),
]
prereqs_possible(numCourses, prereqs)