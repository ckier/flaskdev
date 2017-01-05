# Copyright 2016 Molecular Devices, LLC
# All Rights Reserved.

from flaskdev import create_app
from flask_script import Manager

app = create_app('dev')
manager = Manager(app)

if __name__ == '__main__':
    manager.run()
