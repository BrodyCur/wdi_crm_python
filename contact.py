from peewee import SqliteDatabase, Model, CharField, TextField

db = SqliteDatabase('crm.db')

class Contact(Model):
  first_name = CharField()
  last_name = CharField()
  email = CharField()
  note = TextField()

  class Meta:
    database = db

  def full_name(self):
    """Returns the full (first and last) name of the contact"""
    return(f"Full Name: {self.first_name} {self.last_name}")


db.connect()
db.create_tables([Contact])

# brody = Contact.create("Brody", "Currie", "brodycurrie@gmail.com", "Builds Gunpla")
# jasmin = Contact.create("Jasmin", "Saromo", "JasminFace@gmail.com", "Also Builds Gunpla")
# cindy = Contact.create("Cindy", "Chea", "cindychea@gmail.com", "Dancer")
# kayla = Contact.create("Kayla", "Brissette", "kaylabrissette9@gmail.com", "loves dogs")

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

# brody.delete()

# Contact.all()

# kayla.update('note', 'Will flip the bitch')

# Contact.all()