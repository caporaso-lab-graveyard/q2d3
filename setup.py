# ----------------------------------------------------------------------------
# Copyright (c) 2016--, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
# ----------------------------------------------------------------------------

import glob
from setuptools import find_packages, setup

setup(
    name='q2ui-q2d3',
    version='0.0.1.dev0',
    packages=find_packages(),
    scripts=glob.glob('scripts/*'),
    install_requires=['click', 'python-frontmatter', 'pyyaml',
                      'qiime >= 2.0.0', 'tornado', 'ipymd >= 0.1.2'],
    package_data={'q2d3': ['static/*']}
)
