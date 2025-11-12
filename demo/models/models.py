import re
from odoo import models, fields, api


class User(models.Model):
    _inherit = 'res.users'
    hobby = fields.Many2one('demo.hobby', string='Favorite Hobby')
    hobbies = fields.Many2many('demo.hobby', string='Hobbies', relation='demo_user_hobby', column1='user_id', column2='hobby_id')
    description = fields.Char(string='Description', required=True, default="Descritpion par défaut.")

    def create(self, vals):
        return super(User, self).create(vals)
                                        
    @api.constrains('description')
    def _description_is_one_line(self):
        for user in self:
            if user.description and "/n" in user.description:
                raise ValueError(f'Description must be oneline, got `{user.description}`')
    @api.constrains('description')
    def _description_is_required(self):
        for user in self:
            if not user.description:
                raise ValueError(f'Description must not be empty, got `{user.description}`')

class Hobby(models.Model):
    _name = 'demo.hobby'
    _description = 'Topic'

    name = fields.Char(string='Name', required=True)
