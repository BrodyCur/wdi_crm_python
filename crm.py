from contact import Contact
import sys

class CRM:

  def main_menu(self):
    while True: # repeat indefinitely
      self.print_main_menu()
      user_selected = int(input())
      self.call_option(user_selected)


  def print_main_menu(self):
    print('[1] Add a new contact')
    print('[2] Modify an existing contact')
    print('[3] Delete a contact')
    print('[4] Display all the contacts')
    print('[5] Search by attribute')
    print('[6] Exit')
    print('Enter a number: ')


  def call_option(self, user_selected):
    if user_selected == 1:
      self.add_new_contact()
    elif user_selected == 2:
      self.modify_existing_contact()
    elif user_selected == 3:
      self.delete_contact()
    elif user_selected == 4:
      self.display_all_contacts()
    elif user_selected == 5:
      self.search_by_attribute()
    elif user_selected == 6:
      sys.exit()


  def add_new_contact(self):
    print('Enter First Name: ')
    first_name = input()

    print('Enter Last Name: ')
    last_name = input()

    print('Enter Email Address: ')
    email = input()

    print('Enter a Note: ')
    note = input()

    Contact.create(first_name=first_name, last_name=last_name, email=email, note=note)


  def modify_existing_contact(self):
    print('Enter the id of the contact you would like to modify: ')
    contact_id = int(input())
    contact = Contact.get(id=contact_id)

    print("Would you like to modify, 'first_name', 'last_name', 'email', or 'note': ")
    attr = input()

    print(f'Enter the new {attr}: ')
    new_val = input()

    setattr(contact, attr, new_val)
    contact.save()

    return contact
  
  def delete_contact(self):
    print('Enter the id of the contact you would like to delete: ')
    contact_id = int(input())

    contact = Contact.get(id=contact_id)

    contact.delete_instance()

  def display_all_contacts(self):
    for contact in Contact.select():
      print(f"{contact.first_name} {contact.last_name}, email: {contact.email}, notes: {contact.note}")


  def search_by_attribute(self):
    print("Please enter which attribute you would like to search by('first_name', 'last_name', 'email', 'note'): ")
    attribute = input()

    print("Please enter the search term: ")
    search_term = input()

    found_contact = None
    if attribute == 'first_name':
      found_contact = Contact.select().where(Contact.first_name == search_term)
    elif attribute == 'last_name':
      found_contact = Contact.select().where(Contact.last_name == search_term)
    elif attribute == 'email':
      found_contact = Contact.select().where(Contact.email == search_term)
    elif attribute == 'note':
      found_contact = Contact.select().where(Contact.note == search_term)
    elif attribute == 'id':
      found_contact = Contact.select().where(Contact.id == search_term)
    for contact in found_contact:
      print(f"{contact.first_name} {contact.last_name}, email: {contact.email}, notes: {contact.note}")


crm_app = CRM()
crm_app.main_menu()