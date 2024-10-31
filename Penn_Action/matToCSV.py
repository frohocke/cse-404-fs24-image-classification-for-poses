import os
import csv
import scipy.io

joints =  ["head","left_shoulder","right_shoulder","left_elbow","right_elbow","left_wrist","right_wrist","left_hip","right_hip","left_knee","right_knee","left_ankle","right_ankle"]
fieldnames = joints + ["action"]
actions = {"baseball_pitch" : 0,  "clean_and_jerk": 1,  "pullup" : 2, "strum_guitar" : 3,
"baseball_swing" : 4, "golf_swing" : 5, "pushup" : 6,  "tennis_forehand" : 7,
"bench_press" : 8,  "jumping_jacks": 9,   "situp" : 10,   "tennis_serve" : 11,
"bowl" : 12,  "jump_rope" : 13, "squat" : 14}
csvTrainPath = "TrainTable" + '.csv'
csvTestPath = "TestTable" + '.csv'

rows = []
testRows = []
for filename in os.listdir('labels'):
    mat = scipy.io.loadmat('labels/' + filename)

    
    temp = {}
    test = mat["train"][0][0]
    for i in range(len(joints)):
        temp[joints[i]] = [str(mat["x"][0][i]),str(mat["y"][0][i]),str(mat["visibility"][0][i])]
    temp["action"] = actions[str(mat["action"][0])]
    if mat["train"][0][0] == -1:
         rows += [temp]
    else:
        testRows += [temp]
print(rows)
with open(csvTrainPath, 'w') as f1:
       writer = csv.DictWriter(f1,fieldnames=fieldnames)
       writer.writeheader()
       for entry in rows:
           writer.writerow(entry)

with open(csvTestPath, 'w') as f1:
       writer = csv.DictWriter(f1,fieldnames=fieldnames)
       writer.writeheader()
       for entry in rows:
           writer.writerow(entry)