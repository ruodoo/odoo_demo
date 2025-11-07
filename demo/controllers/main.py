from odoo.http import Controller, route, request
from markupsafe import Markup


class Main(Controller):
        @route('/hobby', auth='public')
        def hello(self):
            hobbies = request.env['demo.hobby'].search([])
            content = Markup('<h2>Hello world</h2>')
            for hobby in hobbies:
                content += Markup('<div id="%s">%s</div>') % (hobby.id, hobby.name)
            return content