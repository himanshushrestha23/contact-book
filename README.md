# Contact Book

## Description

A simple command-line application built in Python to manage contacts. The application allows users to add, search, update, delete, and display contacts through a menu-driven interface. Contact information is stored using a Python dictionary and saved to a text file so contacts persist after closing the program.

## Features

* Add a new contact.
* Search for a contact by name or phone number.
* Update a contact's phone number.
* Delete a contact.
* Display all contacts in alphabetical order.
* Prevent duplicate contact names.
* Prevent duplicate phone numbers.
* Validate empty names and phone numbers.
* Load saved contacts when the program starts.
* Save contacts to a file when the program exits.

## Technologies Used

* Python 3
* Dictionaries
* Functions
* Loops
* Conditional statements
* File handling
* Exception handling

## How to Run

1. Clone this repository.
2. Open the project folder.
3. Run:

```bash
python contact_book.py
```

The program will create `contact_book.txt` when contacts are saved for the first time.

## How It Works

Each contact is stored in a dictionary where the contact name is the key and the phone number is the value.

```python
{"John": "98XXXXXXXX"}
```

The program uses a menu-driven interface to let the user add, search, update, delete, and display contacts.

When displaying contacts, the names are sorted alphabetically.

## File Storage

Contacts are stored in `contact_book.txt` using the following format:

```text
John:98XXXXXXXX
Jack:97XXXXXXXX
```

When the program starts, it reads the file and converts each line into a dictionary entry.

When the user exits, the current contacts are written back to the file.

## What I Learned

* Using dictionaries to store related data.
* Organizing a program into functions.
* Building menu-driven command-line applications.
* Searching through dictionary keys and values.
* Validating and handling user input.
* Updating and deleting dictionary data.
* Reading and writing data using text files.
* Converting file data into dictionary data and vice versa.

## Future Improvements

* Store additional contact information such as email and address.
* Add phone number format validation.
* Allow users to search for partial names.
* Improve the user interface.
