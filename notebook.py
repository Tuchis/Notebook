"""
MODULE DOCSTRING
"""
import note


class Notebook:
    """
    The class that contains notes
    """

    def __init__(self):
        self.notes = []
        self.note_id = 1

    def __str__(self):
        return f"The notebook\n" \
               f"There are {len(self.notes)} in the notebook"

    def search_by_text(self, filter) -> list:
        """
        Search by the text among the notes
        """
        match = []
        [match.append(elem.note_id) for elem in self.notes if elem.match(filter)]
        if match:
            return f'The text is found in that notes - {str(match)[1:-1]}.'
        else:
            return f"The text wasn't found in notes."

    def search_by_tags(self, filter) -> list:
        """
        Search by the tags among the notes
        """
        match = []
        [match.append(elem.note_id) for elem in self.notes if elem.match(filter)]
        if match:
            return f'Notes with such tags - {str(match)[1:-1]}.'
        else:
            return f"There are no notes with such tags."

    def new_note(self, memo, tags=""):
        """
        Creates the new note
        """
        self.notes.append(note.Note(memo, tags, self.note_id))
        self.note_id += 1

    def modify_memo(self, given_id, memo):
        """
        Modifies the memo in notes by its id
        """
        [note.memo_change(memo) for note in self.notes if note.note_id == given_id]

    def modify_tags(self, given_id, tags):
        """
        Modifies the memo in notes by its tag
        """
        [note.tags_change(tags) for note in self.notes if note.note_id == given_id]

    def print_note_by_id(self, given_id):
        """
        Prints note by id
        """
        try:
            return [note for note in self.notes if note.note_id == given_id][0]
        except IndexError:
            return "There are no notes with that id."


class CommandOption:
    def __int__(self):
        pass


class Menu:
    def __init__(self):
        pass


def main():
    """
    MAIN FUNCTION
    """
    notebook = Notebook()
    print(notebook)
    notebook.new_note("Hello", ["Start", "First"])
    notebook.new_note("Good bye", ["First"])
    notebook.new_note("Vlad", ["Name"])
    print(notebook.print_note_by_id(3))
    notebook.modify_memo(1, "Not Hello")
    notebook.modify_tags(1, ["New Tag"])
    print(notebook.print_note_by_id(0))
    print(notebook.search_by_text("o"))
    print(notebook.search_by_tags("First"))

if __name__ == "__main__":
    main()
