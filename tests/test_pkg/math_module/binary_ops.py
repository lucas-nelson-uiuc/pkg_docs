from typing import Iterable, Any
import operator

from pkg_docs.core.decorator import document


@document(section_name="Math Operations")
def compute_result(elements: Iterable, op: Any) -> Any:
    """Compute the result of an operator against an element(s)"""
    return getattr(operator, op)(elements)
