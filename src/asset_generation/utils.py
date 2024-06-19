import json

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

# class CompactJSONEncoder(json.JSONEncoder):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.indent = kwargs.get('indent', None)
#         self.newline_indent = '\n' + (' ' * self.indent) if self.indent else ''

#     def iterencode(self, obj, _one_shot=False):
#         print(obj)
#         if isinstance(obj, list):
#             print(1)
#             if len(obj) == 0:
#                 print(4)
#                 return super().iterencode(obj, _one_shot)
#             list_content = ', '.join(super().iterencode(elm, _one_shot) for elm in obj)
#             print(2)
#             return f'[{list_content}]'
#         print(3)
#         return super().iterencode(obj, _one_shot)

def dump_json_to_file(json_obj, file_path):
    """
    Dumps the given JSON object to a file.

    Parameters:
    json_obj (dict): The JSON object to be dumped.
    file_path (str): The path to the file where the JSON object will be written.
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(json_obj, file, ensure_ascii=False, indent=4)
        print(f"Successfully dumped JSON to the file at {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")