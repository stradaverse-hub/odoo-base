# -*- coding: utf-8 -*-

import base64
from odoo.http import Controller, request, route
from werkzeug.utils import redirect

DEFAULT_IMAGE = 'stradaverse_login_bg/static/src/img/default_background.png'


class LoginBackground(Controller):

    @route(['/bg_image'], type='http', auth="public")
    def bg_image(self, **post):
        user = request.env.user
        company = user.company_id
        if company.bg_image:
            image = base64.b64decode(company.bg_image)
        else:
            return redirect(DEFAULT_IMAGE)

        return request.make_response(
            image, [('Content-Type', 'image')])
