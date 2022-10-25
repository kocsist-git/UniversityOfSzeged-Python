import calendar
import datetime as dt

most = dt.datetime.now()
c = calendar.LocaleTextCalendar(locale="hu")
print("Aktualis naptari honap:")
print(c.formatmonth(most.year, most.month))
 