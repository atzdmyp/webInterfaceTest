import os
import unittest
from common.Log import MyLog as Log
import readConfig as readConfig
from common import HTMLTestRunner
from common.configEmail import MyEmail

localReadConfig = readConfig.ReadConfig()


class AllTest:
    def __init__(self):
        global log, logger, resultPath, on_off
        log = Log.get_log()
        logger = log.get_logger()
        resultPath = log.get_report_path()
        on_off = localReadConfig.get_email("on_off")
        self.caseListFile = os.path.join(readConfig.proDir, "caselist.txt")
        self.caseFile = os.path.join(readConfig.proDir, "testCase")
        # self.caseFile = None
        self.caseList = []
        self.email = MyEmail.get_email()

        # 2016case
        self.caseListFile2016 = os.path.join(readConfig.proDir, "caselist2016.txt")
        self.caseFile2016 = os.path.join(readConfig.proDir, "testCase2016")
        self.caseList2016 = []

    def set_case_list(self):
        """
        set case list
        :return:
        """
        fb = open(self.caseListFile2016)
        for value in fb.readlines():
            data = str(value)
            if data != '' and not data.startswith("#"):
                self.caseList2016.append(data.replace("\n", ""))
        fb.close()

    def set_case_suite(self):
        """
        set case suite
        :return:
        """
        self.set_case_list()
        test_suite = unittest.TestSuite()
        suite_module = []

        for case in self.caseList2016:
            case_name = case.split("/")[-1]
            print(case_name+".py")
            discover = unittest.defaultTestLoader.discover(self.caseFile2016, pattern=case_name + '.py', top_level_dir=None)
            suite_module.append(discover)

        if len(suite_module) > 0:

            for suite in suite_module:
                for test_name in suite:
                    test_suite.addTest(test_name)
        else:
            return None

        return test_suite

    def run(self):
        """
        run test
        :return:
        """
        try:
            suit = self.set_case_suite()
            if suit is not None:
                logger.info("********TEST START 2016********")
                fp = open(resultPath, 'wb')
                runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='接口测试报告', description='Test Description')
                runner.run(suit)
            else:
                logger.info("Have no case to test.")
        except Exception as ex:
            logger.error(str(ex))
        finally:
            logger.info("*********TEST END*********")
            fp.close()
            # send test report by email
            if on_off == 'on':
                self.email.send_email()
            elif on_off == 'off':
                logger.info("Doesn't send report email to developer.")
            else:
                logger.info("Unknow state.")


if __name__ == '__main__':
    obj = AllTest()
    obj.run()
