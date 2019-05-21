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

brody = Contact.create(first_name="Brody", last_name="Currie", email="brodycurrie@gmail.com", note="Builds Gunpla")
jasmin = Contact.create(first_name="Jasmin", last_name="Saromo", email="JasminFace@gmail.com", note="Also Builds Gunpla")
cindy = Contact.create(first_name="Cindy", last_name="Chea", email="cindychea@gmail.com", note="Dancer")
kayla = Contact.create(first_name="Kayla", last_name="Brissette", email="kaylabrissette9@gmail.com", note="loves dogs")

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