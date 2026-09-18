project = 'TeleBid Research'
author = 'Искандар Гарифуллин'
copyright = '2026, Искандар Гарифуллин'

extensions = [
    'myst_parser',
]

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}
master_doc = 'index'
language = 'ru'
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'furo'
html_title = 'TeleBid Research — НИР-2'
html_static_path = ['_static']
html_css_files = ['custom.css']
html_show_sourcelink = False
html_show_sphinx = False

html_theme_options = {
    'sidebar_hide_name': True,
    'navigation_with_keys': True,
}

myst_enable_extensions = [
    'colon_fence',
    'deflist',
    'dollarmath',
    'html_admonition',
    'html_image',
]
