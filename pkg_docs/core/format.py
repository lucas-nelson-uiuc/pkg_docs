import inspect
import re


def clean_documentation(docstring: str) -> str:
    """Format documentation for tabular cell"""
    RE_SPACES = re.compile("[\\n\\t\\r]+")
    return RE_SPACES.sub(" ", inspect.cleandoc(docstring))
