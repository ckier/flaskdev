# Copyright 2016 Molecular Devices, LLC
# All Rights Reserved.

from flask import url_for
import flaskdev
from flask_testing import TestCase


class TestFlaskdev(TestCase):

    def create_app(self):
        return flaskdev.create_app('test')

    def test_index(self):
        response = self.client.get(url_for('main.index'))
        self.assert200(response)

    def test_page_not_found(self):
        response = self.client.get('/bad_url/')
        self.assert404(response)

