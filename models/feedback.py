from odoo import models, fields


class Feedback(models.Model):
    _name = "my.module.feedback"
    _description = "Website Feedback"

    name = fields.Char("Your Name", required=True)
    email = fields.Char("Your Email", required=True)
    message = fields.Char("Feedback Message", required=True)
