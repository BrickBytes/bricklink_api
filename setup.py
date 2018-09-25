"""
FUMBBL SR Rankings module and scripts
"""

import pathlib
import re

from setuptools import setup


thisdir = pathlib.Path(__file__).parent
srdir = thisdir / "bricklink_api"


with (thisdir / "README.md").open(encoding="utf8") as f:
  readme = f.read()


metadata_pobj = re.compile(r"__([a-z]+)__ = \"([^\"]+)")
with (srdir / "__init__.py").open(encoding="utf8") as f:
  initpy = f.read()
metadata = dict(metadata_pobj.findall(initpy))


setup(
  name = "bricklink_api",
  version = metadata["version"],
  description = "BrickLink API",
  long_description = readme,
  url = "https://github.com/BrickBytes/bricklink_api",
  author = "Szieberth Ádám",
  author_email = "sziebadam@gmail.com",
  license = "MIT",
  classifiers = [
      "Development Status :: 3 - Alpha",
      "Intended Audience :: Developers",
      "License :: OSI Approved :: MIT License",
      "Programming Language :: Python :: 3 :: Only",
      "Programming Language :: Python :: 3.6",
  ],
  keywords = [
      "game",
      "lego",
      "brick",
      "bricklink",
  ],
  packages = ["sr"],
  package_dir = {
      "bricklink_api": "bricklink_api",
  },
  include_package_data = True,
  package_data={
      "": [
          "LICENSE.txt",
          "README.md",
      ],
  },
  install_requires = [
      "requests",
      "requests_oauthlib",
      "yarl",
  ],
  extras_require = {
  },
  scripts = [
  ],
  )
