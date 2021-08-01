from __future__ import print_function
from typing import Dict

import mysql.connector
from mysql.connector import errorcode
from datetime import date, datetime, timedelta
DB_NAME='tic7'

TABLES={}
TABLES['plays']=(
    "CREATE TABLE `plays`("
    " `Play_id` int NOT NULL AUTO_INCREMENT,"
    " `played_date` date NOT NULL,"
    " `player1` varchar(16) NOT NULL,"
    " `player2` varchar(16) NOT NULL,"
    " `win_player` int(11) NOT NULL,"
    " PRIMARY KEY (Play_id))"
    
)

cnx = mysql.connector.connect(host="localhost",user='root')
cursor = cnx.cursor()
def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

def createTable():
 
    for table_name in TABLES:
       
        table_description = TABLES[table_name]
        try:
            print("Creating table {}: ".format(table_name), end='')
            cursor.execute(table_description)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("already exists.")
            else:
                print(err.msg)
        else:
            print("OK")

def restoreDb(history):
    try:
        cursor.execute("USE {}".format(DB_NAME))
        createTable()
    except mysql.connector.Error as err:
        print("Database {} does not exists.".format(DB_NAME))
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            create_database(cursor)
            print("Database {} created successfully.".format(DB_NAME))
            cnx.database = DB_NAME
            cursor.execute("USE {}".format(DB_NAME))
            createTable()
            oldTable(history)
        else:
            print(err)
            exit(1)
def oldTable(history):
    for i in range(len(history)):
        print(history[i])
        temData={
            "played_date":None,
            "player1":None,
            "player2":None,
            "winPlayer":None

        }
        for key,value in Dict.items(history[i]):
            temData[key]=value
        updateDb(time=temData["played_date"],p1=temData["player1"],p2=temData["player2"],winPlayer=temData["win_player"])
 
def updateDb(time,p1,p2,winPlayer):
    cnx.database = DB_NAME
    data = (time,p1 , p2, winPlayer)
    quary=("INSERT INTO plays"
        "(played_date,player1,player2,win_player)"
            "VALUES (%s, %s, %s, %s)"
        )
    cursor.execute(quary, data)
    cnx.commit()
    return

def insertData(p1,p2,winPlayer):
    timeNow=datetime.now().date()
    updateDb(timeNow,p1,p2,winPlayer)
    return
    
def history():
    cnx.database = DB_NAME
    quary=("SELECT COUNT(Play_id),win_player FROM  plays GROUP BY win_player " )
    cursor.execute(quary)
    data={}
    total=0
    for (playersCount, status ) in cursor:
        
        data[status]=playersCount
        total+=playersCount
    data["total"]=total
    print(data)
    return data

def pastPlays():
    cnx.database = DB_NAME
    quary=("SELECT * FROM  plays" )
    cursor.execute(quary)
    data=[]
    tem=[]
    # print(cursor)
    for (id,played_date,player1,player2,win_player) in cursor:
        tem=[id,played_date,player1,player2,win_player]
        data.append(tem)
        # print(id)
    
    
    # print(data)
    return data
