# © 2013-2014 Nicolas Bessi (Camptocamp SA)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Base Comments Templates",
    "summary": "Add conditional mako template to any report "
    "on models that inherits comment.template.",
    "version": "13.0.3.0.3",
    "category": "Reporting",
    "website": "https://github.com/OCA/reporting-engine",
    "author": "Camptocamp, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "installable": True,
    "depends": ["base", "mail"],
    "development_status": "Mature",
    "data": [
        "security/ir.model.access.csv",
        "security/security.xml",
        "views/base_comment_template_view.xml",
        "views/res_partner_view.xml",
    ],
}
