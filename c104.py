from collections import Counter
import csv

with open("SOCR-HeightWeight.csv") as wh:
    fileread = csv.reader(wh)
    filedata = list(fileread)
  
filedata.pop(0)
newData = []
totalData = len(filedata)

for i in range(totalData):
  newno = filedata[i][1]
  newData.append(float(newno))

total = 0
for n in newData:
  total += n

mean = total / totalData
print("Mean height is =>"+ str(mean))

if totalData % 2 == 0:
  median1 = float(newData[totalData // 2 ])
  median2 = float(newData[totalData // 2 - 1 ])
  median = (median1 + median2) / 2
else:
  median = newData[totalData // 2]

print("The median is =>"+ str(median))

from collections import Counter

data = Counter(newData)
modeRange = {"50-60":0,"60-70":0,"70-80":0}

for height, occur in data.items():
  if 50 < float(height) < 60:
    modeRange["50-60"] += occur 

  if 60 < float(height) < 70: 
    modeRange["60-70"] += occur 

  if 70 < float(height) < 80:
    modeRange["70-80"] += occur

mode_range, mode_occurence = 0, 0

for range, occur in modeRange.items():
  if occur > mode_occurence:
    mode_range, mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occur

mode = float((mode_range[0] + mode_range[1]) / 2)
print(f"The mode is -> {mode:2f}")