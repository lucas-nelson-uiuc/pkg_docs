from types import ModuleType
import inspect
import pkgutil

from pkg_docs.core.constants import KEYWORD_CONTEXT, KEYWORD_SECTION_NAME


def extract_module_metadata(module: ModuleType) -> dict[str, str]:
    """Extract metadata from module objects tagged for documentation

    For all functions in a module, if the function has been decorated with
    `@document()` - which assigns the `_doc_metadata` attribute to `True` -
    store necessary information to a dictionary. This dictionary contains
    metadata that will be rendered in the final Jinja Template.
    """
    functions = dict()
    for name, func in inspect.getmembers(module, inspect.isfunction):
        assert inspect.getdoc(func) is not None, f"Missing docstring for: `{name}`"
        if hasattr(func, f"_{KEYWORD_SECTION_NAME}"):
            section_name = func._section_name
            if section_name not in functions:
                functions[section_name] = dict()
            functions[section_name][name] = {
                "docstring": inspect.getdoc(func),
                "annotations": inspect.get_annotations(func),
            }
    return functions


def extract_package_metadata(package: ModuleType) -> dict[str, str]:
    """Extract metadata from pacakge objects

    For all modules in the package, extract metadata from each module
    tagged for documentation. See `extract_module_metadata` for more
    information.
    """
    all_functions = {KEYWORD_CONTEXT: {}}
    package_path = package.__path__
    package_name = package.__name__

    for _, module_name, ispkg in pkgutil.walk_packages(
        path=package_path, prefix=f"{package_name}."
    ):
        if not ispkg:
            module = __import__(module_name, fromlist="dummy")
            functions = extract_module_metadata(module)
            all_functions[KEYWORD_CONTEXT] |= functions
    return all_functions
