# -*- coding: utf-8 -*-

"""
OpenEA is a package for embedding-based entity alignment.

"""

__version__ = '0.1-dev'

__title__ = 'openea'
__description__ = "A package for embedding-based entity alignment"
__url__ = 'https://github.com/nju-websoft/EEA.git'
__author__ = 'Zequn Sun'
__email__ = 'zqsun.nju@gmail.com'
__license__ = 'MIT License'
__copyright__ = 'Copyright (c) 2019 websoft'

from tensorflow.compat.v1 import disable_v2_behavior

disable_v2_behavior()

from openea import modules
from openea import models
from openea import approaches
