project = "gepref"
copyright = "2024, Juan Lara"
author = "Juan Lara"
release = "latest"

extensions = [
        "sphinx.ext.autodoc",
        "sphinx.ext.napoleon",
        "sphinx.ext.viewcode",
        "sphinx.ext.autosummary",
        "myst_parser"
        ]

autodoc_default_flags = ["members", "show-inheritance"]
autosummary_generate = True
source_suffix = {
        ".rst": "restructuredtext",
        ".md": "markdown"
        }

templates_path = ["_templates"]
exclude_patterns = []

html_theme = "sphinx_book_theme"
html_theme_options = {
        "repository_url": "https://github.com/juselara1/gepref",
        "use_repository_button": True
        }
html_static_path = ["_static"]
html_title = "gepref"
html_logo = "_static/gepref.svg"
