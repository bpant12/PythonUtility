import json
from jsonpath_rw import jsonpath, parse
import objectpath
import glob


file = open('../MogrtList.csv','w+')
file.write('Author,Mogrt Name,Layer Count,Animated Layer Count,Animation Tag\n')
for filename in glob.iglob("../Mogrt/**/definition.json"):
        with open(filename) as f:
            data = json.load(f)
        tree = objectpath.Tree(data)
        list1 = list(tree.execute('$.clientControls..canAnimate'))
        count=0
        for target_list in list1:
            if str(target_list)=='True':
                count=count+1
        file.write(tree.execute('$.authorApp')+","+tree.execute('$.capsuleName')+","+ str(len(tree.execute('$.clientControls')))   +","+ str(count) +",\""+ str(tree.execute('$.capsuleTags'))  +"\"\n")
file.close()