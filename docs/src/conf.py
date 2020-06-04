#
# Copyright 2019 is-land
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


import ConfigParser
import StringIO
import os

ohara_version = '0.11.0-SNAPSHOT'

# Branch name(e.g. master or 0.9.x) or Tag name(e.g. 0.9.0)
# Used as variable $|branch| in the contents, code blocks or links.
ohara_branch = 'master'


# -- Ultimate Replace -----------
# A Sphinx hack for string replacement in directive block
# https://github.com/sphinx-doc/sphinx/issues/4054#issuecomment-329097229

def ultimate_replace(app, docname, source):
    result = source[0]
    for key in app.config.ultimate_replacements:
        result = result.replace(key, app.config.ultimate_replacements[key])
    source[0] = result


def setup(app):
    app.add_config_value('ultimate_replacements', {}, True)
    app.connect('source-read', ultimate_replace)


ultimate_replacements = {
    "$|version|": ohara_version,
    "$|branch|": ohara_branch
}


# -- Project information -----------------------------------------------------

project = u'Ohara-Quickstart'
copyright = u'2019, is-land Systems. Version: ' + ohara_version + '(branch: ' + ohara_branch + ')'
author = u'is-land Systems'

# The short X.Y version
version = ohara_version

# The full version, including alpha/beta/rc tags
release = ohara_version


print("=" * 40)
print("Ohara version: %s" % ohara_version)
print("Ohara branch/tag: %s" % ohara_branch)
print("=" * 40)

# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'recommonmark',
    'sphinx.ext.todo',
    'sphinx.ext.extlinks',
    'sphinx_tabs.tabs'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = {
    '.rst': 'restructuredtext'
}

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['build', 'Thumbs.db', '.DS_Store']


# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# Use Read the Docs Sphinx Theme: https://sphinx-rtd-theme.readthedocs.io/en/latest
html_theme = "sphinx_rtd_theme"
html_theme_path = ["_themes", ]

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'Oharadoc'


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'ohara', u'Ohara Documentation',
     [author], 1)
]

# -- extlinks ----------------------------------------------------------------
#   https://www.sphinx-doc.org/en/master/usage/extensions/extlinks.html#module-sphinx.ext.extlinks

extlinks = {
    'ohara-issue': ('https://github.com/oharastream/ohara/issues/%s', '#'),
    'ohara-source': ('https://github.com/oharastream/ohara/blob/%s/' % ohara_branch + "%s", ''),
    'kafka-issue': ('https://issues.apache.org/jira/browse/KAFKA-%s', 'KAFKA-'),
    'zookeeper-issue': ('https://issues.apache.org/jira/browse/ZOOKEEPER-%s', 'ZOOKEEPER-'),
    'k8s-issue': ('https://github.com/kubernetes/kubernetes/issues/%s', '#')
}


# -- rst_prolog --------------------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-rst_prolog
rst_prolog = """
.. |branch| replace:: %s
""" % (ohara_branch)
