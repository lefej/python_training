# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata =  [Contact(firstname =  random_string("firstname", 20), lastname =  random_string("lastname", 30), middlename = random_string("middlename", 30), nickname =random_string("middlename", 30),
                           title =random_string("middlename", 30), address =random_string("address", 30),
                           company = random_string("company", 30), home_phone = random_string("home_phone", 30), mobile_phone = random_string("mobile_phone", 30),
                           work_phone = random_string("work_phone", 30), fax = random_string("fax", 30),
                           email = random_string("email", 30), email2 = random_string("email2", 30),
                           email3 = random_string("email3", 30), site = random_string("site", 30),
                           birthday_year = "1990", aniversary_day = "28", birthday_day = "30", birthday_month = "July",
                           aniversary_month = "August", aniversary_year = "2000",
                           address2 = random_string("address2", 30), phone2 = random_string("phone2", 30), notes = random_string("middlename", 30))
             for i in range(5)
]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact1(app, contact):
        old_contacts = app.contact.get_contact_list()
        app.contact.create(contact)
        new_contacts = app.contact.get_contact_list()
        assert len(old_contacts) + 1 == len(new_contacts)
        old_contacts.append(contact)
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
