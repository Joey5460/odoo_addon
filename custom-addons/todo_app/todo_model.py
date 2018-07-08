# -*- coding: utf-8 -*-
from odoo import models, fields, api
class TodoTask (models.Model):
    _name = 'todo.task'
    _description = 'To-do Task'
    name = fields.Char('Name', required=True, translate=True) 
    num = fields.Char('Number', required=True,translate=True)
    scale = fields.Char('Scale',translate=True)
    acc = fields.Char('Accurate',translate=True)
    manu = fields.Char('Manufacture',translate=True)
    lev_time = fields.Char('Leverage Time',translate=True)
    det_peri= fields.Char('Detection Period',translate=True)
    dur = fields.Char('Duration',required=True)
    dep = fields.Char('Department',translate=True)
    user = fields.Char('User',translate=True)
    comment = fields.Text('Comment',translate=True)
    dt= fields.Date('Date',translate=True)
    det_no= fields.Integer('Detection No.',translate=True)
    result= fields.Boolean('Result',translate=True)
    issue_dep= fields.Char('Issue Dep',translate=True)
    #is_done = fields.Boolean('Done?')
    #active = fields.Boolean('Active?', default=True)

    @api.multi
    def do_toggle_done(self):
        #for task in self:
        #    task.is_done = not task.is_done
        return True

    #@api.model
    @api.multi
    def do_clear_done(self):
        #dones = self.search([('is_done', '=', True)])
        #dones.write({'active': False})
        return True

