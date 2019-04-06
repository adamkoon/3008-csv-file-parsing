# spreadsheet
# 33 users
import csv
# make a readable file without Mozilla stuff
# with open('text21.csv', 'r', newline='') as inp, open('imagept21.csv', 'r', newline='') as inp2,\
#         open('read.csv', 'w', newline='') as out:
#     writer = csv.writer(out)
#     for row in csv.reader(inp):
#         if "Mozilla" not in row[7]:
#             writer.writerow(row)
#     for row2 in csv.reader(inp2):
#         if "Mozilla" not in row2[7]:
#             writer.writerow(row2)


# makes the time for the successful login time and failed login time
def time_converter(time_one, time_two):
    stime = int(time_one[0:1])*3600 + int(time_one[3:4]) * 60 + int(time_one[6:7])
    etime = int(time_two[0:1])*3600 + int(time_two[3:4]) * 60 + int(time_two[6:7])
    return stime - etime


r = csv.reader(open('3008data.csv', newline=''))
lines = list(r)
for i in lines:
    i[0] = i[0][11:len(i[0])]

newList = [['userid', 'password scheme', 'number of total logins', 'number of successful', "number of failed",
            "time for successful", "time for failed"]]
user = 'ast103'
success = 0
fails = 0
startTime = '0'
endTime = '0'
scheme = 'text21'
for i in lines:
    if i[1] == user:
        if i[6] == "success":
            success += 1
        elif i[6] == "failure":
            fails += 1
    else:
        newList.append([user])
        newList[len(newList) - 1].append(scheme)
        newList[len(newList) - 1].append(str(success+fails))
        newList[len(newList) - 1].append(str(success))
        newList[len(newList) - 1].append(str(fails))
        user = i[1]
        if i[3] == 'testpasstiles':
            scheme = 'imagept21'
        success = 0
        fails = 0

# append last user to the list
newList.append([user])
newList[len(newList) - 1].append(scheme)
newList[len(newList) - 1].append(str(success+fails))
newList[len(newList) - 1].append(str(success))
newList[len(newList) - 1].append(str(fails))
print(lines[0][0])
writer = csv.writer(open('modifieddata.csv', 'w', newline=''))
writer.writerows(newList)
