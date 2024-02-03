import mysql.connector

dataBase=mysql.connector.connect(
    host='localhost',
    user='root',
    password='root'
)

cursorObject=dataBase.cursor()

#create database

cursorObject.execute("CREATE DATABASE Project_dcrm")

print("Done!")