from selenium.webdriver.support.ui import Select

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def go_home(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and len( wd.find_elements_by_xpath("//select[@value='Send e-Mail']")) > 0):
            # Переход на главную страницу
            wd.find_element_by_link_text("home").click()



    def confirm_add(self):
        wd = self.app.wd
        # Подтверждение создания контакта
        wd.find_element_by_xpath("//input[@name='submit']").click()
        wd.find_element_by_xpath("//body").click()

    def fill(self, contact):
        wd = self.app.wd
        # Заполнение
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        wd.find_element_by_name("photo").clear()
        wd.find_element_by_name("photo").send_keys("C:\\unnamed.jpg")
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.home_phone)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobile_phone)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.work_phone)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(contact.fax)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contact.email2)
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(contact.email3)
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(contact.site)
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.birthday_day)
        wd.find_element_by_xpath("//select[@name='bday']").click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.birthday_month)
        wd.find_element_by_xpath("//select[@name='bmonth']").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.birthday_year)
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text(contact.aniversary_day)
        wd.find_element_by_xpath("//select[@name='aday']").click()
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(contact.aniversary_month)
        wd.find_element_by_xpath("//select[@name='amonth']").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(contact.aniversary_year)
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contact.address2)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact.phone2)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contact.notes)

    def create(self, contact):
        wd = self.app.wd
        self.init_add_contact()
        self.fill(contact)
        self.confirm_add()
        self.go_home()

    def init_add_contact(self):
        wd = self.app.wd
        # Инициализация создания контакта
        wd.find_element_by_link_text("add new").click()

    def delete_first_contact(self):
        wd = self.app.wd
        # выбрать первый контакт
        wd.find_element_by_name("selected[]").click()
        # удалить
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.go_home()

    def modify_first_contact(self, contact):
        wd = self.app.wd
        # инициировать редактирование первого конаткта
        wd.find_element_by_xpath("//img[@title='Edit']").click()
        # редактирование контакта
        self.fill(contact)
        # подтверждение редактирования
        wd.find_element_by_name("update").click()
        # возврат на страницу контактов
        self.go_home()

    def count(self):
        wd = self.app.wd
        self.go_home()
        return len(wd.find_elements_by_name("selected[]"))