# Copyright 2016 Molecular Devices, LLC
# All Rights Reserved.

import os
from flaskdev import create_app
from flask_script import Manager

app = create_app(os.getenv('FLASKDEV_ENV') or 'dev')
manager = Manager(app)

if __name__ == '__main__':
    manager.run()
