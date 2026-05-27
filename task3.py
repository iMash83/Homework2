import sys
from pathlib import Path
from colorama import init, Fore, Style

init(autoreset=True)

def print_tree(path: Path, prefix: str = ""):
    try:
        entries = [
            e for e in path.iterdir() 
            if not e.name.startswith(".") and e.name != "__pycache__"
        ]
        entries = sorted(entries, key=lambda p: (not p.is_dir(), p.name.lower()))
    except PermissionError:
        print(f"{prefix}{Fore.RED}Permission denied: {path.name}{Style.RESET_ALL}")
        return
    except Exception as e:
        print(f"{prefix}{Fore.RED}Error listing {path.name}: {e}{Style.RESET_ALL}")
        return

    entries_count = len(entries)
    for index, entry in enumerate(entries):
        is_last = (index == entries_count - 1)
        connector = "┗ " if is_last else "┣ "
        
        if entry.is_dir():
            print(f"{prefix}{connector}{Fore.BLUE}{Style.BRIGHT}📂 {entry.name}{Style.RESET_ALL}")
            next_prefix = prefix + ("  " if is_last else "┃ ")
            print_tree(entry, next_prefix)
        else:
            print(f"{prefix}{connector}{Fore.GREEN}📜 {entry.name}{Style.RESET_ALL}")

def main():
    if len(sys.argv) < 2:
        print(f"{Fore.YELLOW}Usage: python task3.py <directory_path>{Style.RESET_ALL}")
        sys.exit(1)
        
    path_arg = sys.argv[1]
    path = Path(path_arg).resolve()
    
    if not path.exists():
        print(f"{Fore.RED}Error: Path '{path_arg}' does not exist.{Style.RESET_ALL}")
        sys.exit(1)
        
    if not path.is_dir():
        print(f"{Fore.RED}Error: Path '{path_arg}' is not a directory.{Style.RESET_ALL}")
        sys.exit(1)
        
    print(f"{Fore.CYAN}{Style.BRIGHT}📦 {path.name}{Style.RESET_ALL}")
    print_tree(path)

if __name__ == "__main__":
    main()
