from model.group import Group
from random import randrange

def test_modify_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
   # app.group.modify_first_group(Group(name="отредактированная группа", header="тест2", footer="тест2"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="отредактированная группа")
    group.id = old_groups[index].id
    app.group.modify_group_by_index(group, index)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)