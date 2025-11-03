
# Command-line REPL (uses Colorama for color-coded outputs — optional feature for A)
import sys
from colorama import init, Fore, Style  # pip install colorama
from .calculator_config import Config, ensure_dirs
from .calculator import Calculator
from .observers_impl import LoggingObserver, AutoSaveObserver

COMMANDS = {"add","subtract","multiply","divide","power","root","modulus","int_divide","percent","abs_diff",
            "history","clear","undo","redo","save","load","help","exit"}

HELP = """Commands:
 add|subtract|multiply|divide|power|root|modulus|int_divide|percent|abs_diff a b
 history | clear | undo | redo | save | load | help | exit
"""

def main():  # pragma: no cover (interactive loop)
    init(autoreset=True)
    cfg = Config()
    ensure_dirs(cfg)
    calc = Calculator(cfg)
    calc.register_observer(LoggingObserver(cfg))
    calc.register_observer(AutoSaveObserver(calc.history, cfg))

    print(Fore.CYAN + "Calculator REPL. Type 'help' for commands.")
    while True:
        try:
            raw = input(Fore.GREEN + "calc> " + Style.RESET_ALL).strip()
        except (EOFError, KeyboardInterrupt):
            print("\nBye!")
            break
        if not raw: 
            continue
        parts = raw.split()
        cmd = parts[0]
        if cmd not in COMMANDS:
            print(Fore.RED + f"Unknown command: {cmd}"); 
            continue

        try:
            if cmd == "help":
                print(HELP)
            elif cmd == "exit":
                print("Bye!"); 
                break
            elif cmd == "history":
                for i, c in enumerate(calc.history.all(), 1):
                    print(f"{i}. {c.op} {c.a} {c.b} = {c.result} @ {c.ts.isoformat()}")
            elif cmd == "clear":
                calc.clear(); print("History cleared.")
            elif cmd == "undo":
                calc.undo(); print("Undone.")
            elif cmd == "redo":
                calc.redo(); print("Redone.")
            elif cmd == "save":
                calc.save(); print("Saved.")
            elif cmd == "load":
                calc.load(); print("Loaded.")
            else:
                if len(parts) != 3:
                    print(Fore.YELLOW + "Usage: <op> <a> <b>")
                    continue
                a,b = parts[1], parts[2]
                res = calc.calculate(cmd, a, b)
                print(Fore.WHITE + f"= {res}")
        except Exception as e:
            print(Fore.RED + f"Error: {e}")

if __name__ == "__main__":
    main()
