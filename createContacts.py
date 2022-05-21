import requests as r
import pandas as p
import re
import json
from json import dumps
import subprocess
from datetime import date, datetime


# def json_serial(obj):
#     """JSON serializer for objects not serializable by default json code"""

#     if isinstance(obj, (datetime, date)):
#         return obj.isoformat()
#     raise TypeError ("Type %s not serializable" % type(obj))

# filename = "Contactpersons.xlsx"
# collName = 'customerId'
# xlsx = p.read_excel(filename)
# arr = xlsx[collName].tolist()
#print(arr)
#for i in range(len(arr)):
url = ("https://api.tst.carlsbergwebservices.com/cadi/api/contacts")
data = {
    "outletId": "6000335",
    "name": "Samuel",
    "email": "01131@coop.dk",
    "favorite": False,
    "jobTitle": {
        "name": "Butiksassistent",
        "salesOrgCode": "A001",
        "isOnTrade": False,
        "createdDate": "2021-12-02T11:13:42",
        "modifiedDate": "2021-12-02T11:13:42",
        "createdBy": "ADMIN",
        "modifiedBy": "ADMIN",
        "createdByApp": "cx-contact-services",
        "modifiedByApp": "cx-contact-services",
        "id": "80dc6007-683f-4b7a-ac6e-8db3365d3c55"
    },
    "phone": "36148210",
    "creationDate": "2022-05-19T13:41:26.322Z",
    "modificationDate": "2022-05-19T13:41:26.322Z"
}
    #"creationDate": dumps(datetime.now(), default=json_serial),
    #"modificationDate": dumps(datetime.now(), default=json_serial)
auth_token='eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJBUUdJcE16a19tREhsNmpndEQ4TjNldnVsZndldUJRTUdnQkRtVUNNLWc0In0.eyJqdGkiOiJiNWEzZWQzMy0wN2VjLTQ3YjYtYWJjMC03NzlhMDFkYzY0OGIiLCJleHAiOjE2NTMwOTg2ODQsIm5iZiI6MCwiaWF0IjoxNjUzMDk1MDg0LCJpc3MiOiJodHRwczovL2NhZGkudHN0LmN4LWFwcHMuaW8vYXV0aC9yZWFsbXMvY3giLCJhdWQiOlsiYnJva2VyIiwiYWNjb3VudCJdLCJzdWIiOiI4YzRjZDA1Mi02YjBlLTQ0YmYtODg2MS01ZmUyYzViYjBiZDEiLCJ0eXAiOiJCZWFyZXIiLCJhenAiOiJjeC1hcHBzIiwibm9uY2UiOiJhNzMyMjc0NS01NTVlLTQ2NjQtYWY3ZS1lNjQ0NzkzYTk1ZGEiLCJhdXRoX3RpbWUiOjE2NTMwMTE3MjQsInNlc3Npb25fc3RhdGUiOiJiNGM1ZmI0NS1hOGU1LTQ1ODItODFjMi1hMWI1ZTY0OTEyNDQiLCJhY3IiOiIwIiwicmVhbG1fYWNjZXNzIjp7InJvbGVzIjpbIm9mZmxpbmVfYWNjZXNzIiwidW1hX2F1dGhvcml6YXRpb24iXX0sInJlc291cmNlX2FjY2VzcyI6eyJicm9rZXIiOnsicm9sZXMiOlsicmVhZC10b2tlbiJdfSwiYWNjb3VudCI6eyJyb2xlcyI6WyJtYW5hZ2UtYWNjb3VudCIsIm1hbmFnZS1hY2NvdW50LWxpbmtzIiwidmlldy1wcm9maWxlIl19fSwic2NvcGUiOiJvcGVuaWQiLCJjeCI6eyJ0ZXAiOltdLCJ1c2VyRGF0YSI6eyJ0eXBlIjoiSU5URVJOQUwiLCJkZXRhaWxzIjp7ImVpZCI6ImJjZjAyNTRjLTAxMzEtNGZjOC04NTYzLTc0MTk0NWU3YWE0MyIsImZpcnN0TmFtZSI6IlNhbXVlbCIsImxhc3ROYW1lIjoiQmV1cmFuIiwiZW1haWxzIjpbeyJkZWZhdWx0RW1haWwiOnRydWUsImFkZHJlc3MiOiJzYW11ZWwuYmV1cmFuQGNhcmxzYmVyZ2dyb3VwLmNvbSIsImlzRGVmYXVsdEVtYWlsIjp0cnVlfV0sInBob25lcyI6W10sInJvbGVzIjp7InVzZXJSb2xlcyI6W3sicm9sZSI6eyJhcHBsaWNhdGlvbkNvZGUiOiJBTEwiLCJyb2xlTmFtZSI6IkFETUlOIn19XSwidXNlclNhbGVzT3JnUm9sZXMiOlt7InJvbGUiOnsiYXBwbGljYXRpb25Db2RlIjoiQ0FESSIsInJvbGVOYW1lIjoiQURNSU4ifSwic2FsZXNPcmdDb2RlIjoiRDAwMSJ9LHsicm9sZSI6eyJhcHBsaWNhdGlvbkNvZGUiOiJDQURJIiwicm9sZU5hbWUiOiJBUFBfT1JERVJfVVNFUiJ9LCJzYWxlc09yZ0NvZGUiOiJBMDAxIn0seyJyb2xlIjp7ImFwcGxpY2F0aW9uQ29kZSI6IkNBREkiLCJyb2xlTmFtZSI6IkFQUF9PRlRfU1VQX1VTRVIifSwic2FsZXNPcmdDb2RlIjoiQTAwMSJ9LHsicm9sZSI6eyJhcHBsaWNhdGlvbkNvZGUiOiJDQURJIiwicm9sZU5hbWUiOiJCT19PRlRfVVNFUiJ9LCJzYWxlc09yZ0NvZGUiOiJBMDAxIn1dLCJ1c2VyU2FsZXNPcmdDdXN0b21lclJvbGVzIjpbXX19LCJleHRyYURldGFpbHMiOnsiYXp1cmVVc2VyRGV0YWlscyI6eyJjb3VudHJ5IjoiUG9ydHVnYWwiLCJ1c2FnZUxvY2F0aW9uIjoiUFQiLCJjeEdyb3VwcyI6WyJDWF9DQURJX0FDQ0VTUyIsIkNYX0NBRElfQUNDRVNTX0RFViIsIkNYX0NBRElfQUNDRVNTX1NURyIsIkNYX0NBRElfQUNDRVNTX1RFU1QiLCJDWF9DQURJX09SREVSX1NURyIsIkNYX0NBRElfT1JERVJfREVWIiwiQ1hfQ0FESV9PUkRFUiJdfX19fX0.IsnEOHYBlDa6AwVAPmVOTxofzS3CeZnyvC51k2Axm2qmrcBw61BcN8kF1BvyeCzlrJ90JV_rjbk5qSLqTcW0S3EcMnAEiFX5khP5NYiJHwWJoMplmez_eRpZQpC20RlDGaYWnoClJRinCwVF-_li9rxvX-_cj1kYTr3LVSD2BrVPOSJ-KhYMbYYfEBFfnAvI6hTsnBTqVCdwoNQqIkgrLwW_lCcNniEM5n4l9gCRL757wIdjMk0cenIwyipt-t9bVoou6tF78HnQMPPy-VUoRwVsT5wTx0KeS2YJdfpQhfjfIkZWmjJJC6ztViTq-hNVIsS3xycNHKxtnaoQAAlTcw'
hed = {'Authorization': 'Bearer ' + auth_token}
createContact = r.post(url, json=data, headers=hed)
print(createContact.status_code)
print(createContact.reason)
print(createContact.json)

     