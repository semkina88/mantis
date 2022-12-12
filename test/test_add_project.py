from model.project import Project


def test_add_project(app):
    project = Project("name", "description")
    old_list = app.soap.get_project_list()
    if project in old_list:
        app.project.delete_project(project)
        old_list.remove(project)
    old_list = app.soap.get_project_list()
    app.project.add_project(project)
    new_list = app.soap.get_project_list()
    old_list.append(project)
    assert sorted(old_list, key=Project.id_or_max) == sorted(new_list, key=Project.id_or_max)
    assert sorted(old_list, key=Project.id_or_max) == sorted(new_list, key=Project.id_or_max)