# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange

def test_modify_some_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname ="Олеся", middlename ="Павловна", lastname ="Лисовская", nickname ="lefej", title ="тест", address ="г. Москва, ул. Раменки, д.25",
                           company = "НИИ Восход", home_phone = "555555", mobile_phone = "444444", work_phone = "33333", fax = "22222",
                           email = "lefej@rambler.ru", email2 = "olesalis@gmail.com",
                           email3 = "test@mail.ru", site = "test.com",
                           birthday_year = "1990", aniversary_day = "28", birthday_day = "30", birthday_month = "July",
                           aniversary_month = "August", aniversary_year = "2000",
                           address2 = "ул. Удальцова, д.85", phone2 = "тест2", notes = "тест тест тест 7777"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Анна", middlename="Петровна", lastname="Лесовская", nickname="anna", title="тест222",
                address="г. Москва, ул. Революции, д.1",
                company="ПАО Сбербанк", home_phone="+7 495 1234567", mobile_phone="+7 903 1414133", work_phone="1111", fax="9999",
                email="anna@rambler.ru", email2="anna@gmail.com",
                email3="anna@mail.ru", site="anna.com",
                birthday_year="1985", aniversary_day="20", birthday_day="21", birthday_month="September",
                aniversary_month="October", aniversary_year="2002",
                address2="ул. Покрова, д.1", phone2="тест3", notes="zzzzzzzz")
    index = randrange(len(old_contacts))
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(contact, index)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)