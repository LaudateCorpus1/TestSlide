# Copyright (c) Facebook, Inc. and its affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

import asyncio
import csv
import testslide
import unittest
import sys


class SomeClass:
    @staticmethod
    def do_something():
        return "original"

    @staticmethod
    async def async_do_something():
        return "original"


class IntMatcherTest(testslide.TestCase):

    def testAnyInt(self):
        self.assertEqual(testslide.matchers.AnyInt(), 666)
        self.assertEqual(testslide.matchers.AnyInt(), 42)
        self.assertNotEqual(testslide.matchers.AnyInt(), "derp") 

    def test_ThisInt(self):
        self.assertEqual(testslide.matchers.ThisInt(666), 666)
        self.assertNotEqual(testslide.matchers.ThisInt(69), 42)
        self.assertNotEqual(testslide.matchers.ThisInt(42), "derp")
    
    def test_NotThisInt(self):
        self.assertEqual(testslide.matchers.NotThisInt(666), 42)
        self.assertNotEqual(testslide.matchers.NotThisInt(69), 69)
        self.assertNotEqual(testslide.matchers.NotThisInt(42), "derp")

    def test_IntBetween(self):
        self.assertEqual(testslide.matchers.IntBetween(21, 666), 42)
        self.assertEqual(testslide.matchers.IntBetween(21, 666), 21)
        self.assertEqual(testslide.matchers.IntBetween(21, 666), 666)
        self.assertNotEqual(testslide.matchers.IntBetween(42, 69), 666)
        self.assertNotEqual(testslide.matchers.IntBetween(42, 69), "derp")

    def test_IntGreater(self):
        self.assertEqual(testslide.matchers.IntGreater(21), 42)
        self.assertNotEqual(testslide.matchers.IntGreater(21), 21)
        self.assertNotEqual(testslide.matchers.IntGreater(21), 20)
        self.assertNotEqual(testslide.matchers.IntGreater(42), "derp")


    def test_IntGreaterOrEquals(self):
        self.assertEqual(testslide.matchers.IntGreaterOrEquals(21), 42)
        self.assertEqual(testslide.matchers.IntGreaterOrEquals(21), 21)
        self.assertNotEqual(testslide.matchers.IntGreaterOrEquals(21), 20)
        self.assertNotEqual(testslide.matchers.IntGreaterOrEquals(42), "derp")

    def test_IntLess(self):
        self.assertEqual(testslide.matchers.IntLess(21), 20)
        self.assertNotEqual(testslide.matchers.IntLess(21), 21)
        self.assertNotEqual(testslide.matchers.IntLess(21), 22)
        self.assertNotEqual(testslide.matchers.IntLess(42), "derp")

    def test_IntLessOrEquals(self):
        self.assertEqual(testslide.matchers.IntLessOrEquals(21), 20)
        self.assertEqual(testslide.matchers.IntLessOrEquals(21), 21)
        self.assertNotEqual(testslide.matchers.IntLessOrEquals(21), 22)
        self.assertNotEqual(testslide.matchers.IntLessOrEquals(42), "derp")


class FloatMatcherTest(testslide.TestCase):

    def testAnyFloat(self):
        self.assertEqual(testslide.matchers.AnyFloat(), 66.6)
        self.assertEqual(testslide.matchers.AnyFloat(), 4.2)
        self.assertNotEqual(testslide.matchers.AnyFloat(), "derp") 

    def test_ThisFloat(self):
        self.assertEqual(testslide.matchers.ThisFloat(66.6), 66.6)
        self.assertNotEqual(testslide.matchers.ThisFloat(6.9), 4.2)
        self.assertNotEqual(testslide.matchers.ThisFloat(4.2), "derp")
    
    def test_NotThisFloat(self):
        self.assertEqual(testslide.matchers.NotThisFloat(66.6), 4.2)
        self.assertNotEqual(testslide.matchers.NotThisFloat(6.9), 6.9)
        self.assertNotEqual(testslide.matchers.NotThisFloat(4.2), "derp")

    def test_FloatBetween(self):
        self.assertEqual(testslide.matchers.FloatBetween(2.1, 666), 4.2)
        self.assertEqual(testslide.matchers.FloatBetween(2.1, 666), 2.1)
        self.assertEqual(testslide.matchers.FloatBetween(21, 66.6), 66.6)
        self.assertNotEqual(testslide.matchers.FloatBetween(4.2, 6.9), 66.6)
        self.assertNotEqual(testslide.matchers.FloatBetween(4.2, 6.9), "derp")

    def test_FloatGreater(self):
        self.assertEqual(testslide.matchers.FloatGreater(2.1), 4.2)
        self.assertNotEqual(testslide.matchers.FloatGreater(2.1), 2.1)
        self.assertNotEqual(testslide.matchers.FloatGreater(2.1), 2.0)
        self.assertNotEqual(testslide.matchers.FloatGreater(4.2), "derp")


    def test_FloatGreaterOrEquals(self):
        self.assertEqual(testslide.matchers.FloatGreaterOrEquals(2.1), 4.2)
        self.assertEqual(testslide.matchers.FloatGreaterOrEquals(2.1), 2.1)
        self.assertNotEqual(testslide.matchers.FloatGreaterOrEquals(2.1), 2.0)
        self.assertNotEqual(testslide.matchers.FloatGreaterOrEquals(4.2), "derp")

    def test_FloatLess(self):
        self.assertEqual(testslide.matchers.FloatLess(2.1), 2.0)
        self.assertNotEqual(testslide.matchers.FloatLess(2.1), 2.1)
        self.assertNotEqual(testslide.matchers.FloatLess(2.1), 2.2)
        self.assertNotEqual(testslide.matchers.FloatLess(4.2), "derp")

    def test_FloatLessOrEquals(self):
        self.assertEqual(testslide.matchers.FloatLessOrEquals(2.1), 2.0)
        self.assertEqual(testslide.matchers.FloatLessOrEquals(2.1), 2.1)
        self.assertNotEqual(testslide.matchers.FloatLessOrEquals(2.1), 2.2)
        self.assertNotEqual(testslide.matchers.FloatLessOrEquals(4.2), "derp")

class SimpleTestCase(testslide.TestCase):
    def testEmpty(self):
        self.assertEqual(testslide.matchers.Empty(), {})
        self.assertEqual(testslide.matchers.Empty(), [])
        self.assertEqual(testslide.matchers.Empty(), ())
        self.assertEqual(testslide.matchers.Empty(), "")
        self.assertEqual(testslide.matchers.Empty(), None)
        self.assertEqual(testslide.matchers.Empty(), 0)
        self.assertNotEqual(testslide.matchers.Empty(), {"a":"b"})
        self.assertNotEqual(testslide.matchers.Empty(), ["a", "b"])
        self.assertNotEqual(testslide.matchers.Empty(), ("a", "b"))
        self.assertNotEqual(testslide.matchers.Empty(), "a")
        self.assertNotEqual(testslide.matchers.Empty(), 1)


    def testNotEmpty(self):
        self.assertNotEqual(testslide.matchers.NotEmpty(), {})
        self.assertNotEqual(testslide.matchers.NotEmpty(), [])
        self.assertNotEqual(testslide.matchers.NotEmpty(), ())
        self.assertNotEqual(testslide.matchers.NotEmpty(), "")
        self.assertNotEqual(testslide.matchers.NotEmpty(), None)
        self.assertNotEqual(testslide.matchers.NotEmpty(), 0)
        self.assertEqual(testslide.matchers.NotEmpty(), {"a":"b"})
        self.assertEqual(testslide.matchers.NotEmpty(), ["a", "b"])
        self.assertEqual(testslide.matchers.NotEmpty(), ("a", "b"))
        self.assertEqual(testslide.matchers.NotEmpty(), "a")
        self.assertEqual(testslide.matchers.NotEmpty(), 1)

    def testNothing(self):
        self.assertNotEqual(testslide.matchers.Nothing(), {})
        self.assertNotEqual(testslide.matchers.Nothing(), [])
        self.assertNotEqual(testslide.matchers.Nothing(), ())
        self.assertNotEqual(testslide.matchers.Nothing(), "")
        self.assertEqual(testslide.matchers.Nothing(), None)
        self.assertNotEqual(testslide.matchers.Nothing(), 0)
        self.assertNotEqual(testslide.matchers.Nothing(), {"a":"b"})
        self.assertNotEqual(testslide.matchers.Nothing(), ["a", "b"])
        self.assertNotEqual(testslide.matchers.Nothing(), ("a", "b"))
        self.assertNotEqual(testslide.matchers.Nothing(), "a")
        self.assertNotEqual(testslide.matchers.Nothing(), 1)

    def testSomething(self):
        self.assertEqual(testslide.matchers.Something(), {})
        self.assertEqual(testslide.matchers.Something(), [])
        self.assertEqual(testslide.matchers.Something(), ())
        self.assertEqual(testslide.matchers.Something(), "")
        self.assertNotEqual(testslide.matchers.Something(), None)
        self.assertEqual(testslide.matchers.Something(), 0)
        self.assertEqual(testslide.matchers.Something(), {"a":"b"})
        self.assertEqual(testslide.matchers.Something(), ["a", "b"])
        self.assertEqual(testslide.matchers.Something(), ("a", "b"))
        self.assertEqual(testslide.matchers.Something(), "a")
        self.assertEqual(testslide.matchers.Something(), 1)

    def testA(self):
        self.assertEqual(testslide.matchers.A(str), "durrdurr")
        self.assertNotEqual(testslide.matchers.A(str), 7)


class StringTest(testslide.TestCase):
    def testAnyString(self):
        self.assertEqual(testslide.matchers.AnyString(), "aa")
        self.assertEqual(testslide.matchers.AnyString(), "")
        self.assertNotEqual(testslide.matchers.AnyString(), 69)
        self.assertNotEqual(testslide.matchers.AnyString(), None)

    def testRegexMatches(self):
        self.assertEqual(testslide.matchers.RegexMatches("b[aeiou]t"), "bott")
        self.assertNotEqual(testslide.matchers.RegexMatches("b[aeiou]t"), "boot")
        self.assertNotEqual(testslide.matchers.RegexMatches("b[aeiou]t"), 13)

class TestSubsets(testslide.TestCase):
    def testListContaining(self):
        self.assertEqual(testslide.matchers.ListContaining([1,2]), [1,2,3])
        self.assertNotEqual(testslide.matchers.ListContaining([1,2]), [2,3,4])
        self.assertNotEqual(testslide.matchers.ListContaining([1,2]), "DERP")

    def testDictContaining(self):
        self.assertEqual(testslide.matchers.DictContaining({"a":"b", "c":1}), {"a":"b",  "c":1, "d":"e"})
        self.assertNotEqual(testslide.matchers.DictContaining({"a":"b", "c":1}), {"c":1, "d":"e"})
        self.assertNotEqual(testslide.matchers.DictContaining([1,2]), "DERP")

class TestChaining(testslide.TestCase):
    def testBitwiseAnd(self):
        self.assertTrue(isinstance(testslide.matchers.Something()&testslide.matchers.AnyString(), testslide.matchers._AndMatcher))
        self.assertEqual(testslide.matchers.Something()&testslide.matchers.AnyString(), "a" )
        self.assertNotEqual(testslide.matchers.Something()&testslide.matchers.AnyString(), 3 )


    def testBitwiseOr(self):
        self.assertTrue(isinstance(testslide.matchers.Something()|testslide.matchers.AnyString(), testslide.matchers._OrMatcher))
        self.assertEqual(testslide.matchers.AnyInt()|testslide.matchers.AnyString(), "a" )
        self.assertEqual(testslide.matchers.AnyInt()|testslide.matchers.AnyString(), 3 )
        self.assertNotEqual(testslide.matchers.AnyInt()|testslide.matchers.AnyString(), [] )


    def testBitwiseXor(self):
        self.assertTrue(isinstance(testslide.matchers.Something()^testslide.matchers.AnyString(), testslide.matchers._XorMatcher))
        self.assertEqual(testslide.matchers.AnyInt()^testslide.matchers.AnyString(), [] )
        self.assertNotEqual(testslide.matchers.AnyInt()^testslide.matchers.AnyString(), 3 )

    def testCannotChainMoreThanTwo(self):
            with self.assertRaises(testslide.matchers.AlreadyChainedException):
                testslide.matchers.Something()|testslide.matchers.AnyString()|testslide.matchers.AnyInt()
            with self.assertRaises(testslide.matchers.AlreadyChainedException):
                testslide.matchers.Something()&testslide.matchers.AnyString()&testslide.matchers.AnyInt()
            with self.assertRaises(testslide.matchers.AlreadyChainedException):
                testslide.matchers.Something()^testslide.matchers.AnyString()^testslide.matchers.AnyInt()
