from odoo import http
from odoo.http import request


class FeedbackController(http.Controller):
    @http.route("/feedback", type="http", auth="public", website=True)
    def feedback_form(self, **kwargs):
        return request.render("feedback_module.s_feedback_module", {})

    @http.route(
        "/submit_feedback",
        type="http",
        auth="public",
        website=True,
        csrf=True,
        methods=["POST"],
    )
    def submit_feedback(self, **post):
        request.env["my.module.feedback"].sudo().create(
            {
                "name": post.get("name"),
                "email": post.get("email"),
                "message": post.get("message"),
            }
        )
        return request.render("feedback_module.thank_you_template", {})
