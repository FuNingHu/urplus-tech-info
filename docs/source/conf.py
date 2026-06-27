# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'UR+ Tech Info'
copyright = '2026, Universal Robots A/S'
author = 'UR Development Consultant Team'
version = '1.0'
release = '1.8.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

# -- Custom URScript syntax highlighting -------------------------------------
# Pygments has no built-in URScript lexer. URScript uses ``if ... end`` style
# blocks (unlike Python's indentation), so we register a minimal lexer that
# colours the control keywords, including ``end``.
from pygments.lexer import RegexLexer, words
from pygments.token import (
    Comment, Keyword, Name, Number, Operator, Punctuation, String, Whitespace,
)
from sphinx.highlighting import lexers


class URScriptLexer(RegexLexer):
    name = 'URScript'
    aliases = ['urscript']
    filenames = ['*.script', '*.script']

    tokens = {
        'root': [
            (r'\s+', Whitespace),
            (r'#.*?$', Comment.Single),
            (words((
                'def', 'end', 'if', 'elif', 'else', 'while', 'for', 'thread',
                'return', 'break', 'continue', 'global', 'local', 'halt',
                'sync', 'enter_critical', 'exit_critical', 'in',
            ), suffix=r'\b'), Keyword),
            (words(('and', 'or', 'not', 'xor'), suffix=r'\b'), Operator.Word),
            (words(('True', 'False', 'None'), suffix=r'\b'), Keyword.Constant),
            (r'"(\\.|[^"\\])*"', String.Double),
            (r"'(\\.|[^'\\])*'", String.Single),
            (r'\b\d+\.\d+([eE][+-]?\d+)?\b', Number.Float),
            (r'\b\d+\b', Number.Integer),
            (r'[a-zA-Z_]\w*(?=\s*\()', Name.Function),
            (r'[a-zA-Z_]\w*', Name),
            (r'[+\-*/%=<>!&|^~]+', Operator),
            (r'[\(\)\[\]\{\},:;.]', Punctuation),
        ],
    }


lexers['urscript'] = URScriptLexer()

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_css_files = ['custom.css']

# Copy .nojekyll to output
html_extra_path = ['.nojekyll']

# Theme options
html_theme_options = {
    'navigation_depth': 4,
    'collapse_navigation': False,
    'sticky_navigation': True,
    'includehidden': True,
    'titles_only': False,
}

# Logo
html_logo = 'images/urplus_logo.png'

# Favicon (browser tab icon)
html_favicon = 'images/urplus_logo.png'

# -- Sphinx Multiversion Configuration ---------------------------------------
# Whitelist pattern for tags (e.g., v0.1.0, v1.0.0)
smv_tag_whitelist = r'^v\d+\.\d+\.\d+$'

# Whitelist pattern for branches
smv_branch_whitelist = r'^(main|master)$'

# Pattern for released versions
smv_released_pattern = r'^tags/v\d+\.\d+\.\d+$'

# Format for versioned output directories
smv_outputdir_format = '{ref.name}'

# Show warning banner for old versions
smv_latest_version = 'main'

# HTML context for version selector
html_context = {
    'display_github': True,
    'github_user': 'funinghu',
    'github_repo': 'urplus-tech-info',
    'github_version': 'main',
    'conf_py_path': '/docs/source/',
}
