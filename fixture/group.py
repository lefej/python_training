
class GroupHelper:

    def __init__(self, app):
        self.app = app

    def return_to_groups(self):
        wd = self.app.wd
        # Возврат на страницу Группы
        wd.find_element_by_link_text("group page").click()

    def fill(self, group):
        wd = self.app.wd
        # Заполнение
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)

    def create(self, group):
        wd = self.app.wd
        self.open_groups()
        # Создание новой группы
        wd.find_element_by_name("new").click()
        # Заполнение
        self.fill(group)
        # Подтверждение создания группы
        wd.find_element_by_name("submit").click()
        self.return_to_groups()

    def open_groups(self):
        wd = self.app.wd
        # Открытие Групп
        wd.find_element_by_link_text("groups").click()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups()
        # выбрать первую группу
        wd.find_element_by_name("selected[]").click()
        # удалить
        wd.find_element_by_name("delete").click()
        self.return_to_groups()

    def modify_first_group(self, group):
        wd = self.app.wd
        self.open_groups()
        # выбрать первую группу
        wd.find_element_by_name("selected[]").click()
        # инициировать редактирование
        wd.find_element_by_name("edit").click()
        # редактирование
        self.fill(group)
        # подтверждение редактирования
        wd.find_element_by_name("update").click()
        # возврат в группы
        self.return_to_groups()