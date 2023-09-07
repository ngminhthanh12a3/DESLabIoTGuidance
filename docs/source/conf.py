# Configuration file for the Sphinx documentation builder.

# 
import os,sys
sys.path.insert(0,os.path.abspath('../..'))

# -- Project information

project = 'DESLab IoT Training'
copyright = '2023, Thanh'
author = 'Nguyen Vu Minh Thanh'

# release = '0.1'
# version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

# -- Latex for Vietnamese
# Package for latexmk: in .readthedocs.yaml
# Refs: 
# https://www.sphinx-doc.org/en/master/usage/builders/index.html#sphinx.builders.latex.LaTeXBuilder
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-latex-output
# https://www.sphinx-doc.org/en/master/latex.html
latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '12pt',
    'fontenc':'',
    'inputenc': 
    r"""\usepackage[T5]{fontenc}
\usepackage[utf8]{inputenc}
\DeclareTextSymbolDefault{\DH}{T1}
    """,
    'babel': '\\usepackage[vietnamese]{babel}',
}
latex_use_xindy = True
language = 'vi'