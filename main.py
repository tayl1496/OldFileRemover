import os, time
import datetime

downloadsPath = "\\Users\\Stsam\\Desktop"

numDays = int(
    input("Enter the number of days ago that anything previous will be deleted: ")
)
twoWeeksAgo = datetime.datetime.now() - datetime.timedelta(days=numDays)

onlyfiles = os.listdir(downloadsPath)

for file in onlyfiles:
    if (
        datetime.datetime.strptime(
            time.ctime(os.path.getmtime(downloadsPath + "\\" + file)),
            "%a %b %d %H:%M:%S %Y",
        )
        < twoWeeksAgo
    ):
        os.remove(downloadsPath + "\\" + file)

