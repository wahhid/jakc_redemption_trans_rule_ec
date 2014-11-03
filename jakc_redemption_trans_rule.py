from openerp.osv import fields, osv

SCHEMAS_SELECTIONS = [
    ('birthday','Birthday'),
    ('gender','Gender'),
    ('day','Day'),
    ('dayname','Day Name'),
    ('cardtype','Card Type'),
    ('tenant','Tenant'),
    ('tenanttype','Tenant Type'),
    ('bankcard','Bank Card'),
    ('age','Customer Age')
]

OPERATOR_SELECTIONS = [
    ('eq','Equal'),
    ('ne','Not Equal'),
    ('lt','Less Than'),
    ('gt','Greater Than'),
    ('bw','Between'),
]

DAY_NAME_SELECTIONS = [
    ('01','Sunday'),
    ('02','Monday'),
    ('03','Tuesday'),
    ('04','Wednesday'),
    ('05','Thursday'),
    ('06','Friday'),
    ('07','Saturday')
]

class rdm_rules(osv.osv):
    _name = "rdm.rules"
    _description = "Redemption Rules"
    _columns = {
        'name': fields.char('Name', size=200, required=True),
        'apply_for': fields.selection([('1','Coupon'),('2','Point')],'Apply For',required=True),
        'rule_schema': fields.selection(SCHEMAS_SELECTIONS,'Schema',required=True),           
        'birthday': fields.boolean('Birthday'),
        'gender': fields.many2one('rdm.customer.gender','Gender'),                
        'day': fields.date('Day'),    
        'day_name': fields.selection(DAY_NAME_SELECTIONS,'Day Name'),           
        'card_type_ids': fields.one2many('rdm.rules.card.type','rules_id','Card Type'),
        'tenant_ids': fields.one2many('rdm.rules.tenant','rules_id','Tenant'),
        'tenant_category_ids': fields.one2many('rdm.rules.tenant.category','rules_id','Tenant Category'),
        'bank_ids': fields.one2many('rdm.rules.bank','rules_id','Bank'),        
        'age_ids': fields.one2many('rdm.rules.customer.age','rules_id','Age'),
        'operation': fields.selection([('add','Add'),('multiple','Multiple')],'Operation',required=True),
        'calculation': fields.selection([('terbesar','Terbesar'),('ditotal','Di Total')],'Method'),
        'quantity': fields.float('Quantity',required=True),
    }
    
    _defaults = {
        'quantity': lambda *a : 1,
    }
    
rdm_rules()

class rdm_rules_card_type(osv.osv):
    _name = "rdm.rules.card.type"
    _description = "Redemption Rule Card Type"
    _columns = {
        'rules_id': fields.many2one('rdm.rules','Rules ID', readonly=True),
        'card_type_id': fields.many2one('rdm.card.type','Card Type')        
    }
    
rdm_rules_card_type()
    
class rdm_rules_tenant(osv.osv):
    _name = "rdm.rules.tenant"
    _description = "Redemption Rule Tenant"
    _columns = {
        'rules_id': fields.many2one('rdm.rules','Rules ID', readonly=True),
        'tenant_id': fields.many2one('rdm.tenant','Tenant') 
    }

rdm_rules_tenant()

class rdm_rules_customer_age(osv.osv):
    _name = "rdm.rules.customer.age"
    _description = "Redemption Rules Customer Age"
    _columns = {
        'rules_id': fields.many2one('rdm.rules','Rules ID', readonly=True),
        'operator': fields.selection(OPERATOR_SELECTIONS,'Operator',size=16,required=True),
        'value1': fields.integer('Value 01'),
        'value2': fields.integer('Value 02'),         
    }
    
rdm_rules_customer_age()

class rdm_rules_tenant_category(osv.osv):
    _name = "rdm.rules.tenant.category"
    _description = "Redemption Rule Tenant Category"
    _columns = {
        'rules_id': fields.many2one('rdm.rules','Rules ID', readonly=True),
        'tenant_category_id': fields.many2one('rdm.tenant.category','Tenant Category') 
    }

rdm_rules_tenant_category()

class rdm_rules_bank(osv.osv):
    _name = "rdm.rules.bank"
    _description = "Redemption Rule Bank"
    _columns = {
        'rules_id': fields.many2one('rdm.rules','Rules ID', readonly=True),
        'bank_card_id': fields.many2one('rdm.bank','Bank') 
    }
    
class rdm_rules_bank_card(osv.osv):
    _name = "rdm.rules.bank.card"
    _description = "Redemption Rule Bank Card"
    _columns = {
        'rules_id': fields.many2one('rdm.rules','Rules ID', readonly=True),
        'bank_card_id': fields.many2one('rdm.bank.card','Bank Card') 
    }

rdm_rules_bank_card()