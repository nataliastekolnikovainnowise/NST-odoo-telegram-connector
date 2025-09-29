from odoo import http
from odoo.http import request

class TelegramController(http.Controller):
    @http.route('/telegram_api/customers', type='json', auth='public', methods=['POST'])
    def get_customers(self):
        customers = request.env['res.partner'].sudo().search([], limit=5)
        return [{'id': c.id, 'name': c.name, 'email': c.email or ''} for c in customers]
    
    @http.route('/telegram_api/orders', type='json', auth='public', methods=['POST'])
    def get_orders(self):
        # Проверяем, установлен ли модуль sale
        if 'sale.order' not in request.env:
            return {'error': 'Module sale is not installed'}
        
        orders = request.env['sale.order'].sudo().search([], limit=5)
        return [{'id': o.id, 'name': o.name, 'amount': o.amount_total} for o in orders]
