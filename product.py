# This file is part of the product_warranty module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.model import ModelView, ModelSQL, fields
from trytond.pool import Pool, PoolMeta

__all__ = ['ProductWarrantyInstruction', 'ProductSupplier']


class ProductWarrantyInstruction(ModelSQL, ModelView):
    'Product Warranty Instruction'
    __name__ = 'product.warranty.instruction'
    name = fields.Char('Title', required=True)
    instructions = fields.Text('Instructions',
        help='Instructions for product return')
    is_default = fields.Boolean('Default',
        help='If this warranty is the default one, it will be used to set the '
        'default value in supplier info. Be careful to have only one '
        'default.')


class ProductSupplier(metaclass=PoolMeta):
    __name__ = 'purchase.product_supplier'
    warranty_duration = fields.Float('Warranty',
        help='Warranty in months for this product/supplier relation.')
    warranty_return_partner = fields.Selection([
        ('', ''),
        ('company', 'Company'),
        ('supplier', 'Supplier'),
        ('other', 'Other'),
        ], 'Warrantee return', help='Who is in charge of the warranty return '
        'treatment towards the end customer.')
    warranty_instructions = fields.Many2One('product.warranty.instruction', 'Instructions',
        help='Instructions for product return.')

    @staticmethod
    def default_warranty_return_partner():
        return 'company'

    @staticmethod
    def default_warranty_instructions():
        Warranty = Pool().get('product.warranty.instruction')
        warranties = Warranty.search([('is_default', '=', True)])
        if warranties:
            warranty, = warranties
            return warranty.id
