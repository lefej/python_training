from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


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
             for i in range(n)
             ]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))