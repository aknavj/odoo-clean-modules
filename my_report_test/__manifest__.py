##############################################################################
#
# Clear / Blank Report Template for Sale order
# Author: @aknavj
#
##############################################################################
{ 
	'name' : 'My Report Test',
	'version' : '0.01 (12.0)',
	'author' : 'Ondrej Vanka',
	'category': 'Enterprise Specific Modules',
	'website': 'http://aknavj.com',
	'description': """
		My Report Test Module
	""",
	'license': 'AGPL-3',
	'depends': ['sale',],
	'qweb': [],
	'demo': [],
	'data': [
        'data/sale_report_paper_format.xml',
		'report/report.xml',
		'report/report_template.xml',
		'views/sale_order_view.xml'
	],
	'installable': True,
	'application': True,
	'auto_install': False,
}