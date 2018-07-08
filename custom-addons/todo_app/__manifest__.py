{
    'name':'ToDo Application',
    'description':'Manage To-Do Tasks',
    'author': 'Joey',
    'depends': ['base'],
    'application': True,
    'data': [
        'security/ir.model.access.csv',
        'security/todo_access_rules.xml',
        'views/todo_menu.xml',
        'views/todo_view.xml',
        'views/measure_view.xml',
        ],
}
