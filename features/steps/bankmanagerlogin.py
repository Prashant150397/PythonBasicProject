import time

from behave import *
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

wait = 20

@given('i click on Bank Manager Login')
def step_impl(context):
    context.driver.implicitly_wait(wait)
    context.driver.find_element(By.XPATH,"//button[contains(.,'Bank Manager Login')]").click()
    context.driver.implicitly_wait(wait)
    #time.sleep(4)


@when('i click on Add customers tab')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//button[normalize-space()='Add Customer']").click()
    context.driver.implicitly_wait(wait)


@when('i enter first name "{firstname}"')
def step_impl(context, firstname):
    context.driver.find_element(By.XPATH, "//input[contains(@placeholder,'First Name')]").send_keys(firstname)


@when('i enter last name "{lastname}"')
def step_impl(context, lastname):
    context.driver.find_element(By.XPATH, "//input[contains(@placeholder,'Last Name')]").send_keys(lastname)


@when('i enter post code "{postcode}"')
def step_impl(context, postcode):
    context.driver.find_element(By.XPATH, "//input[@placeholder='Post Code']").send_keys(postcode)


@when('i click on add customer to add the customer')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//button[@type='submit'][contains(.,'Add Customer')]").click()
    context.driver.implicitly_wait(wait)


@then('i verify the customer added successfully')
def step_impl(context):
    alert = context.driver.switch_to.alert
    context.driver.implicitly_wait(wait)
    text = alert.text
    assert text == "Customer added successfully with customer id :6"
    print(alert.text)
    alert.accept()


@when('i click on Open Account')
def clickOnOpenAccount(context):
    context.driver.implicitly_wait(wait)
    context.driver.find_element(By.XPATH, "//button[contains(text(),'Open Account')]").click()
    context.driver.implicitly_wait(wait)


@when('i select Customers Name "{name}"')
def step_impl(context, name):
    context.driver.find_element(By.XPATH, "//select[contains(@name,'userSelect')]").click()
    context.driver.implicitly_wait(wait)
    context.driver.find_element(By.XPATH, "//option[contains(text(),'" + name + "')]").click()


@when('i select Currency "{currency}"')
def step_impl(context, currency):
    context.driver.find_element(By.XPATH, "//select[@id='currency']").click()
    context.driver.implicitly_wait(wait)
    context.driver.find_element(By.XPATH, "//option[contains(text(),'" + currency + "')]").click()


@when('i click on Process')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//button[@type='submit']").click()


@then('i verify account created successfully')
def step_impl(context):
    alert = context.driver.switch_to.alert
    time.sleep(2)
    print(alert.text)
    alert.accept()


@when('i click on Customers tab')
def clickOnCustomers(context):
    context.driver.find_element(By.XPATH, "//button[contains(text(),'Customers')]").click()
    context.driver.implicitly_wait(wait)


@when('i enter the name of customer "{firstName}"')
def enterCustomerName(context, firstName):
    context.driver.find_element(By.XPATH, "//input[@placeholder='Search Customer']").send_keys(firstName)
    context.driver.implicitly_wait(wait)


@then('i verify the customer name "{name}" successfully')
def verifyCustomerName(context, name):
    firstName = context.driver.find_element(By.XPATH, "//td[contains(text(),'" + name + "')]").text
    assert firstName == "Harry"


@given('i clear and enter the the name of customer "{name}"')
def clearAndEnterName(context, name):
    context.driver.find_element(By.XPATH, "//input[@placeholder='Search Customer']").clear()
    context.driver.find_element(By.XPATH, "//input[@placeholder='Search Customer']").send_keys(name)
    context.driver.implicitly_wait(wait)


@when('i click on delete customers')
def deleteCustomer(context):
    context.driver.find_element(By.XPATH, "//tr//td[contains(text(),'Tom')]/..//td//button").click()
    context.driver.implicitly_wait(wait)


@then('i verify the customer "{name}" deleted successfully')
def verifyCustomerDeletedSuccessfully(context, name):
    try:
        context.driver.find_element(By.XPATH, "//td[contains(text(),'" + name + "')]")
    except NoSuchElementException:
        print("Element is not present")


@given('I click on customer login')
def clickOnCustomerLogin(context):
    context.driver.implicitly_wait(wait)
    time.sleep(3)
    context.driver.find_element(By.XPATH, "//button[contains(text(),'Home')]").click()
    context.driver.find_element(By.XPATH, "//button[contains(.,'Customer Login')]").click()
    context.driver.implicitly_wait(wait)


@when('I select customer name "{name}"')
def selectCustomer(context, name):
    context.driver.find_element(By.XPATH, "//select[@id='userSelect']").click()
    context.driver.implicitly_wait(wait)
    context.driver.find_element(By.XPATH, "//option[contains(text(),'" + name + "')]").click()


@when('I click on Login button')
def clickOnLoginButton(context):
    context.driver.find_element(By.XPATH, "//button[contains(text(),'Login')]").click()
    context.driver.implicitly_wait(wait)


@then('I verify customer login successfully "{name}"')
def step_impl(context, name):
    text = context.driver.find_element(By.XPATH, "//span[contains(text(),'" + name + "')]").text
    assert text == "Harry Potter"


@given('I click on deposit tab')
def clickOnDepositTab(context):
    context.driver.find_element(By.XPATH, "//div/button[contains(text(),'Deposit')] ").click()
    context.driver.implicitly_wait(wait)


@when('I enter amount "{amount}"')
def enterAmountToDeposit(context, amount):
    context.driver.find_element(By.XPATH, "//input[@type='number'] ").send_keys(amount)
    context.driver.implicitly_wait(wait)


@when('I click on deposit button')
def clickOnWithdrawButton(context):
    context.driver.find_element(By.XPATH, "//button[text()='Deposit']").click()
    context.driver.implicitly_wait(wait)


@then('I verify amount Deposit successful message is displayed "{message}"')
def verifyTransactionSuccessful(context, message):
    text = context.driver.find_element(By.XPATH, "//span[contains(text(),'" + message + "')]").text
    assert text == "Deposit Successful"


@given('I click on withdrawl tab')
def clickOnWithdrwalTab(context):
    context.driver.find_element(By.XPATH, "//button[contains(normalize-space(),'Withdrawl')] ").click()
    context.driver.implicitly_wait(wait)
    time.sleep(3)



@when('I enter amount to withdraw "{amount}"')
def enterAmountToWithdraw(context, amount):
    context.driver.find_element(By.XPATH, "//input[@type='number'] ").send_keys(amount)
    context.driver.implicitly_wait(wait)


@when('I click on withdraw button')
def clickOnWithdrawButton(context):
    context.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    context.driver.implicitly_wait(wait)



@then('I verify transaction successful message is displayed "{message}"')
def verifyTransactionSuccessful(context, message):
    text = context.driver.find_element(By.XPATH, "//span[contains(text(),'" + message + "')]").text
    assert text == "Transaction successful"