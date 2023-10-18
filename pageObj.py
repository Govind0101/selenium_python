"""
# For each web page in the application there should be corresponding page class.
# This Page class will find the WebElements of that web page and also contains Page methods which perform operations on those WebElements.
# Name of these methods should be given as per the task they are performing i.e., if a loader is waiting for payment gateway to be appear, POM method name can be waitForPaymentScreenDisplay().
"""

"""
# Home page - http://www.makemytrip.com
# Search Results Page - 
# Modal Dialog - "Need to click 'Search Flights' button on that"
# Modal Dialog - "Need to click 'Continue to Book' button on that"
"""

class BasePage(object):
	url = "http://www.makemytrip.com"

	def __init__(self, driver):
		self.driver = driver

	def selRadioButtonByID(self, id):
		self.id = id
		self.driver.find_element_by_id(id)

class SearchResultsPage(object):
	url = None

	def __init__(self, driver):
		self.driver = driver

	def clickBookButton(self, driver):
		self.driver.find_element_by_id(id)
