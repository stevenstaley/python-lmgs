import os

def get_options_from_file(FILE_PATH):
    """Reads options from the file and returns a list."""
    options = []
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r") as f:
            # Read lines, strip whitespace, and filter out any empty lines
            options = [line.strip() for line in f.readlines() if line.strip()]
    return options