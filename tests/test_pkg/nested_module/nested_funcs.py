import re

from pkg_docs.core.decorator import document


@document(section_name="Nested Module")
def generate_sentence(strings: list[str], sep: str = ". ") -> str:
    """Separate collection of strings by character"""

    @document(section_name="Nested Module")
    def clean_string(string: str) -> str:
        RE_SPACES = re.compile("[\s]+")
        return RE_SPACES.sub(" ", string)

    @document(section_name="Nested Module")
    def format_string(string: str) -> str:
        return '"' + string + '"'

    return sep.join(map(format_string, map(clean_string, strings)))
