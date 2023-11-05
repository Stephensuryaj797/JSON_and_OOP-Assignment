import json
employee_info=[{"Name":"anbu","DOB":"16/01/1997","Height":"5'10","City":"selam","State":"Tamil nadu"},
               {"Name":"Srinivas reddy","DOB":"24/04/1996","Height":"5'6","City":"Vijayawada","State":"Telengana"},
               {"Name":"Renuka","DOB":"08/08/1997","Height":"5'4","City":"puna","State":"Maharastra"},
               {"Name":"Abhijeet","DOB":"18/07/1999","Height":"5'3","City":"Varanasi","State":"Uttar Pradesh"},
               {"Name":"Suman","DOB":"28/03/2001","Height":"5'4","City":"Ahmedabad","State":"Gujarat"}]
with open("employee.json","w") as f:
    d=json.dump(employee_info,f)
with open("employee.json","r") as f:
    x=json.load(f)
    print(x)
