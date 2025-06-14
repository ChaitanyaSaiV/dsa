""" semesters required
Write a function, semesters_required, that takes in a number of courses (n) and a list of prerequisites as arguments. Courses have ids ranging from 0 through n - 1. A single prerequisite of (A, B) means that course A must be taken before course B. Return the minimum number of semesters required to complete all n courses. There is no limit on how many courses you can take in a single semester, as long as the prerequisites of a course are satisfied before taking it.

Note that given prerequisite (A, B), you cannot take course A and course B concurrently in the same semester. You must take A in some semester before B.

You can assume that it is possible to eventually complete all courses. """

def semesters_required(num_courses, prereqs):
  graph, courses = build_graph(prereqs)

  completed = set()

  sems = 0

  while courses:
    for prereqs in list(graph):
      for prereq in list(graph[prereqs]):
        if prereq in completed:
          graph[prereqs].remove(prereq)
        
        if len(graph[prereqs]) == 0:
          del graph[prereqs]

    current_sem = set()

    for course in courses:
      if course not in graph:
        current_sem.add(course)
    
    for current_sem_course in current_sem:
      courses.remove(current_sem_course)
      completed.add(current_sem_course)

    sems += 1
  
  return sems

def build_graph(prereqs):
  graph = {}
  courses = set()
  for prereq in prereqs:
    a, b = prereq
    if b not in graph:
      graph[b] = []
    if a not in courses:
      courses.add(a)
    if b not in courses:
      courses.add(b)

    graph[b].append(a)

  return graph, courses


num_courses = 6
prereqs = [
  (1, 2),
  (2, 4),
  (3, 5),
  (0, 5),
]
semesters_required(num_courses, prereqs) # -> 3