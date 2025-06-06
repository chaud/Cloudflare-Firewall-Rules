__title__ = "cf_rules"
__description__ = "A Cloudflare wrapper to bulk add / edit your WAF custom rules using Cloudflare's API."
__url__ = "https://quentiumyt.github.io/Cloudflare-Firewall-Rules/"
__version__ = "2.1.0"

__author__ = "Quentin Lienhardt"
__author_email__ = "pro@quentium.fr"
__license__ = "Apache 2.0"
__copyright__ = "Copyright 2025 Quentin Lienhardt"

__all__ = (
    "Cloudflare",
    "Utils",
    "Error",
)

from .cf import Cloudflare
from .utils import Utils
from .error import Error
