__title__ = "pyhidentity"
__version_info__ = ('1', '0', '0')
__version__ = ".".join(__version_info__)
__author__ = "Christian Bierschneider"
__email__ = "christian.bierschneider@web.de"
__license__ = "MIT"

import os
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# set library modules
from pyhidentity.tor.tor import Tor
from pyhidentity.tor_request import TorRequest
from pyhidentity.proxy_request import ProxyRequest
from pyhidentity.utils.ip_analyzer import IPAnalyzer
from pyhidentity.utils.logger import Logger