import unittest
import paramunittest
import readConfig as readConfig
from common import Log as Log
from common import common
from common import configHttp as ConfigHttp
from common import businessCommon

addAddress_xls = common.get_xls("userCase.xlsx", "addAddress")
localReadConfig = readConfig.ReadConfig()
configHttp = ConfigHttp.ConfigHttp()


@paramunittest.parametrized(*addAddress_xls)
class AddAddressOrder(unittest.TestCase):
    def setParameters(self, description, sex, fname, lname, father_name, english_name, tel, standby_tel, address1, address2, city, state, postcode, country_id, tax_number, company, fax, is_default, street, msg, code):
        """
        set params
        :param description:
        :param sex:
        :param fname:
        :param lname:
        :param father_name:
        :param english_name:
        :param tel:
        :param standby_tel:
        :param address1:
        :param address2:
        :param city:
        :param state:
        :param postcode:
        :param country_id:
        :param tax_number:
        :param company:
        :param fax:
        :param is_default:
        :param street:
        :param msg:
        :param code:
        :return:
        """
        self.description = str(description)
        self.sex = str(sex)
        self.fname = str(fname)
        self.lname = str(lname)
        self.father_name = str(father_name)
        self.english_name = str(english_name)
        self.tel = tel
        self.standby_tel = str(standby_tel)
        self.address1 = str(address1)
        self.address2 = str(address2)
        self.city = str(city)
        self.state = str(state)
        self.postcode = str(postcode)
        self.country_id = int(country_id)
        self.tax_number = str(tax_number)
        self.company = str(company)
        self.fax = str(fax)
        self.is_default = str(is_default)
        self.street = str(street)
        self.code = str(code)
        self.msg = str(msg)
        self.info = None

    def description(self):
        """

        :return:
        """
        self.description

    def setUp(self):
        """

        :return:
        """
        self.log = Log.MyLog.get_log()
        self.logger = self.log.get_logger()
        # self.login_token = businessCommon.login()

    def testAddAddress(self):
        """
        test body
        :return:
        """
        # set url
        self.url = "/index.php"
        configHttp.set_url(self.url)

        # get token
        self.token = "42002693993_5a2669785c0267.83174218_2a2367697a6fa222dd63927f72752c3e85060f63"

        # set headers
        header = {"token": str(self.token),
                  "SiteUID": "rwm"}
        configHttp.set_headers(header)

        # set params
        params = {
            "model": "order",
            "action": "address_book",
            "operate": "insert_address"
        }
        configHttp.set_params(params)

        # set data
        if self.country_id == 74 or self.country_id == 198:
            self.postcode = int(self.postcode)
        data = {"sex": self.sex,
                "fname": self.fname,
                "lname": self.lname,
                "father_name": self.father_name,
                "english_name": self.english_name,
                "tel": self.tel,
                "standby_tel": self.standby_tel,
                "address1": self.address1,
                "address2": self.address2,
                "city": self.city,
                "state": self.state,
                "postcode": self.postcode,
                "country_id": self.country_id,
                "tax_number": self.tax_number,
                "company": self.company,
                "fax": self.fax,
                "is_default": self.is_default,
                "street": self.street}
        configHttp.set_data(data)

        # test interface
        self.return_json = configHttp.post()

        # check result
        self.checkResult()

    def tearDown(self):
        """

        :return:
        """

        # logout
        # businessCommon.logout(self.token)
        self.log.build_case_line(self.description, self.info['code'], self.info['msg'])

    def checkResult(self):
        """
        check test result
        :return:
        """
        self.info = self.return_json.json()
        common.show_return_msg(self.return_json)

        if self.code == '0':
            self.assertEqual(self.info['code'], self.code)
            self.assertEqual(self.info['msg'], self.msg)
            self.assertEqual(self.sex, common.get_value_from_return_json(self.info, 'address', 'sex'))
            self.assertEqual(self.fname, common.get_value_from_return_json(self.info, 'address', 'fname'))
            if self.country_id == 38 or self.country_id == 137:
                self.assertEqual("", common.get_value_from_return_json(self.info, 'address', 'lname'))
            else:
                self.assertEqual(self.lname, common.get_value_from_return_json(self.info, 'address', 'lname'))
            if self.country_id == 178:
                self.assertEqual(self.father_name, common.get_value_from_return_json(self.info, 'address', 'fatherName'))
            else:
                self.assertEqual("", common.get_value_from_return_json(self.info, 'address', 'fatherName'))
            if self.country_id == 74 or self.country_id == 198:
                self.assertEqual(str(self.postcode), common.get_value_from_return_json(self.info, 'address', 'postcode'))
            else:
                self.assertEqual(self.postcode, common.get_value_from_return_json(self.info, 'address', 'postcode'))
            if self.country_id == 30:
                self.assertEqual(self.tax_number, common.get_value_from_return_json(self.info, 'address', 'taxNumber'))
            self.assertEqual(str(self.tel), common.get_value_from_return_json(self.info, 'address', 'tel'))
            self.assertEqual(self.address1, common.get_value_from_return_json(self.info, 'address', 'address1'))
            self.assertEqual(self.city, common.get_value_from_return_json(self.info, 'address', 'city'))
            self.assertEqual(self.state, common.get_value_from_return_json(self.info, 'address', 'state'))
            self.assertEqual(str(self.country_id), common.get_value_from_return_json(self.info, 'address', 'countryId'))

        else:
            self.assertEqual(self.info['code'], self.code)
            self.assertEqual(self.info['msg'], self.msg)
