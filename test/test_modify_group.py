from model.group import Group

def test_modify_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(name="отредактированная группа", header="тест2", footer="тест2"))
    app.session.logout()