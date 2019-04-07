# spreadsheet parser for comp3008
import csv


# makes the time for the successful login time and failed login time
def time_converter(time_one, time_two):
    stime = int(time_one[0:2])*3600 + int(time_one[3:5]) * 60 + int(time_one[6:])
    etime = int(time_two[0:2])*3600 + int(time_two[3:5]) * 60 + int(time_two[6:])
    return etime - stime


# access the data from a combined csv file
r = csv.reader(open('3008data.csv', newline=''))
lines = list(r)
# make the timestamps easier to read
for i in lines:
    i[0] = i[0][11:len(i[0])]

newList = [['userid', 'password scheme', 'number of total logins', 'number of successful', "number of failed",
            "time for successful", "time for failed", 'average success time', 'average failed time']]
user = lines[0][1]
success = 0
fails = 0
strt = ''
startTime = 0
endTime = 0
dubcheck = ''
scheme = 'text21'

# go through the data and collect the valuable information
for i in lines:
    if i[1] == user:
        if i[6] == "start":
            strt = i[0]
        # edge case protector
        if i[6] == 'order inputPwd':
            dubcheck = i[0]
        # successful login and failed login counter
        if i[6] == "success":
            success += 1
            if time_converter(strt, i[0]) < 0:
                startTime += time_converter(dubcheck, i[0])
            else:
                startTime += time_converter(strt, i[0])
        elif i[6] == "failure":
            fails += 1
            endTime += time_converter(strt, i[0])
    else:
        # add the user's data to the list
        newList.append([user])
        newList[len(newList) - 1].append(scheme)
        newList[len(newList) - 1].append(str(success+fails))
        newList[len(newList) - 1].append(str(success))
        newList[len(newList) - 1].append(str(fails))
        newList[len(newList) - 1].append(str(startTime))
        newList[len(newList) - 1].append(str(endTime))
        newList[len(newList) - 1].append(str(round(startTime/success, 2)))
        if fails == 0:
            newList[len(newList) - 1].append('0')
        else:
            newList[len(newList) - 1].append(str(round(endTime/fails, 2)))
        user = i[1]
        # check what scheme the user is using
        if i[3] == 'testpasstiles':
            scheme = 'imagept21'
        success = 0
        fails = 0
        startTime = 0
        endTime = 0

# append last user to the list
newList.append([user])
newList[len(newList) - 1].append(scheme)
newList[len(newList) - 1].append(str(success+fails))
newList[len(newList) - 1].append(str(success))
newList[len(newList) - 1].append(str(fails))
newList[len(newList) - 1].append(str(startTime))
newList[len(newList) - 1].append(str(endTime))
newList[len(newList) - 1].append(str(round(startTime / success, 2)))
if fails == 0:
    newList[len(newList) - 1].append('0')
else:
    newList[len(newList) - 1].append(str(round(endTime / success, 2)))

# put table into the csv file
writer = csv.writer(open('modifieddata.csv', 'w', newline=''))
writer.writerows(newList)
