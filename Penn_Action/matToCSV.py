import os
import csv
import scipy.io

joints =  ["head","left_shoulder","right_shoulder","left_elbow","right_elbow","left_wrist","right_wrist","left_hip","right_hip","left_knee","right_knee","left_ankle","right_ankle"]
fieldnames = joints + ["action"]
csvPath = "InputTable" + '.csv'

rows = []
for filename in os.listdir('labels'):
    mat = scipy.io.loadmat('labels/' + filename)

    
    temp = {}
    for i in range(len(joints)):
        temp[joints[i]] = [str(mat["x"][0][i]),str(mat["y"][0][i]),str(mat["visibility"][0][i])]
    temp["action"] = str(mat["action"][0])
    rows += [temp]
print(rows)
with open(csvPath, 'w') as f1:
       writer = csv.DictWriter(f1,fieldnames=fieldnames)
       writer.writeheader()
       for entry in rows:
           writer.writerow(entry)