# Name: Talha Ahmad | Roll No: TRN-2026-000347 | Date: 11-11-2026
# Part 8 Challenge - small project using a package and the requests library
import requests
from school import grades, attendance

print("requests version:", requests.__version__)
print("Grade for 85 marks:", grades.get_grade(85))
print("Attendance:", attendance.attendance_percent(18, 20), "%")
