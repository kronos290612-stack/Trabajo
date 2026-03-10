{
    'name': 'Commercial Management',
    'version': '1.0',
    'category': 'Human Resources',
    'summary': 'Complete business management, applications, document management and deliveries.',
    'description': """
    Advanced Management of Advances and Expense Settlements
    ======================================================

     """,
    'author': 'KRONOS',
    'website': '',
    'depends': ['account_area_expense', 'hr_expense'],
    'data': [
        'security/ir.model.access.csv',
        'views/account_move_form_header.xml.xml',


            ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
