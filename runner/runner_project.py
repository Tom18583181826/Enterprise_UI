import time

import pytest

from common.read_ini import ReadIni


# 运行项目
class RunnerProject:
    def runner(self):
        now_time = time.strftime("%Y_%m_%d_%H_%M")
        report_path = ReadIni().get_report_file_path()

        pytest.main([r"E:\Code\pbf_enterprise_ui\case\interest_group\create_interest_group_test.py",
                     r"--html=E:\Code\pbf_enterprise_ui\result\report\report{}.html".format(
                         now_time),
                     "--self-contained-html"])

        # sendmail = SendMail()
        # sendmail.send_mail(report_path + "report{}.html".format(now_time))


if __name__ == '__main__':
    runner = RunnerProject()
    runner.runner()
