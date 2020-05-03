##############################################################################
#
#
#
##############################################################################
{ 
	'name' : 'My Web External Layout Test',
	'version' : '0.01 (12.0)',
	'author' : 'Ondrej Vanka',
	'category': 'Enterprise Specific Modules',
	'website': 'http://www.aknavj.com',
	'description': """
		Replace in Settings->General Settings "Document Template" to "ins_external_layout_document" to see changes.
	""",
	'license': 'AGPL-3',
	'depends': [],
	'qweb': [],
	'demo': [],
	'data': [
        'views/external_layout_document.xml',
		'views/external_layout.xml',
	],
	'installable': True,
	'application': True,
	'auto_install': False,
}
