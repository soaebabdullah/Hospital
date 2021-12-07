from odoo import models, fields


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Patient Record'

    patient_name = fields.Char(string='Name', required=True)
    patient_age = fields.Integer('Age')
    test = fields.Text(string='Test Documents')
    image = fields.Binary(string='Report Image')
    name = fields.Char(string="Pathologist Name ")
