from pathlib import Path

def total_salary(path: str) -> tuple[float, float] | tuple[int, int]:
    total = 0
    count = 0
    
    try:
        file_path = Path(path)   
        with open(file_path, "r", encoding="utf-8") as file:
            for line_num, line in enumerate(file, 1):
                line = line.strip()
                if not line:
                    continue
                
                try:
                    parts = line.split(",")
                    if len(parts) != 2:
                        raise ValueError(f"Line must contain exactly one comma separating name and salary.")
                    
                    name, salary_str = parts
                    try:
                        salary = int(salary_str.strip())
                    except ValueError:
                        salary = float(salary_str.strip())
                    
                    total += salary
                    count += 1
                except ValueError as e:
                    print(f"Warning: Corrupted data on line {line_num} in '{path}': {e}. Skipping line.")
                    
    except FileNotFoundError:
        print(f"Error: The file '{path}' was not found.")
        return 0, 0
    except PermissionError:
        print(f"Error: Permission denied when accessing the file '{path}'.")
        return 0, 0
    except Exception as e:
        print(f"Error: An unexpected error occurred while reading the file '{path}': {e}")
        return 0, 0

    if count == 0:
        return 0, 0
        
    average = total / count
    
    if isinstance(total, int) and total % count == 0:
        return int(total), int(average)
        
    return total, average


if __name__ == "__main__":
    test_file_path = Path("salaries_example.txt")
    test_content = (
        "Alex Korp,3000\n"
        "Nikita Borisenko,2000\n"
        "Sitarama Raju,1000\n"
    )
    
    try:
        test_file_path.write_text(test_content, encoding="utf-8")
        total, average = total_salary(str(test_file_path))
        print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
        
        test_file_path.unlink(missing_ok=True)
    except Exception as e:
        print(f"Error running self-test: {e}")
