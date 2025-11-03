
class CalculatorError(Exception):
    """Base exception for calculator errors."""

class OperationError(CalculatorError):
    """Raised when an operation fails or is not supported."""

class ValidationError(CalculatorError):
    """Raised when user input fails validation."""

class PersistenceError(CalculatorError):
    """Raised when saving/loading history fails."""
