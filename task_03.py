import sys
from pathlib import Path
from colorama import init, Fore

def print_directory_tree(path: Path, indent: str = "    "):
    """
    Recursively prints the directory tree structure starting from the given path.

    Parameters:
        path (Path): The starting directory path.
        indent (str): Indentation prefix for nested levels (used internally).
    """
    for item in sorted(path.iterdir()):
        if item.is_dir():
            print(indent + Fore.BLUE + f"{item.name}/")
            print_directory_tree(item, indent + "    ")
        else:
            print(indent + Fore.GREEN + item.name)

def main():
    """
    Main function to handle command-line argument and initiate directory tree printing.
    """
    # Initialize colorama to enable coloured terminal output.
    # The 'autoreset=True' option automatically resets colours and styles
    # after each print(), so there's no need to manually call Style.RESET_ALL.
    init(autoreset=True)
    
    if len(sys.argv) != 2:
        print(Fore.RED + "Usage: python3 task_03.py /path/to/directory")
        sys.exit(1)

    dir_path = Path(sys.argv[1])

    if not dir_path.exists():
        print(Fore.RED + f"Error: Path '{dir_path}' does not exist.")
        sys.exit(1)

    if not dir_path.is_dir():
        print(Fore.RED + f"Error: Path '{dir_path}' is not a directory.")
        sys.exit(1)

    print(Fore.CYAN + f"Directory tree for: {dir_path}\n")
    print(Fore.BLUE + f"{dir_path.name}/")
    print_directory_tree(dir_path)

if __name__ == "__main__":
    main()