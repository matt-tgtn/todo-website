from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)

		#Can you enter a to-do item straight away?
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			inputbox.get_attribute('placeholder'), 
			'Enter a to-do item'
		)

		#Someone wants to "Buy Peacock feathers"
		inputbox.send_keys("Buy peacock feathers")

		#When you hit enter the page updates and lists "1: Buy peacock feathers"
		inputbox.send_keys(Keys.ENTER)
		
		table = self.browser.find_element_by_id('id_list_table')
		
		rows = table.find_elements_by_tag_name('tr')
		
		
		self.assertIn("1: Buy peacock feathers", [row.text for row in rows])
		
		#There should still be a text box to enter another task such as "Use peacock feathers to make a fly"
		inputbox = self.browser.find_element_by_id("id_new_item")
		inputbox.send_keys("Use peacock feathers to make a fly")
		inputbox.send_keys(Keys.ENTER)
		
		#The page updates again with both items on the list
		table = self.browser.find_element_by_tag_name("table")
		rows = table.find_elements_by_tag_name("tr")
		self.assertIn('1: Buy peacock feathers', [row.text for row in rows])
		self.assertIn('2: Use peacock feathers to make a fly', [row.text for row in rows])

		#The page should generate a unique URL so teh list can be saved - with explanation
		self.fail('Finish da test')
		
		#When re-visiting the URL it should still be there

		#Satisfied we can sleep



if __name__ == '__main__':
	unittest.main(warnings='ignore')
	