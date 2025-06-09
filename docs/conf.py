project = 'UHC Card'
author = 'UHC Card'
release = '1.0.0'

extensions = []
templates_path = []
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'alabaster'
html_static_path = ['_static']
html_extra_path = ['.']  # ✅ This is required to copy index.html

html_show_sourcelink = False
html_theme_options = {
    'show_powered_by': False,
}
