# Copyright 2016 Molecular Devices, LLC
# All Rights Reserved.

from flask import Blueprint

main = Blueprint('main', __name__)

from . import views
