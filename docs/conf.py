import os
import re
import sys

sys.path.insert(0, os.path.abspath(".."))


extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "sphinxcontrib_trio",
    "sphinx_rtd_theme",
]

autodoc_member_order = "groupwise"
autodoc_typehints = "none"

extlinks = {
    "issue": ("https://github.com/ShineyDev/screen/issues/%s", "#"),
}

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}

highlight_language = "python3"
html_theme = "sphinx_rtd_theme"
master_doc = "index"
pygments_style = "friendly"
source_suffix = ".rst"

copyright = "2021-present, ShineyDev"
project = "screen"

with open("../screen/__init__.py", "r") as file_stream:
    version = re.search(r"^version = [\"]([^\"]*)[\"]", file_stream.read(), re.MULTILINE).group(1)

release = version
