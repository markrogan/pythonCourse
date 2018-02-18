import datetime
import re


stringDate = "January 10th, 2018"

stringDate = re.sub(r'(\d)(st|nd|rd|th)', r'\1', stringDate)
print stringDate

dateObj = datetime.datetime.strptime(stringDate, "%B %d, %Y")


print dateObj.date()


endDate = dateObj + datetime.timedelta(days=5)

print endDate.date()
