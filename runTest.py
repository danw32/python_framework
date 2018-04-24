from read_sheet import *
import selenium_test_module
import driver_global

class runUnitTest_class(driver_global.SeleniumTest):

    """loop through the list"""
    for i in range(len(data)):
        if data[i]['Run'].lower() == 'y':
            """make the dictionary values more readable by putting them in variables"""
            url_value = data[i]['URL']
            password_value = data[i]['password']
            username_value = data[i]['username']
            print url_value
            print password_value
            print username_value

            """***Selenium tests below...***"""

            """Instantiate the selenium test class"""
            test_selenium_object = selenium_test_module.selenium_class()

            """Basic selenium test that goes to URLs that are in spreadsheet"""
            test_selenium_object.setUp()
            test_selenium_object.go_to_url(url_value)
            test_selenium_object.teardown()

        elif data[i]['Run'].lower() == 'n':
            print "Don't run row " + str(i + 1)
        elif data[i]['Run'].lower() != 'n' or data[i]['Run'].lower() != 'y':
            print "enter something useful in Run column: Y or N"
        else:
            pass