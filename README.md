# Notebook

Program to learn about the classes and realise realationships between different classes

The main class is Notebook. It contains all notes (class Note), and gives you opportunity to interact with them. You can add notes, search desired ones by tags, text or ID, you can modify tags, notes, show all notes. All of that functions are used in class Menu, which is the main engine of the program. When you start the program, you see this:

The menu:
1. Show all notes
2. Create new note
3. Print note by ID
4. Find note by tags
5. Find note by text
6. Modify note by ID
7. Modify tags by note ID
8. Exit

All of that is pretty straightforward and is made in class Menu. Every option is a different method, which almost always calls object notebook, which is created in menu object.
