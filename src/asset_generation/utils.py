

def append_to_file(file_path: str, content_to_append: str, new_line: bool = True):
    """
    Appends the given string to the content of the file at the specified path.

    Parameters:
    file_path (str): The path to the file.
    content_to_append (str): The string to append to the file.
    """
    try:
        with open(file_path, 'a', encoding='utf-8') as file:
            file.write(content_to_append)
            if new_line:
                file.write("\n")
    except Exception as e:
        print(f"An error occurred: {e}")