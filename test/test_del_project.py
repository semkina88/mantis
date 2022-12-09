from model.project import Project
import random


def test_delete_project(app):
    if len(app.soap.get_project_list()) == 0:
        app.project.add_project(Project(name="projects_new"))
    old_list = app.soap.get_project_list()
    project = random.choice(old_list)
    app.project.delete_project(project)
    new_list = app.soap.get_project_list()
    old_list.remove(project)
    assert sorted(old_list, key=Project.id_or_max) == sorted(new_list, key=Project.id_or_max)

