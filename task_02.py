def get_cats_info(path: str) -> list[dict[str, str]]:
    """
    Reads cat information from a file and returns a list of dictionaries.

    Each line in the file should contain a cat's ID, name, and age, separated by commas.

    Parameters:
        path (str): The path to the text file containing cat data.

    Returns:
        list[dict[str, str]]: A list of dictionaries, each representing a cat with keys "id", "name", and "age".

    Raises:
        FileNotFoundError: If the file at the given path does not exist.
        ValueError: If any line in the file is malformed or missing fields.
    """
    cats = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line_number, line in enumerate(file, start=1):
                parts = line.strip().split(',')
                if len(parts) != 3:
                    raise ValueError(f"Malformed line {line_number}: '{line.strip()}'")
                cat_id, name, age = parts
                cats.append({"id": cat_id, "name": name, "age": age})
        return cats
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found at path: '{path}'")
    except Exception as e:
        raise RuntimeError(f"Error processing file: {e}")
    

# Example usage:
if __name__ == "__main__":
    try:
        cats_info = get_cats_info("cats.txt")
        print(type(cats_info))
        for cat in cats_info:
            print(cat)
    except Exception as e:
        print(e)


# Output:
# <class 'list'>
# {'id': '60b90c1c13067a15887e1ae1', 'name': 'Tayson', 'age': '3'}
# {'id': '60b90c2413067a15887e1ae2', 'name': 'Vika', 'age': '1'}
# {'id': '60b90c2e13067a15887e1ae3', 'name': 'Barsik', 'age': '2'}
# {'id': '60b90c3b13067a15887e1ae4', 'name': 'Simon', 'age': '12'}
# {'id': '60b90c4613067a15887e1ae5', 'name': 'Tessi', 'age': '5'}