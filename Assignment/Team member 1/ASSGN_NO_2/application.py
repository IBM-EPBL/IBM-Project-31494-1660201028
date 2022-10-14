from flask import Flask, render_template, request, redirect, url_for, session
import ibm_db
import db2
import re

hostname = '19af6446-6171-4641-8aba-9dcff8e1b6ff.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud'
uid = 'pqw81844'
pwd = 'U9EkEP2DEWnscaL6'
driver = "{IBM DB2 ODBC DRIVER}"
db_name = 'Bludb'
port = '30699'
protocol = 'TCPIP'
cert = "C:/Users/Jeeva/Desktop/ASSGN_NO_2/certi.crt"
dsn = (
    "DATABASE ={0};"
    "HOSTNAME ={1};"
    "PORT ={2};"
    "UID ={3};"
    "SECURITY=SSL;"
    "PROTOCOL={4};"
    "SSlServerCertificate={5};"
    "PWD ={6};"
).format(db_name, hostname, port, uid, protocol, cert, pwd)
print(dsn)
try:

    print("Connecting to db2.....")
    db2 = ibm_db.connect(dsn, "", "")
    print()
    print("Connected to database")
    print("Connection Successful!!!")

except Exception as exception:
    print("unable to connect ", exception)
