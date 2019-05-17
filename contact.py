class Contact:

  contacts = []
  next_id = 1

  def __init__(self, f_name, l_name, email, note):
    """This method should initialize the contact's attributes"""
    self.first_name = f_name
    self.last_name = l_name
    self.email = email
    self.note = note
    self.id = Contact.next_id
    Contact.next_id += 1


  def __str__(self):
    return f"Name: {self.first_name} {self.last_name} - Email: {self.email} - Info: {self.note}"


  @classmethod
  def create(cls, f_name, l_name, email, note):
    """This method should call the initializer,
    store the newly created contact, and then return it"""
    contact = Contact(f_name, l_name, email, note)
    cls.contacts.append(contact)
    return contact


  @classmethod
  def all(cls):
    """This method should return all of the existing contacts"""
    for contact in cls.contacts:
      print(f"{contact}")


  @classmethod
  def find(cls, id):
    """ This method should accept an id as an argument
    and return the contact who has that id"""
    print(cls.contacts[id - 1])


  def update(self):
    """ This method should allow you to specify
    1. which of the contact's attributes you want to update
    2. the new value for that attribute
    and then make the appropriate change to the contact
    """


  @classmethod
  def find_by(cls, attr, val):
    """This method should work similarly to the find method above
    but it should allow you to search for a contact using attributes other than id by specifying both the name of the attribute and the value eg. searching for 'first_name', 'Betty' should return the first contact named Betty"""
    for contact in cls.contacts:
      if getattr(contact, attr) == val:
        print(contact)


  @classmethod
  def delete_all(cls):
    """This method should delete all of the contacts"""
    cls.contacts.clear()


  def full_name(self):
    """Returns the full (first and last) name of the contact"""
    print(f"Full Name: {self.first_name} {self.last_name}")


  def delete(self):
    """This method should delete the contact
    HINT: Check the Array class docs for built-in methods that might be useful here"""
    Contact.contacts.remove(self)


  # Feel free to add other methods here, if you need them.

brody = Contact.create("Brody", "Currie", "brodycurrie@gmail.com", "Builds Gunpla")
jasmin = Contact.create("Jasmin", "Saromo", "JasminFace@gmail.com", "Also Builds Gunpla")
cindy = Contact.create("Cindy", "Chea", "cindychea@gmail.com", "Dancer")
kayla = Contact.create("Kayla", "Brissette", "kaylabrissette9@gmail.com", "loves dogs")

# print(len(Contact.contacts))
# print(brody.id)
# print(jasmin.id)
# print(cindy.id)
# print(kayla.id)
# Contact.all()

# Contact.find(1)

# Contact.delete_all()

# Contact.all()

# brody.full_name()

# Contact.find_by('first_name', 'Brody')

brody.delete()

Contact.all()