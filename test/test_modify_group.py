from model.group import Group

def test_modify_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
   # app.group.modify_first_group(Group(name="отредактированная группа", header="тест2", footer="тест2"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(name="отредактированная группа"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)