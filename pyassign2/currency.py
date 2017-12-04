#Module for currency exchange
#Hanyun Fan
#2017.12.2
"""Module for currency exchange
This module provides several string parsing functions to implement a 
simple currency exchange routine using an online currency service. 
The primary function in this module is exchange."""


import string
currency_from = input("")
currency_to = input("")
amount_from = input("")
def before_space(s):
    """Returns: Substring of s; up to, but not including, the first space 
    Parameter s: the string to slice
    Precondition: s has at least one space in it """
    
    
    if s != None:
        a = s.find(" ")
        if a == -1:
            return("NO SPACE")
        else:
            return float(s[:a])
    else:
        return("Error")
    
        
def get_to(s):
    """Returns: The TO value in the response to a currency query. 
    Parameter json: a json string to parse
    Precondition: json is the response to a currency query """
    
    
    a = s.find("to")
    b = s.find('"',a+8)
    if s[a+7] != '"':
        return s[a+7:b]
    

def currency_response(currency_from, currency_to, amount_from):
    """Returns: a JSON string that is a response to a currency query.
    
    A currency query converts amount_from money in currency currency_from 
    to the currency currency_to. The response should be a string of the form
    
        '{"from":"<old-amt>","to":"<new-amt>","success":true, "error":""}'
    
    where the values old-amount and new-amount contain the value and name 
    for the original and new currencies. If the query is invalid, both 
    old-amount and new-amount will be empty, while "success" will be followed 
    by the value false.
    
    Parameter currency_from: the currency on hand
    Precondition: currency_from is a string
    
    Parameter currency_to: the currency to convert to
    Precondition: currency_to is a string
    
    Parameter amount_from: amount of currency to convert
    Precondition: amount_from is a float"""
    
    
    URL = "http://cs1110.cs.cornell.edu/2016fa/a1server.php?from="
    URL = URL + currency_from + "&to=" + currency_to + "&amt=" + amount_from
    from urllib.request import urlopen
    doc = urlopen(URL)
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')
    return jstr


def exchange(currency_from, currency_to, amount_from):
    """Returns: amount of currency received in the given exchange.

    In this exchange, the user is changing amount_from money in 
    currency currency_from to the currency currency_to. The value 
    returned represents the amount in currency currency_to.

    The value returned has type float.

    Parameter currency_from: the currency on hand
    Precondition: currency_from is a string for a valid currency code
    
    Parameter currency_to: the currency to convert to
    Precondition: currency_to is a string for a valid currency code
    
    Parameter amount_from: amount of currency to convert
    Precondition: amount_from is a float"""
    
    
    a = get_to(currency_response(currency_from, currency_to, amount_from))
    result = before_space(a)
    return result
exchange(currency_from, currency_to, amount_from)


def test_before_space():
    """test if the before_space fuction can get the wanted answer"""
    
    
    assert(1 == before_space("1 2 3"))
    assert("NO SPACE" == before_space("1"))
    assert("Error" == before_space(None))
    
    
def test_get_to():
    """test if the get_to fuction can get the wanted answer"""
    
    
    assert(None == get_to('"to" : ""'))
    assert("1.825936" == get_to('to" : "1.825936"'))
def test_currency_response():
    """test if the currency_response fuction can get the wanted answer"""
    
    
    assert('{ "from" : "1 United States Dollar", "to" : "1 United States Dollar", "success" : true, "error" : "" }' == currency_response("USD", "USD", "1"))
    assert('{ "from" : "1 United States Dollar", "to" : "0.838095 Euros", "success" : true, "error" : "" }' == currency_response("USD", "EUR", "1"))
    assert('{ "from" : "", "to" : "", "success" : false, "error" : "Source currency code is invalid." }' == currency_response("A", "USD", "1"))

    
def test_exchange():
    """test if the exchange fuction can get the wanted answer"""
    
    
    assert(1 == exchange("USD", "USD", "1"))
    assert(0.838095 == exchange("USD", "EUR", "1"))
    assert("Error" == exchange("A", "EUR", "1"))
    
    
def testAll():
    """test all cases"""
    
    
    test_before_space()
    test_get_to()
    test_currency_response()
    test_exchange()
    print("All tests passed")
    

def main():
    testAll()
    exchange(currency_from, currency_to, amount_from)
    
    
if __name__ == "__main__":
    main()











    
