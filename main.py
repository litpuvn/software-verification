import unittest
from suds.client import Client

class PhoneVerifyTestCase(unittest.TestCase):

    wsdl_url = 'http://ws.cdyne.com/phoneverify/phoneverify.asmx?wsdl'
    client = Client(url=wsdl_url)

    validPhoneNumber = "+18067867128"
    cleanValidPhoneNumber = "8067867128"

    invalidPhoneNumber = "this-is-invalid-number"
    validLicense = "my-key"
    invalidLicense = "in-valid-license-string"

    # ## Case X5 - the wsdl suddenly working without license, so the license parameter becomes redundant
    def testInvalidLicense(self):
        phone_return = self.client.service.CheckPhoneNumber(self.validPhoneNumber, self.invalidLicense)
        assert "Please Purchase a license key or email us for a test key." == phone_return["Company"]
        assert False == phone_return["Valid"]
        assert self.validPhoneNumber == phone_return["OriginalNumber"]
        assert self.cleanValidPhoneNumber == phone_return["CleanNumber"]
        assert False == phone_return["Wireless"]

    def testValidPhoneLength(self):
        print("Running test case with valid phone length = 10")

        phone_return = self.client.service.CheckPhoneNumber(self.validPhoneNumber, self.validLicense)

        assert "NEW CINGULAR WIRELESS PCS, LLC" == phone_return["Company"]
        assert True == phone_return["Valid"]
        assert "Assigned to a code holder for normal use." == phone_return["Use"]
        assert "TX"== phone_return["State"]
        assert "LUBBOCK" == phone_return["RC"]
        assert "6534" == phone_return["OCN"]
        assert self.validPhoneNumber == phone_return["OriginalNumber"]
        assert self.cleanValidPhoneNumber == phone_return["CleanNumber"]
        assert ""== phone_return["SwitchName"]
        assert ""== phone_return["SwitchType"]
        assert "United States" == phone_return["Country"]
        assert "LBCKTXFGG03"== phone_return["CLLI"]
        assert "WIRELESS"== phone_return["PrefixType"]
        assert "544"== phone_return["LATA"]
        assert "WIRELESS"== phone_return["sms"]
        assert "txt.att.net"== phone_return["Email"]
        assert "Unknown"== phone_return["AssignDate"]
        assert "Lubbock"== phone_return["TelecomCity"]
        assert "Lubbock"== phone_return["TelecomCounty"]
        assert "TX"== phone_return["TelecomState"]
        assert "79401"== phone_return["TelecomZip"]
        assert "CST"== phone_return["TimeZone"]
        assert "33.5024"== phone_return["Lat"]
        assert "-101.8777"== phone_return["Long"]
        assert True == phone_return["Wireless"]
        assert self.cleanValidPhoneNumber == phone_return["LRN"]

    def testInvalidPhoneNumberLength(self):

        phone_numbers = ["1180678671282", "80678671"]
        for pn in phone_numbers:
            phone_return = self.client.service.CheckPhoneNumber(pn, self.validLicense)
            assert False == phone_return["Valid"]
            assert pn == phone_return["OriginalNumber"]
            assert pn == phone_return["CleanNumber"]
            assert False == phone_return["Wireless"]

    def testInvalidPhoneNumber(self):

        phone_numbers = ["18067e67128", "+28067867128", "28067867128"]
        for pn in phone_numbers:
            phone_return = self.client.service.CheckPhoneNumber(pn, self.validLicense)
            assert False == phone_return["Valid"]
            cleanPn = pn
            if pn[0] == '+':
                cleanPn = pn[1:]
            assert pn == phone_return["OriginalNumber"]
            assert cleanPn == phone_return["CleanNumber"]
            assert False == phone_return["Wireless"]

    def testValidAreaCode(self):
        validAreaCodes = ["806"] #a long list of existing area codes

        for area in validAreaCodes:
            validPN = self.getPhoneNumberWithAreaCode(area)
            phone_return = self.client.service.CheckPhoneNumber(validPN, self.validLicense)
            assert "NEW CINGULAR WIRELESS PCS, LLC" == phone_return["Company"].upper()
            assert True == phone_return["Valid"]
            assert "Assigned to a code holder for normal use.".upper() == phone_return["Use"].upper()
            assert "TX" == phone_return["State"]
            assert "LUBBOCK" == phone_return["RC"]
            assert "6534" == phone_return["OCN"]
            assert validPN == phone_return["OriginalNumber"]
            assert validPN == phone_return["CleanNumber"]
            assert "" == phone_return["SwitchName"]
            assert "" == phone_return["SwitchType"]
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
            assert validPN == phone_return["LRN"]


    def testInvalidAreaCode(self):

        phone_return = self.client.service.CheckPhoneNumber("+18077867128", self.validLicense)
        assert False == phone_return["Valid"]
        assert "+18077867128" == phone_return["OriginalNumber"]
        assert "8077867128" == phone_return["CleanNumber"]
        assert False == phone_return["Wireless"]


    def getPhoneNumberWithAreaCode(self, area_code: str):

        return area_code + "7867128"

if __name__ == "__main__":

    unittest.main()  # run all tests