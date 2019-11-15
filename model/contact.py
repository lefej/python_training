class Contact:

    def __init__(self, firstname = None, middlename = None, lastname = None, nickname = None, title = None, address = None, company = None, home_phone = None,
                     mobile_phone = None, work_phone = None, fax = None, email = None, email2 = None, email3 = None, site = None, birthday_year = None, aniversary_day = None,
                     birthday_day = None, birthday_month = None, aniversary_month = None, aniversary_year = None, address2 = None, phone2 = None, notes = None, id = None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.address = address
        self.company = company
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.site = site
        self.birthday_year = birthday_year
        self.aniversary_day = aniversary_day
        self.birthday_day = birthday_day
        self.birthday_month = birthday_month
        self.aniversary_month = aniversary_month
        self.aniversary_year = aniversary_year
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return self.id == other.id and self.firstname == other.firstname and self.lastname == other.lastname
