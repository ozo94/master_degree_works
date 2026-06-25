# -*- coding: utf-8 -*-
"""Create an application instance."""
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from flask.helpers import get_debug_flag
from dataDisplay.app import create_app
from dataDisplay.settings import DevConfig, ProdConfig

CONFIG = DevConfig if get_debug_flag() else ProdConfig

app = create_app(CONFIG)


if __name__ =='__main__':
    app.run()