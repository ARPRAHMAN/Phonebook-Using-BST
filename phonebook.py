def create_phonebook():
  """Initializes an empty phone book (list of tuples)."""
  phonebook = []
  return phonebook

def add_contact(phonebook, name, number):
  """Adds a new contact (name, number) to the phone book, maintaining alphabetical order."""
  contact = (name, number)
  index = 0
  while index < len(phonebook) and phonebook[index][0] < name:
    index += 1
  phonebook.insert(index, contact)

def binary_search(phonebook, name):
  """Searches for a contact's name in the phone book using binary search.

  Returns:
      The phone number if found, otherwise None.
  """
  low = 0
  high = len(phonebook) - 1
  while low <= high:
    mid = (low + high) // 2
    if phonebook[mid][0] == name:
      return phonebook[mid][1]
    elif phonebook[mid][0] < name:
      low = mid + 1
    else:
      high = mid - 1
  return None

def display_contact(name, number):
  """Prints the contact information in a user-friendly format."""
  if number:
    print(f"{name}'s phone number is: {number}")
  else:
    print(f"{name} is not found in the phone book.")

def main():
  """Main function to handle user interaction."""
  phonebook = create_phonebook()
  while True:
    print("\nPhone Book Menu")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
      name = input("Enter contact name: ")
      number = input("Enter phone number: ")
      add_contact(phonebook, name, number)
      print(f"Contact added successfully!")
    elif choice == '2':
      name = input("Enter name to search: ")
      number = binary_search(phonebook, name)
      display_contact(name, number)
    elif choice == '3':
      print("Exiting phone book...")
      break
    else:
      print("Invalid choice. Please try again.")

if __name__ == "__main__":
  main()
