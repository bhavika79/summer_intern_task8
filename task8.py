#!/usr/bin/python3

import cgi
import subprocess

print("content-type: text/html")
print()

fs = cgi.FieldStorage()
plate_no = fs.getvalue("x")
if plate_no == "AP15BL3334":
	print("<body style='padding: 40px;'>")
	print('<h1 style="color:#df405a;" >Output</h1>')
	print('''<pre>
    Registration Name :Thakkalapally Bapurao 
    License No : 100012134567
    Make / Model : MAGNA HYUNDAI / I10
    Registration Date : 7/5/2013
    Registering Authority : hyderabad , INDIA
    Vehicle Class : MCWG
    Fuel Type : petrol,CNG
    Engine No : IVK3N1684632
    Chassis No : HMSURVWHFGVWE
    Insurance Upto : 5/13/2031
    Fitness Upto : 4/8/2025
    </pre>''')
	print("</body>")
else:
    print("<body style='padding: 40px;'>")
    print('<h1 style="color:#df405a;" >Output</h1>')
    print("No data available for this number...")
    print("</body>")


