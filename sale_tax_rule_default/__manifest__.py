{
    'name': 'Apply Global Tax to Quotations',
    'version': '17.0',
    'summary': 'Apply a global tax to all order lines in one click',
    'description': 'This module adds a “Global Tax” field in sales quotations. When you select a tax in this field, it will automatically be applied to all order lines, helping you save time and avoid mistakes.',
    'author': 'Kone Adama',
    'website': 'https://kone-adama.com/',
    'category': 'Sales',
    'depends': ['sale'],
    'data': [
        'views/sale_order_view.xml',
    ],
    'images': ['static/description/icon.png'],  # ← cette ligne est importante
    'installable': True,
    'application': False,
    'license': 'OPL-1',
    'price': 49.99,
    'currency': 'USD'
}
