from pkg_docs.core.constants import KEYWORD_SECTION


def document(section_name: str = "Package") -> callable:
    """Generic decorator for tagging functions for documentation"""

    def decorator(func: callable) -> callable:
        func._is_documented = True
        func._section_name = section_name
        return func

    return decorator
