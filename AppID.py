import json
from jsonpath_rw import jsonpath, parse
import objectpath
import glob

file = open('../app_id.txt', 'w+')

for filename in glob.iglob("../latest_executed_report.json"):
    with open(filename) as f:
        data = json.load(f)
    tree = objectpath.Tree(data)
    counter = 0
    flag = True
    reportList = []
    while flag:
        target_list = tree.execute(
            "$.entities[@.usage is 'ANDROID_INSTRUMENTATION'].testReportIds[" + str(counter) + "]")
        if target_list is not None:
            reportList.append(target_list)
            # print(target_list)
            counter = counter + 1
        else:
            break
    reportList.sort(reverse=True)
    print(reportList[0][0])
    file.write(str(reportList[0][0]))
file.close()

# file = open('../app_id.txt','w+')

# with open('../latest_executed_report.txt') as fp:
#    line = fp.readline()
#    cnt = 1
#    while line:
#        if 'TestReportId:' in line:
#            data = line.split("TestReportId:")[1].split(' ')
#            print(data[1].strip())
#            file.write(str(data[1].strip()))
#            break
#        line = fp.readline()
#        cnt += 1
# file.close()