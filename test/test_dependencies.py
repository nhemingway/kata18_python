#!/usr/bin/env python

import unittest

from dependencies import Dependencies

class TestDependencies(unittest.TestCase):
    def test_basic(self):
        dep = Dependencies()
        dep.add_direct('A', 'B C'.split() )
        dep.add_direct('B', 'C E'.split() )
        dep.add_direct('C', 'G'.split() )
        dep.add_direct('D', 'A F'.split() )
        dep.add_direct('E', 'F'.split() )
        dep.add_direct('F', 'H'.split() )

        self.assertEqual( 'G'.split(),             dep.dependencies_for('C'))
        self.assertEqual( 'H'.split(),             dep.dependencies_for('F'))
        self.assertEqual( 'F H'.split(),           dep.dependencies_for('E'))
        self.assertEqual( 'B C E F G H'.split(),   dep.dependencies_for('A'))
        self.assertEqual( 'C E F G H'.split(),     dep.dependencies_for('B'))
        self.assertEqual( 'A B C E F G H'.split(), dep.dependencies_for('D'))

    def test_recursive(self):
        dep = Dependencies()
        dep.add_direct('A', 'B'.split() )
        dep.add_direct('B', 'C'.split() )
        dep.add_direct('C', 'A'.split() )

        with self.assertRaises( ValueError ) as cm:
            dep.dependencies_for('C')

        the_exception = cm.exception
        self.assertEqual(the_exception.message, 'Recursive dependency found: A -> B -> C -> A')
