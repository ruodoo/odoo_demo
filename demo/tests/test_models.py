from psycopg2.errors import NotNullViolation

from odoo.exceptions import ValidationError
from odoo.tests import TransactionCase
from odoo.tools import mute_logger


class TestHobby(TransactionCase):
    def test_name(self):
        hobby = self.env['demo.hobby'].create({
            'name': 'Programming',
        })
        self.assertEqual(hobby.name, 'Programming')

    def test_name_is_required(self):
        with self.assertRaises(NotNullViolation):
            with mute_logger('odoo.sql_db'):
                self.env['demo.hobby'].create({})


class TestPartners(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.partner = cls.env['res.partner'].create({
            'name': 'Marie-Noël',
        })

    def test_hobby(self):
        swimming = self.env.ref('demo.hobby_swimming')
        minecraft = self.env.ref('demo.hobby_minecraft')
        self.partner.write({
            'hobbies': swimming.ids + minecraft.ids,
            'hobby': minecraft.id,
        })
        self.assertEqual(self.partner.hobby.name, 'Minecraft')

    def test_hobby_in_hobbies(self):
        swimming = self.env.ref('demo.hobby_swimming')
        minecraft = self.env.ref('demo.hobby_minecraft')
        with self.assertRaises(ValidationError):
            self.partner.write({
                'hobbies': swimming.ids,
                'hobby': minecraft.id,
            })
