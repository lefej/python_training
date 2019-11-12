from model.contact import Contact

def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create( Contact(firstname="Анна", middlename="Петровна", lastname="Лесовская", nickname="anna", title="тест222",
                address="г. Москва, ул. Революции, д.1",
                company="ПАО Сбербанк", home_phone="+7 495 1234567", mobile_phone="+7 903 1414133", work_phone="1111", fax="9999",
                email="anna@rambler.ru", email2="anna@gmail.com",
                email3="anna@mail.ru", site="anna.com",
                birthday_year="1985", aniversary_day="20", birthday_day="21", birthday_month="September",
                aniversary_month="October", aniversary_year="2002",
                address2="ул. Покрова, д.1", phone2="тест3", notes="zzzzzzzz"))
    app.contact.delete_first_contact()
