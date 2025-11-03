
from dataclasses import dataclass
from typing import List
from .calculation import Calculation

@dataclass
class HistoryState:
    entries: List[Calculation]

class Caretaker:
    def __init__(self):
        self._undo_stack: List[HistoryState] = []
        self._redo_stack: List[HistoryState] = []

    def snapshot(self, entries: List[Calculation]):
        self._undo_stack.append(HistoryState(entries=list(entries)))
        self._redo_stack.clear()

    def can_undo(self): return bool(self._undo_stack)
    def can_redo(self): return bool(self._redo_stack)

    def undo(self, current_entries: List[Calculation]) -> List[Calculation]:
        if not self._undo_stack: return current_entries
        prev = self._undo_stack.pop()
        self._redo_stack.append(HistoryState(entries=list(current_entries)))
        return list(prev.entries)

    def redo(self, current_entries: List[Calculation]) -> List[Calculation]:
        if not self._redo_stack: return current_entries
        nxt = self._redo_stack.pop()
        self._undo_stack.append(HistoryState(entries=list(current_entries)))
        return list(nxt.entries)
