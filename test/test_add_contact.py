# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange

def test_add_contact1(app):
        old_contacts = app.contact.get_contact_list()
        contact = Contact(firstname ="Олеся", middlename ="Павловна", lastname ="Лисовская", nickname ="lefej", title ="тест", address ="г. Москва, ул. Раменки, д.25",
                           company = "НИИ Восход", home_phone = "555555", mobile_phone = "444444", work_phone = "33333", fax = "22222",
                           email = "lefej@rambler.ru", email2 = "olesalis@gmail.com",
                           email3 = "test@mail.ru", site = "test.com",
                           birthday_year = "1990", aniversary_day = "28", birthday_day = "30", birthday_month = "July",
                           aniversary_month = "August", aniversary_year = "2000",
                           address2 = "ул. Удальцова, д.85", phone2 = "тест2", notes = "тест тест тест 7777")
        app.contact.create(contact)
        new_contacts = app.contact.get_contact_list()
        assert len(old_contacts) + 1 == len(new_contacts)
        old_contacts.append(contact)
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_add_contact2(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Иван", middlename="Иванович", lastname="Иванов", nickname="ivanov",
                      title="тест", address="г. Москва, ул. Ленина, д.25",
                      company="АО Сбербанк", home_phone="555555", mobile_phone="444444",
                      work_phone="33333", fax="22222",
                      email="ivanov@rambler.ru", email2="ivanov@gmail.com",
                      email3="test@mail.ru", site="test.com",
                      birthday_year="2000", aniversary_day="22", birthday_day="11",
                      birthday_month="January",
                      aniversary_month="August", aniversary_year="2000",
                      address2="ул. Почтовая, д.85", phone2="тест2", notes="тест тест тест тест тест 999555")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)