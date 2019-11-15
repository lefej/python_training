from model.group import Group

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
        self.group_cache = None

    def open_groups(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len( wd.find_elements_by_name("new")) > 0):
            # Открытие Групп
            wd.find_element_by_link_text("groups").click()


    def select_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def delete_first_group(self):
        self.delete_group_by_index(0)

    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.open_groups()
        # выбрать первую группу
        self.select_group_by_index(index)
        #wd.find_element_by_name("selected[]").click()
        # удалить
        wd.find_element_by_name("delete").click()
        self.return_to_groups()
        self.group_cache = None

    def modify_first_group(self, group):
        self.modify_group_by_index(group, 0)

    def modify_group_by_index(self, group, index):
        wd = self.app.wd
        self.open_groups()
        # выбрать первую группу
        self.select_group_by_index(index)
       #wd.find_element_by_name("selected[]").click()
        # инициировать редактирование
        wd.find_element_by_name("edit").click()
        # редактирование
        self.fill(group)
        # подтверждение редактирования
        wd.find_element_by_name("update").click()
        # возврат в группы
        self.return_to_groups()
        self.group_cache = None

    def count(self):
        wd = self.app.wd
        self.open_groups()
        return len(wd.find_elements_by_name("selected[]"))

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_groups()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name = text, id = id))
        return list(self.group_cache)