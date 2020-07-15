

import unittest
import currency

class TestCurrency(unittest.TestCase):

	def test_validation(self):
		self.assertEqual(currency.validation("123456.78"), True)
		self.assertEqual(currency.validation("123456"), True)
		self.assertEqual(currency.validation("0.78"), True)
		self.assertEqual(currency.validation("999999.99"), True)
		self.assertEqual(currency.validation("0"), True)

		self.assertEqual(currency.validation("1234567.78"), False)
		self.assertEqual(currency.validation("123456123"), False)
		self.assertEqual(currency.validation(".78"), False)
		self.assertEqual(currency.validation("-123456"), False)
		self.assertEqual(currency.validation("123.123"), False)

	def test_words(self):
		self.assertEqual(currency.words(9), "Nine")
		self.assertEqual(currency.words(19), "Nineteen")
		self.assertEqual(currency.words(31), "Thirty One")
		self.assertEqual(currency.words(50), "Fifty")
		self.assertEqual(currency.words(66), "Sixty Six")

	def test_currencyText(self):
		self.assertEqual(currency.currencyText("123456.78"), "Rs. One Lakh Twenty Three Thousand Four Hundred And Fifty Six 78/100 ONLY")
		self.assertEqual(currency.currencyText("999999.99"), "Rs. Nine Lakh Ninty Nine Thousand Nine Hundred And Ninty Nine 99/100 ONLY")
		self.assertEqual(currency.currencyText("0"), "Rs. Zero ONLY")
		self.assertEqual(currency.currencyText("28900"), "Rs. Twenty Eight Thousand Nine Hundred ONLY")

		self.assertRaises(Exception, currency.currencyText, "1234567")
		self.assertRaises(Exception, currency.currencyText, "1234567.")
		self.assertRaises(Exception, currency.currencyText, ".123")
		self.assertRaises(Exception, currency.currencyText, "")
