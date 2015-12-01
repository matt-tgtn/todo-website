from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp (self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown (self):
		self.browser.quit()
		
	def test_can_start_a_list_and_return_later(self):
		self.browser.get('http://localhost:8000')

		#Do the page title and header mention to-do lists
		self.assertIn('To-Do', self.browser.title)
		self.fail('Finish the test!')

		#Can you enter a to-do item straight away?

		#Someone wants to "Buy Peacock feathers"

		#When you hit enter the page updates and lists "1: Buy peacock feathers"

		#There should still be a text box to enter another task such as "Use peacock feathers to make a fly"

		#The page updates again with both items on the list

		#The page should generate a unique URL so teh list can be saved - with explanation

		#When re-visiting the URL it should still be there

		#Satisfied we can sleep



if __name__ == '__main__':
	unittest.main(warnings='ignore')
	