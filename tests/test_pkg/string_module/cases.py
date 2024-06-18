from pkg_docs.core.decorator import document


@document(section_name="String Operations")
def str_to_lower(s: str) -> str:
    """Convert a string to lowercase."""
    return s.lower()


@document(section_name="String Operations")
def str_to_upper(s: str) -> str:
    """Convert a string to uppercase."""
    return s.upper()


@document(section_name="String Operations")
def not_documented_func(s: str) -> str:
    """This function will be documented because it is decorated."""
    return s.capitalize()
