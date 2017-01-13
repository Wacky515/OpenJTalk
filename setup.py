# -*- coding: utf-8 -*-

from distutils.core import setup
import py2exe, sys

sys.argv.append("py2exe")

setup(
        options={"py2exe": {"bundle_files": 3}},
        zipfile=None,
        # console=[{"script": "recordvideo.py"}]
        console=[{"script": "openjtalk.py"}]
        # console=[{"script": "recordctrl.py"}]
)
