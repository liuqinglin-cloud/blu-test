import os.path
from airtest.report.report import LogToHtml

case_path = os.path.dirname(__file__)
project_path = os.path.dirname(os.path.dirname(__file__))
common_ios_path = os.path.join(project_path,"common_ios")
script_path = os.path.join(case_path,"run.py")
log_path = os.path.join(common_ios_path,"log")
logfile_path = os.path.join(common_ios_path,"log\\log.txt")
export_path = os.path.join(project_path,"report\\airtest_report\\translation_ios")
h1 = LogToHtml(script_root=script_path,
               log_root=log_path,
               export_dir=export_path,
               logfile=logfile_path,
               lang='zh',
               plugins=["poco.utils.airtest.report"])
h1.report()