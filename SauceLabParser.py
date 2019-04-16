import json
from jsonpath_rw import jsonpath, parse
import objectpath
import glob


file = open('../emailable_report.txt','w+')

for filename in glob.iglob("../YoutubeExport/test1.json"):
        with open(filename) as f:
            data = json.load(f)
        tree = objectpath.Tree(data)
        list1 = list(tree.execute('$.message'))
        for target_list in list1:
            #print(target_list)
            if '[PLAYER][' in target_list or 'starting testcase[' in target_list or '[RESULT][' in target_list:
                print(target_list)
        file.write(str(target_list) +"\n")
file.close()