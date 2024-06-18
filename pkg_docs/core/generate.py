from pathlib import Path

# from docxtpl import DocxTemplate
from jinja2 import Environment, PackageLoader, select_autoescape

from pkg_docs.core.constants import (
    KEYWORD_CONTEXT,
    KEYWORD_SECTION_NAME,
    KEYWORD_FUNCTIONS_CONTEXT,
    KEYWORD_PACKAGE_NAME,
)
from pkg_docs.core.extract import extract_package_metadata
from pkg_docs.core.format import clean_documentation


def generate_documentation(
    package_context: dict[str, str],
    jinja_env: Environment,
    template_filepath: str,
    output_filepath: str,
) -> None:
    """Write package context to Jinja Template at provided path.

    TODO: ideally will not be a for-loop; broken out like such for the moment
    """
    output_filepath = Path(output_filepath)
    output_filepath.mkdir(parents=True, exist_ok=True)

    template_document = jinja_env.get_template(template_filepath)
    
    for section_name, functions_context in package_context.items():
        context = {
            KEYWORD_SECTION_NAME: section_name,
            KEYWORD_FUNCTIONS_CONTEXT: functions_context,
        }
        section_name = f"{section_name.replace(' ', '_')}"
        with open(
            output_filepath.joinpath(f"{section_name}.md"), "w"
        ) as fp:
            fp.write(template_document.render(context))


def orchestrate_documentation(
    package_name: str,
    template_filepath: str,
    output_filepath: str,
) -> None:
    """Helper function for creating documentation."""
    package = __import__(name=package_name)
    package_context = extract_package_metadata(package=package)
    template_loader = PackageLoader(package_name=KEYWORD_PACKAGE_NAME)
    jinja_env = Environment(loader=template_loader, autoescape=select_autoescape())
    jinja_env.filters["clean_documentation"] = clean_documentation
    generate_documentation(
        package_context=package_context.get(KEYWORD_CONTEXT),
        jinja_env=jinja_env,
        template_filepath=template_filepath,
        output_filepath=output_filepath,
    )
