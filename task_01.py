def total_salary(path: str) -> tuple[int, float]:
    """
    Calculates the total and average monthly salaries of developers from a given file.

    The file should contain one developer per line in the format: "Name,Salary",
    where Salary is a numeric value.

    Lines that are malformed (missing comma or invalid salary) will be skipped
    with a warning message. If the file does not exist or is unreadable, the function
    will return (0, 0.0) and print an error message.

    Parameters:
    path (str): Path to the text file containing developer salary data.

    Returns:
    tuple[int, float]: A tuple containing the total salary (int) and average salary (float).
                       If no valid data is found, returns (0, 0.0).
    """
    try:
        with open(path, 'r', encoding='utf-8') as file:
            salaries = []
            for line in file:
                try:
                    name, salary = line.strip().split(',')
                    salaries.append(int(salary))
                except ValueError:
                    print(f"Warning: Skipping malformed line: {line.strip()}")
            if not salaries:
                return (0, 0.0)
            total = sum(salaries)
            average = total / len(salaries)
            return total, average
    except FileNotFoundError:
        print(f"Error: File not found at path '{path}'")
        return (0, 0.0)
    except Exception as e:
        print(f"Unexpected error: {e}")
        return (0, 0.0)
    

# Example usage:
if __name__ == "__main__":
    try:
        total, average = total_salary("salary_file.txt")
        print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
    except Exception as e:
        print(e)

# Output: Загальна сума заробітної плати: 6000, Середня заробітна плата: 2000.0