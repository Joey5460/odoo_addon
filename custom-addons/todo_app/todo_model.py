# -*- coding: utf-8 -*-
from odoo import models, fields, api
class TodoTask (models.Model):
    _name = 'todo.task'
    _description = 'To-do Task'
    name = fields.Char('Name', required=True) 
    num = fields.Char('Number', required=True)
    scale = fields.Char('Scale')
    acc = fields.Char('Accurate')
    manu = fields.Char('Manufacture')
    lev_time = fields.Char('Leverage Time')
    det_peri= fields.Char('Detection Period')
    exp = fields.Char('Expiration',required=True)
    dep = fields.Char('Department')
    user = fields.Char('User')
    comment = fields.Text('comment')
    dt= fields.Date('Date')
    det_no= fields.Integer('Detection No.')
    result= fields.Boolean('Result')
    issue_dep= fields.Boolean('Issue Dep')
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

