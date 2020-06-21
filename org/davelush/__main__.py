import os
import sys

from org.davelush.app import main
from org.davelush.setup_logging import setup_loggers

setup_loggers()

if __name__ == "__main__":
    ret = main(sys.argv[1:], os.environ)
    exit(ret)
