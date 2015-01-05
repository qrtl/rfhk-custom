# -*- coding: utf-8 -*-


import netsvc
from tools.translate import _
import openerp.addons.decimal_precision as dp
from datetime import datetime
from osv import fields, osv
import time


 
class new_fields_project(osv.osv):
    
    def _releasing_count(self, cr, uid, ids, field_name, arg, context=None):
        res = dict.fromkeys(ids, 0)
        releasing_ids = self.pool.get('project.releasing').search(cr, uid, [('project_id', 'in', ids)])
        for releasing in self.pool.get('project.releasing').browse(cr, uid, releasing_ids, context):
            if releasing.step not in ('done', 'refused'):
                res[releasing.project_id.id] += 1
        return res
     
    _inherit = 'project.project'
 
    _columns = {
           'releasing_count': fields.function(_releasing_count, type='integer', string="Releasing in Progress"),
           'technical_manager': fields.many2one('res.users', 'Technical Manager'),
           
    }
 
new_fields_project()

class new_fields_task(osv.osv):
    
    def _releasing_count(self, cr, uid, ids, field_name, arg, context=None):
        res = dict.fromkeys(ids, 0)
        releasing_ids = self.pool.get('project.releasing').search(cr, uid, [('task_id', 'in', ids)])
        for releasing in self.pool.get('project.releasing').browse(cr, uid, releasing_ids, context):
            if releasing.step not in ('done', 'refused'):
                res[releasing.task_id.id] += 1
        return res
    
    _inherit = 'project.task'
    _columns = {
           'releasing_count': fields.function(_releasing_count, type='integer', string="Releasing in Progress"),
           
    }
 
new_fields_task()

class new_fields_issue(osv.osv):
    
    def _releasing_count(self, cr, uid, ids, field_name, arg, context=None):
        res = dict.fromkeys(ids, 0)
        releasing_ids = self.pool.get('project.releasing').search(cr, uid, [('issue_id', 'in', ids)])
        for releasing in self.pool.get('project.releasing').browse(cr, uid, releasing_ids, context):
            if releasing.step not in ('done', 'refused'):
                res[releasing.issue_id.id] += 1
        return res
     
    _inherit = 'project.issue'
    _columns = {
           'releasing_count': fields.function(_releasing_count, type='integer', string="Releasing in Progress"),
           
    }
 
new_fields_issue()

class project_releasing(osv.osv):



    def _is_pm(self, cr, uid, ids, field, args, context=None):
        res = {}
        for rec in self.browse(cr, uid, ids, context=context):
            res[rec.id] = {
                'is_tm': False,
                'is_pm': False,
            }
            if rec.technical_manager.id == uid:
                res[rec.id]['is_tm'] = True
                
            if rec.project_manager.id == uid:
                res[rec.id]['is_pm'] = True
        return res
    

    
    def _tm(self, cr, uid, ids, field, args, context=None):
        res = {}
        for release in self.browse(cr, uid, ids, context=context):
#            if release.project_id.technical_manager:
            group_obj = self.pool.get('res.groups')
            group_id = group_obj.search(cr,uid,[('name','=','Technical Manager')])
            users = self.pool.get('res.groups').read(cr,uid,group_id[0])['users']
            res[release.id] = {
                'tm_ids': users,
                
            }
#            else:
#                raise osv.except_osv(('Warning'),_('No Technical Manager!'))
        return dict.fromkeys(ids, users)
    
    def _pm(self, cr, uid, ids, field, args, context=None):
        res = {}
        for release in self.browse(cr, uid, ids, context=context):
            group_obj = self.pool.get('res.groups')
            group_id = group_obj.search(cr,uid,[('category_id','=',5),('name','=','Manager')])
            users = self.pool.get('res.groups').read(cr,uid,group_id[0])['users']
            res[release.id] = {
                'pm_ids': users,
                
            }
        return dict.fromkeys(ids, users)





             
    _name="project.releasing"
    _description="Project Releasing"
    
    def _check_project(self, cr, uid, ids, context=None):
        for release in self.browse(cr, uid, ids, context=context):
            if  release.type == 'task':
                if release.task_id.project_id  != release.project_id:  
                    raise osv.except_osv(('Warning'),_('Project Changing!'))
            if release.type == 'issue':
                if release.issue_id.project_id  != release.project_id:
                    raise osv.except_osv(('Warning'),_('Project Changing!'))
        return True

    
    _constraints = [(_check_project,_('Project Changing!'),['project_id']),]
    _inherit = ['mail.thread', 'ir.needaction_mixin']
    _order = "planned_date, actual_date"


        
    _columns ={

        'tm_ids': fields.function(_tm,type='char',invisible=True),
        'pm_ids': fields.function(_pm,type='char',invisible=True),
        'tm_approved': fields.boolean('TM Approved', readonly=True),
        'pm_approved': fields.boolean('PM Approved', readonly=True),
        'tm_approve_date':fields.datetime('Approved Date', readonly=True),
        'pm_approve_date':fields.datetime('Approved Date', readonly=True), 
        'technical_manager':fields.many2one('res.users','Technical Manager'),
        'project_manager':fields.many2one('res.users','Project Manager',),
        'assignee': fields.many2one('res.users', 'Responsible',required=True),
        'release_number':fields.char('NO.',readonly=True, size=64, select=True,),
        'id': fields.integer('ID', readonly=True),
        'name': fields.char('Summary',size=128,required=True),
        'planned_date':fields.datetime('Planned Date', select=True,required=True),
        'actual_date':fields.datetime('Actual Date', select=True),
        'background': fields.text('Background',required=True),  
        'content': fields.text('Release Content',required=True),
        'task_id': fields.many2one('project.task', 'Task', domain="[('project_id','=',project_id)]"),
        'issue_id': fields.many2one('project.issue', 'Issue', domain="[('project_id','=',project_id)]"),
        'project_id':fields.many2one('project.project', 'Project',),
        'type': fields.selection([
            ('task', 'Task'),
            ('issue', 'Issue'),], 'Type',),
        'step': fields.selection([
            ('draft', 'New'),
            ('refused', 'Refused'),
            ('confirm', 'Waiting Approval'),
            ('accepted1', 'TM Approved'),
            ('accepted2', 'PM Approved'),
            ('released', 'Released'),
#            ('released1', '...'),
            ('done', 'Done'),
            
            ], 'Step', track_visibility='onchange'),
        'is_tm': fields.function(_is_pm, method=True, type='boolean', string='Is TM', multi="judge_user"),
        'is_pm': fields.function(_is_pm, method=True, type='boolean', string='Is PM', multi="judge_user"),
        'categ_ids': fields.many2many('project.category', string='Tags'),
        }
    
    _defaults = {
        'release_number': lambda obj, cr, uid, context: '',
        'step': 'draft',
        'assignee': lambda obj, cr, uid, context: obj.pool.get('hr.employee').search(cr, uid, [('user_id', '=', uid)]), 

    }
    
        


            
    def create(self, cr, uid, vals, context=None, ):
        if vals.get('release_number','/')=='/':
            vals['release_number'] = self.pool.get('ir.sequence').get(cr, uid, 'release.sequence.number') or '/'
        
        release =  super(project_releasing, self).create(cr, uid, vals, context=context)
        return release    
        
    
    def copy(self, cr, uid, id, default=None, context=None):
        if not default:
            default = {}
        default.update({
            
            'release_number': self.pool.get('ir.sequence').get(cr, uid, 'release.sequence.number'),
        })
        return super(project_releasing, self).copy(cr, uid, id, default, context=context)
    

    
    def releasing_confirm(self, cr, uid, ids, context=None):
        for release in self.browse(cr, uid, ids):
            if release.project_manager:
                self.message_subscribe_users(cr, uid, [release.id], user_ids=[release.project_manager.id])
            if release.technical_manager:
                self.message_subscribe_users(cr, uid, [release.id], user_ids=[release.technical_manager.id])
#                self.message_post(cr, uid, [release.id], body=("test"),subtype="project_releasing.mt_tec_approved", context=context)
        return self.write(cr, uid, ids, {'step': 'confirm', },context=context)

    def releasing_accept1(self, cr, uid, ids, context=None):
#        for release in self.browse(cr, uid, ids):
#            if release.project_manager and release.technical_manager:
#                self.message_subscribe_users(cr, uid, [release.id], user_ids=[release.project_manager.id])
        return self.write(cr, uid, ids, {'step': 'accepted1','tm_approved': True, 'tm_approve_date': datetime.today().strftime('%Y-%m-%d %H:%M:%S')}, context=context)   
    def releasing_accept2(self, cr, uid, ids, context=None):
        return self.write(cr, uid, ids, {'step': 'accepted2', 'pm_approved': True, 'pm_approve_date': datetime.today().strftime('%Y-%m-%d %H:%M:%S')}, context=context)
    
    def releasing_release(self, cr, uid, ids, context=None):
        for release in self.browse(cr, uid, ids):
            if release.step == 'released' and release.pm_approve_date == False and release.tm_approve_date != False:
                self.write(cr, uid, ids, {'pm_approved': True, 'pm_approve_date': datetime.today().strftime('%Y-%m-%d %H:%M:%S')}, context=context)
            if release.step == 'released' and release.tm_approve_date == False and release.pm_approve_date != False:
                self.write(cr, uid, ids, {'tm_approved': True, 'tm_approve_date': datetime.today().strftime('%Y-%m-%d %H:%M:%S')}, context=context)
        return self.write(cr, uid, ids, {'step': 'released'}, context=context)
    
    
    def releasing_refused(self, cr, uid, ids, context=None):
        return self.write(cr, uid, ids, {'step': 'refused','tm_approved': False, 'pm_approved': False, 'tm_approve_date': False, 'pm_approve_date': False}, context=context)
    
    def releasing_done(self, cr, uid, ids, context=None):
        return self.write(cr, uid, ids, {'step': 'done', 'actual_date': time.strftime('%Y-%m-%d'),}, context=context)
    
    def task_project_manager(self,cr,uid,ids,name,arg,context=None):
        res = {}
        for record in self.pool.get('project.task').browse(cr, uid, ids, context=context):
            res[record.id] = record.project_id.user_id
        return res    
    def task_technical_manager(self,cr,uid,ids,name,arg,context=None):
        res = {}
        for record in self.pool.get('project.task').browse(cr, uid, ids, context=context):
            res[record.id] = record.project_id.technical_manager
        return res
    def issue_project_manager(self,cr,uid,ids,name,arg,context=None):
        res = {}
        for record in self.pool.get('project.issue').browse(cr, uid, ids, context=context):
            res[record.id] = record.project_id.user_id
        return res    
    def issue_technical_manager(self,cr,uid,ids,name,arg,context=None):
        res = {}
        for record in self.pool.get('project.issue').browse(cr, uid, ids, context=context):
            res[record.id] = record.project_id.technical_manager
        return res

    
    def onchange_project(self, cr, uid, id, project_id, context=None):
        if project_id:
            project = self.pool.get('project.project').browse(cr, uid, project_id, context=context)
            if project:
                return {'value': {'technical_manager': project.technical_manager.id, 'project_manager':project.user_id.id}}
        return {}


    def onchange_task(self, cr, uid, id, task_id, context=None):
        if task_id:
            task = self.pool.get('project.task').browse(cr, uid, task_id, context=context)
            if task and task.project_id:
                return {'value': {'project_id': task.project_id.id}}
        return {}
    
    def onchange_issue(self, cr, uid, id, issue_id, context=None):
        if issue_id:
            issue = self.pool.get('project.issue').browse(cr, uid, issue_id, context=context)
            if issue and issue.project_id:
                return {'value': {'project_id': issue.project_id.id}}
        return {}
    

project_releasing()    
