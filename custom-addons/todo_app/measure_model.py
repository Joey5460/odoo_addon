# -*- coding: utf-8 -*-
from odoo import models, fields, api
class TodoTask (models.Model):
    _name = 'measure.task'
    _description = 'Measure Task'
    name = fields.Char('Name', required=True, translate=True) 
    p_a= fields.Char('PointA',translate=True )
    p_b= fields.Char('PointB' ,translate=True)
    num = fields.Char('Number' ,required=True,translate=True)
    process= fields.Char('Process',translate=True)
    dur = fields.Char('Duration',required=True,translate=True)
    exp = fields.Date('Expiration',required=True,translate=True)
    cali = fields.Date('Cali Date',required=True,translate=True)
    li_num = fields.Date('Licence Number',required=True,translate=True)

