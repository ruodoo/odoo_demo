from odoo import api, fields, models
from odoo.exceptions import ValidationError


class Partner(models.Model):
    _inherit = 'res.partner'
    hobby = fields.Many2one('demo.hobby', string='Favorite Hobby')
    hobbies = fields.Many2many('demo.hobby', string='Hobbies', relation='demo_user_hobby', column1='user_id', column2='hobby_id')

    @api.constrains('hobby', 'hobbies')
    def _constraint_hobby_in_hobbies(self):
        for partner in self:
            if partner.hobby and partner.hobby not in partner.hobbies:
                e = self.env._("The favorite hobby must be listed in the hobbies.")
                raise ValidationError(e)


class Hobby(models.Model):
    _name = 'demo.hobby'
    _description = 'Topic'

    name = fields.Char(string='Name', required=True)
