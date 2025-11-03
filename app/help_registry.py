# app/help_registry.py
from typing import Callable, Dict

_COMMAND_HELP: Dict[str, str] = {}

def register_command(name: str, help_text: str):
    """Decorator to register a REPL command with its help text."""
    def deco(fn: Callable):
        _COMMAND_HELP[name] = help_text
        return fn
    return deco

def build_help(extra_sections=None) -> str:
    """Render dynamic help from registered commands plus optional sections."""
    lines = ["Commands:"]
    for cmd, h in sorted(_COMMAND_HELP.items()):
        lines.append(f"  {cmd:<12} {h}")
    if extra_sections:
        lines.append("")
        lines.extend(extra_sections)
    return "\n".join(lines)
