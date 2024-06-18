## {{ section_name }}

| Function | Description | Signature | Examples |
| :-: | :-: | :-: | :-: |
{% for function_name, function_info in functions_context.items() %}
| {{ function_name }} | {{ function_info.get("docstring") | clean_documentation }} | {{ function_info.get("annotations") }} |  |
{% endfor %}
