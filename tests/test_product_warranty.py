# This file is part of the product_warranty module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class ProductWarrantyTestCase(ModuleTestCase):
    'Test Product Warranty module'
    module = 'product_warranty'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        ProductWarrantyTestCase))
    return suite
