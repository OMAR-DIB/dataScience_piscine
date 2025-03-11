import time
import datetime

timestamp = time.time()

# date = datetime.date(2024,1,2).ctime()
print(f"Seconds since January 1, 1970: {timestamp:,.4f} or {timestamp:.2e} in scientific notation")
print(timestamp)
# print(date)

formatted_date = datetime.datetime.today().strftime("%b %d %Y")
print(formatted_date )