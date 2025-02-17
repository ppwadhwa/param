# -*- coding: utf-8 -*-

from nbsite.shared_conf import *

project = u'param'
authors = u'HoloViz developers'
copyright = u'2003-2021 ' + authors
description = 'Declarative Python programming using Parameters'

import param

param.parameterized.docstring_signature = False
param.parameterized.docstring_describe_params = False

version = release = str(param.__version__)

nbbuild_cell_timeout = 600

html_static_path += ['_static']

html_theme = "pydata_sphinx_theme"

html_logo = "_static/logo_horizontal.png"

html_css_files = ['site.css']

html_context.update({
    'PROJECT': project,
    'DESCRIPTION': description,
    'AUTHOR': authors,
    'VERSION': version,
    'theme_google_analytics_id': 'UA-154795830-6',
    'theme_github_url': 'https://github.com/holoviz/param',
})
