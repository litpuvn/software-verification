import unittest
from suds.client import Client

class PhonesVerifyTestCase(unittest.TestCase):

    wsdl_url = 'http://ws.cdyne.com/phoneverify/phoneverify.asmx?wsdl'
    client = Client(url=wsdl_url)

    validPhoneNumber = "+18067867128"
    cleanValidPhoneNumber = "8067867128"

    invalidPhoneNumber = "this-is-invalid-number"
    validLicense = "my-key"
    invalidLicense = "in-valid-license-string"

    # ## Case 16
    # def testInvalidLicense(self):
    #     phone_return = self.client.service.CheckPhoneNumber(self.validPhoneNumber, self.invalidLicense)
    #     assert "Please Purchase a license key or email us for a test key." == phone_return["Company"]
    #     assert False == phone_return["Valid"]
    #     assert self.validPhoneNumber == phone_return["OriginalNumber"]
    #     assert self.cleanValidPhoneNumber == phone_return["CleanNumber"]
    #     assert False == phone_return["Wireless"]

    ## CASE 13
    def testValidPhonesArray(self):

        validNumbers = ["8067867128"]

        phone_returns = self.client.service.CheckPhoneNumbers(validNumbers, self.validLicense)

        assert(1, len(phone_returns))

        phone_return = phone_returns[0]
        pn = validNumbers[0]

        assert "NEW CINGULAR WIRELESS PCS, LLC" == phone_return["Company"]
        assert True == phone_return["Valid"]
        assert "Assigned to a code holder for normal use." == phone_return["Use"]
        assert "TX" == phone_return["State"]
        assert "LUBBOCK" == phone_return["RC"]
        assert "6534" == phone_return["OCN"]
        assert pn == phone_return["OriginalNumber"]
        assert self.cleanValidPhoneNumber == phone_return["CleanNumber"]
        # assert ""== phone_return["SwitchName"]
        # assert ""== phone_return["SwitchType"]
        assert "United States" == phone_return["Country"]
        assert "LBCKTXFGG03" == phone_return["CLLI"]
        assert "WIRELESS" == phone_return["PrefixType"]
        assert "544" == phone_return["LATA"]
        assert "WIRELESS" == phone_return["sms"]
        assert "txt.att.net" == phone_return["Email"]
        assert "Unknown" == phone_return["AssignDate"]
        assert "Lubbock" == phone_return["TelecomCity"]
        assert "Lubbock" == phone_return["TelecomCounty"]
        assert "TX" == phone_return["TelecomState"]
        assert "79401" == phone_return["TelecomZip"]
        assert "CST" == phone_return["TimeZone"]
        assert "33.5024" == phone_return["Lat"]
        assert "-101.8777" == phone_return["Long"]
        assert True == phone_return["Wireless"]
        assert "8067867128" == phone_return["LRN"]

    # case 14
    def testEmptyPhonesArray(self):
        print("Running test case with valid phone length = 10")

        validNumbers = []

        phone_returns = self.client.service.CheckPhoneNumbers(validNumbers, self.validLicense)

        assert (1, len(phone_returns))



    # CASE 15
    def testPhoneArraysHasInvalidElements(self):

        phone_numbers = ["8067867128", "806e867128"]
        phone_returns = self.client.service.CheckPhoneNumbers(phone_numbers, self.validLicense)
        assert(2, len(phone_returns))

        #validate output for valid number
        pn = phone_numbers[0]
        phone_return = phone_returns[0]
        assert "NEW CINGULAR WIRELESS PCS, LLC" == phone_return["Company"]
        assert True == phone_return["Valid"]
        assert "Assigned to a code holder for normal use." == phone_return["Use"]
        assert "TX" == phone_return["State"]
        assert "LUBBOCK" == phone_return["RC"]
        assert "6534" == phone_return["OCN"]
        assert pn == phone_return["OriginalNumber"]
        assert self.cleanValidPhoneNumber == phone_return["CleanNumber"]
        # assert ""== phone_return["SwitchName"]
        # assert ""== phone_return["SwitchType"]
        assert "United States" == phone_return["Country"]
        assert "LBCKTXFGG03" == phone_return["CLLI"]
        assert "WIRELESS" == phone_return["PrefixType"]
        assert "544" == phone_return["LATA"]
        assert "WIRELESS" == phone_return["sms"]
        assert "txt.att.net" == phone_return["Email"]
        assert "Unknown" == phone_return["AssignDate"]
        assert "Lubbock" == phone_return["TelecomCity"]
        assert "Lubbock" == phone_return["TelecomCounty"]
        assert "TX" == phone_return["TelecomState"]
        assert "79401" == phone_return["TelecomZip"]
        assert "CST" == phone_return["TimeZone"]
        assert "33.5024" == phone_return["Lat"]
        assert "-101.8777" == phone_return["Long"]
        assert True == phone_return["Wireless"]
        assert "8067867128" == phone_return["LRN"]


        # validate output for invalid number
        pn = phone_numbers[1]
        phone_return = phone_returns[1]
        cleanPn = pn[0:3] + pn[4:]

        assert False == phone_return["Valid"]
        assert pn == phone_return["OriginalNumber"]
        assert cleanPn == phone_return["CleanNumber"]
        assert False == phone_return["Wireless"]


if __name__ == "__main__":

    unittest.main()  # run all tests