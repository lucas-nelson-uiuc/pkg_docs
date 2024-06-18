# Package Documentation: `pkg_docs`

Documentation generator for local packages. Alternative to tools like Sphinx, MkDocs, and more.

### Installation

*Note: not yet ready to install!*

```bash
pip install pkg_docs
```

### Usage

The `pkg_docs` package provides basic framework for generating documentation alongside the source code. Given the integration with the `Jinja` package, the aim of `pkg_docs` is to create a dictionary containing all "relevant" metadata of your source code.

For all functions you wish to document, you can decorate them with the `@document` decorator. The user can optionally pass a `section_name` argument to the decorator, allowing for separate sections within the documentation.

```python
# source: pkg/core/string_ops.py

SECTION_NAME = "String Operations"

@document(section=SECTION_NAME)
def str_to_lower(s: str) -> str:
    """Convert string to lowercase"""
    if is_string(s):
        return s.lower()

@document(section=SECTION_NAME)
def str_to_title(s: str) -> str:
    """Convert string to titlecase"""
    if is_string(s):
        return s.title()

@document(section=SECTION_NAME)
def str_to_upper(s: str) -> str:
    """Convert string to uppercase"""
    if is_string(s):
        return s.upper()

# optionally, ignore function for documentation
def is_string(s: str) -> bool:
    """Check object is a string"""
    return isinstance(s, str)
```

Generating the documentation for this section returns the following dictionary, gathering the following metadata using the `inspect` package.

```python
{
    "context": {
        "String Operations": {
            "str_to_lower": {
                "docstring": "Convert string to lowercase",
                "annotations": {"s": str, "return": str}
            },
            # ... other functions tagged "String Operations" ...
        },
        # ... other sections ...
    }
}
```

This dictionary can be easily traversed to populate a Jinja Template. Ideally, the structure of the `context` dictionary provides a similar structure as the templates, almost acting as a table of contents within Python.


### Upcoming

Currently, there is no support for nested functions; only top-level functions within a module.

Think of an idea? Feel free to suggest it in the `Issues` tab or create a `Pull Request`.


### Information

**Author**: Lucas Nelson

**Developed**: June 17, 2024

**Last Updated**: June 17, 2024

**Motivation**: Manual documentation procedures at workplace
