from pathlib import Path

def get_cats_info(path: str) -> list[dict[str, str]]:
    cats_info = []
    
    try:
        file_path = Path(path)
        
        with open(file_path, "r", encoding="utf-8") as file:
            for line_num, line in enumerate(file, 1):
                line = line.strip()
                if not line:
                    continue
                
                try:
                    parts = line.split(",")
                    if len(parts) != 3:
                        raise ValueError(f"Line must contain exactly three comma-separated fields (id, name, age).")
                    
                    cat_id, name, age = parts
                    
                    cats_info.append({
                        "id": cat_id.strip(),
                        "name": name.strip(),
                        "age": age.strip()
                    })
                except ValueError as e:
                    print(f"Warning: Corrupted data on line {line_num} in '{path}': {e}. Skipping line.")
                    
    except FileNotFoundError:
        print(f"Error: The file '{path}' was not found.")
        return []
    except PermissionError:
        print(f"Error: Permission denied when accessing the file '{path}'.")
        return []
    except Exception as e:
        print(f"Error: An unexpected error occurred while reading the file '{path}': {e}")
        return []
        
    return cats_info


if __name__ == "__main__":
    test_file_path = Path("cats_example.txt")
    test_content = (
        "60b90c1c13067a15887e1ae1,Tayson,3\n"
        "60b90c2413067a15887e1ae2,Vika,1\n"
        "60b90c2e13067a15887e1ae3,Barsik,2\n"
        "60b90c3b13067a15887e1ae4,Simon,12\n"
        "60b90c4613067a15887e1ae5,Tessi,5\n"
    )
    
    try:
        test_file_path.write_text(test_content, encoding="utf-8")
        cats_info = get_cats_info(str(test_file_path))
        print(cats_info)
        
        test_file_path.unlink(missing_ok=True)
    except Exception as e:
        print(f"Error running self-test: {e}")
