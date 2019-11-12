
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
        self.type("group_name", group.name)
        self.type("group_header", group.header)
        self.type("group_footer", group.footer)

    def type(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

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
        if not (wd.current_url.endswith("/group.php") and len( wd.find_elements_by_name("new")) > 0):
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

    def count(self):
        wd = self.app.wd
        self.open_groups()
        return len(wd.find_elements_by_name("selected[]"))