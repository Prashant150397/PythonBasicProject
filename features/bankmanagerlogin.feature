Feature: Bank Manager


  Scenario Outline: Add customer
    Given i click on Bank Manager Login
    When i click on Add customers tab
    And i enter first name "<firstname>"
    And i enter last name "<lastname>"
    And i enter post code "<postcode>"
    And i click on add customer to add the customer
    Then i verify the customer added successfully

    Examples:
      | firstname | lastname | postcode |
      | Tom       | Parker   | 23456    |


  Scenario Outline: Add second customer
    When i click on Open Account
    And i select Customers Name "<CustomerName>"
    And i select Currency "<currency>"
    And i click on Process
    Then i verify account created successfully

    Examples:
      | CustomerName | currency |
      | Harry Potter | Dollar   |

  Scenario Outline: Search Customer
    When i click on Customers tab
    And i enter the name of customer "<fname>"
    Then i verify the customer name "<fname>" successfully

    Examples:
      | fname |
      | Harry |

  Scenario Outline: Delete Customer
    Given i clear and enter the the name of customer "<name>"
    When i click on delete customers
    Then i verify the customer "<name>" deleted successfully

    Examples:
      | name |
      | Tom  |

    Scenario Outline: Customer Login successfully
    Given I click on customer login
    When I select customer name "<name>"
    And I click on Login button
    Then I verify customer login successfully "<name>"

    Examples:
      | name         |
      | Harry Potter |

  Scenario Outline: Deposit Amount
    Given I click on deposit tab
    When I enter amount "<amount>"
    And I click on deposit button
    Then I verify amount Deposit successful message is displayed "<message>"

    Examples:
      | amount | message            |
      | 30000  | Deposit Successful |

  Scenario Outline: Withdrawl Amount Successully
    Given I click on withdrawl tab
    When I enter amount to withdraw "<amount>"
    And I click on withdraw button
    Then I verify transaction successful message is displayed "<message>"

    Examples:
      | amount | message                |
      | 10000  | Transaction successful |

    Scenario Outline: Customer Login successfully
    Given I click on customer login
    When I select customer name "<name>"
    And I click on Login button
    Then I verify customer login successfully "<name>"

    Examples:
      | name         |
      | Harry Potter |

  Scenario Outline: Deposit Amount
    Given I click on deposit tab
    When I enter amount "<amount>"
    And I click on deposit button
    Then I verify amount Deposit successful message is displayed "<message>"

    Examples:
      | amount | message            |
      | 30000  | Deposit Successful |

  Scenario Outline: Withdrawl Amount Successully
    Given I click on withdrawl tab
    When I enter amount to withdraw "<amount>"
    And I click on withdraw button
    Then I verify transaction successful message is displayed "<message>"

    Examples:
      | amount | message                |
      | 10000  | Transaction successful |



