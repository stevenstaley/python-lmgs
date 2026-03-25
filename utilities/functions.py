import os

def get_options_from_file(FILE_PATH):
    """Reads options from the file and returns a list."""
    options = []
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r") as f:
            # Read lines, strip whitespace, and filter out any empty lines
            options = [line.strip() for line in f.readlines() if line.strip()]
    return options

def load_options(FILE_PATH):
    """Reads options from the text file."""
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r") as f:
            # Read lines and join them into a single string for the text_area
            return "\n".join([line.strip() for line in f.readlines()])
    return ""

def save_options(text_content, FILE_PATH):
    """Saves the given text content to the file."""
    with open(FILE_PATH, "w") as f:
        f.write(text_content)