from odoo.tests import HttpCase


class TestBasic(HttpCase):

    def test_new_hobby(self):
        self.env['demo.hobby'].create({
            'name': 'Movies'
        })
        result = self.url_open('/hobby')
        self.assertIn(b'Movies', result.content)

    def test_main(self):
        result = self.url_open('/hobby')
        self.assertNotIn(b'Movies', result.content)
        self.assertIn(b'Gaming', result.content)
