project = "gepref"
copyright = "2024, Juan Lara"
author = "Juan Lara"
release = "latest"

extensions = [
        "sphinx.ext.autodoc",
        "sphinx.ext.napoleon",
        "sphinx.ext.viewcode",
        "sphinx_rtd_theme",
        "sphinx.ext.autosummary",
        "recommonmark"
        ]

autodoc_default_flags = ["members", "show-inheritance"]
autosummary_generate = True
source_suffix = {
        ".rst": "restructuredtext",
        ".md": "markdown"
        }

templates_path = ["_templates"]
exclude_patterns = []

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_logo = "_static/gepref.png"
