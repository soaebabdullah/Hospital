from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

# Inheriting the Sale Order Model and Adding New Field
class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'

    patient_name = fields.Char(string='Patient Name')


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Patient Record'
    _rec_name = 'patient_name'

    @api.constrains('patient_age')
    def check_age(self):
        for rec in self:
            if rec.patient_age <=5:
                raise ValidationError(
                    "Age Is Must Be  Greater Then 5"
                )

    # Write Compute Field and its Function
    @api.depends('patient_age')
    def set_age_group(self):
        for rec in self:
            rec.age_group = 'major'
            if rec.patient_age:
                if rec.patient_age < 18:
                    rec.age_group = 'minor'

    # Creating Sequence
    @api.model
    def create(self, vals):
        if vals.get('name_seq', _('New')) == _('New'):
            vals['name_seq'] = self.env['ir.sequence'].next_by_code('hospital.patient.sequence') or _('New')

        result = super(HospitalPatient, self).create(vals)
        return result

    patient_name = fields.Char(string="Name", required=True, track_visibility="always")
    patient_age = fields.Integer('Age', track_visibility="always")
    test = fields.Text(string="Test Report")
    image_1920 = fields.Image("Image")
    image = fields.Binary(string="Patient Image")
    name = fields.Char(string="Pathologist Name ")
    name_seq = fields.Char(string="Patient ID", required=True, copy=False, readonly=True,
                           index=True, default=lambda self: _('New'))
    gender = fields.Selection([
        ('male', 'Male'),
        ('fe_male', 'Female'),
    ], default='male', string="Gender")
    age_group = fields.Selection([
        ('major', 'Major'),
        ('minor', 'Minor'),
    ], string="Age Group", compute='set_age_group', store=True)

