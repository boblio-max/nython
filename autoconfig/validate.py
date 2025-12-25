from .errors import MissingConfigError, InvalidTypeError
def validate_and_cast(name, value, expected_type):
    if value is None:
        raise MissingConfigError(f"Missing required config value: '{name}'")
    try:
        return expected_type(value)
    except Exception:
        raise InvalidTypeError(f"Config '{name}' must be of type {expected_type.__name__}, got value '{value}'")
