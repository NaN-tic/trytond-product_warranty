# This file is part of the product_warranty module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import Pool
from . import product


def register():
    Pool.register(
        product.ProductWarrantyInstruction,
        product.ProductSupplier,
        module='product_warranty', type_='model')
