from dataclasses import dataclass
from datetime import datetime

projects = []


"""
tells the project that a file from another location is linked.
"""
@dataclass
class Reference:
    name : str
    fromPath : str
    toPath : str

"""
contains relevant project information for what is being worked on at the moment.
"""
@dataclass
class Project:
    name : str
    due : datetime
    description : str
    elements : list[Reference]


def view_project(proj : Project):
    print("project: " + proj.name)
    print("due: " + str(proj.due))
    print("description: " + proj.description)
    print("elements:")
    for el in proj.elements:
        print(el.name, "from:", el.fromPath, "to:", el.toPath)


# generate some example projects
projects.append(Project("java-learning", datetime(2023, 2, 6), "learning the java language to be more effective in the making of the code during internship.", []))
projects.append(Project("10 step cplex learning book", datetime(2023, 1, 16), "lezen over deze stapsgewijze leermethode.", []))

# view the data in the projects
for proj in projects:
    view_project(proj)