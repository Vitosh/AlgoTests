from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse
import sqlite3
import matplotlib.pyplot as plt
import numpy as np

VAR_DB_NAME = "servers.db"
VAR_TABLE_COLLECTION_NAME = "server100"
VAR_COLUMN_NAME = "webAddress"
VAR_TABLE_PASSED_NAME = "passed"
VAR_COLUMN_SERVER_NAME = "serverType"


def Generate_Table(webSite="http://register.start.bg", myImportedList=[]):
    Create_Tables(webSite)

    connection = sqlite3.connect(VAR_DB_NAME)
    cursor = connection.cursor()

    myHeaders = {}
    ua1 = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
    myHeaders["User-Agent"] = ua1

    r = requests.get(webSite, headers=myHeaders)

    mySoup = BeautifulSoup(r.text)
    myList = []
    myImprovedList = []

    for link in mySoup.find_all('a'):
        if (link.get('href') is not None
                and len(link.get('href')) > 8
                and link.get('href')[:1] != "/"
                and "javascript" not in link.get('href')):

            myList.append(link.get('href'))

    for line in myList:
        ok = True
        if (line[:12] == "link.php?id="):
            line = webSite + "/" + line
        try:
            r = requests.head(line, headers=myHeaders, timeout=3)

            if (r.status_code != 200):
                line = r.headers["location"]

            line = urlparse(line)
            line = line.netloc

        except Exception:
            ok = False

        if line not in myImprovedList and len(line) > 6 and ok and line not in myImportedList:
            myImprovedList.append(line)

    for line in myImprovedList:
        ok = True
        try:

            if (line[:4] != "http"):
                line = "http://" + line

            r = requests.head(line, headers=myHeaders, timeout=3)

            serverType = r.headers["server"]

            if (r.status_code == 200):
                serverSite = line
            else:
                serverSite = r.headers["location"]

        except Exception:
            print("Exception - {}".format(line))
            ok = False

        if ok:
            print(serverSite)
            sqlText = """INSERT INTO "{}" (webAddress,serverType, accessedFrom)
                     VALUES ("{}","{}","{}");""".format(VAR_TABLE_COLLECTION_NAME, serverSite, serverType,  webSite)

            cursor.execute(sqlText)
            connection.commit()

    cursor.close()
    connection.close()


def Create_Tables(website):
    connection = sqlite3.connect(VAR_DB_NAME)
    cursor = connection.cursor()

    create_users_table = """CREATE TABLE IF NOT EXISTS
                        {} (id INTEGER PRIMARY KEY, {} TEXT, serverType TEXT, accessedFrom TEXT);
                        """.format(VAR_TABLE_COLLECTION_NAME, VAR_COLUMN_NAME)

    create_visited_table = """CREATE TABLE IF NOT EXISTS
                        {} (id INTEGER PRIMARY KEY, {} TEXT);
                        """.format(VAR_TABLE_PASSED_NAME, VAR_COLUMN_NAME)

    add_website = """INSERT INTO "{}" ("{}") VALUES ("{}");""".format(
        VAR_TABLE_PASSED_NAME, VAR_COLUMN_NAME, website)

    cursor.execute(create_users_table)
    cursor.execute(create_visited_table)
    cursor.execute(add_website)

    connection.commit()

    cursor.close()
    connection.close()


def Read_Table(db_name, table_name, column_name):

    connection = sqlite3.connect(VAR_DB_NAME)
    cursor = connection.cursor()
    myList = []

    sql = """SELECT {} FROM {};"""
    cursor.execute(sql.format(column_name, table_name))

    for row in cursor:
        myList.append(row[0])

    cursor.close()
    connection.close()

    return myList


def Delete_Tables():
    connection = sqlite3.connect("servers.db")
    cursor = connection.cursor()

    delete_server100 = """DELETE FROM server100;"""
    delete_passed = """DELETE FROM passed;"""

    cursor.execute(delete_server100)
    cursor.execute(delete_passed)

    connection.commit()


def Lets_Crawl():

    myReadList = Read_Table(
        VAR_DB_NAME, VAR_TABLE_COLLECTION_NAME, VAR_COLUMN_NAME)

    myCrawledList = Read_Table(
        VAR_DB_NAME, VAR_TABLE_PASSED_NAME, VAR_COLUMN_NAME)

    siteToCrawl = myReadList.pop(0)
    while siteToCrawl in myCrawledList:
        siteToCrawl = myReadList.pop(0)

    Generate_Table(webSite=siteToCrawl, myImportedList=myReadList)


def Start(times):

    for x in range(1, times):
        Lets_Crawl()
        x += 1


def Print_Results(values=2):
    myReadList = Read_Table(
        VAR_DB_NAME, VAR_TABLE_COLLECTION_NAME, VAR_COLUMN_SERVER_NAME)

    myDictionary = List_To_Dictionary(myReadList)
    print(myDictionary.values())
    x = np.char.array(list(myDictionary.keys()))
    y = np.array(list(myDictionary.values()))

    colors = ['yellowgreen', 'red', 'gold', 'lightskyblue', 'white', 'lightcoral',
              'blue', 'pink', 'darkgreen', 'yellow', 'grey', 'violet', 'magenta', 'cyan']

    porcent = 100. * y / y.sum()

    patches, texts = plt.pie(y, colors=colors, startangle=90, radius=1.2)
    labels = ['{0} - {1:1.2f} %'.format(i, j) for i, j in zip(x, porcent)]

    patches, labels, dummy = zip(
        *sorted(zip(patches, labels, y), key=lambda x: x[2], reverse=True))
    plt.legend(patches, labels, fontsize=12)

    plt.show()


def List_To_Dictionary(myList):
    myDictionary = {}
    servApache = "Apache"
    servNginx = "Nginx"
    servMicrosoft = "Microsoft-IIS"
    servOracle = "Oracle-Application-Server"
    servTPD = "lighttpd"

    for serverType in myList:

        if servApache.lower() in serverType.lower():
            serverType = servApache

        elif servNginx.lower() in serverType.lower():
            serverType = servNginx

        elif servMicrosoft.lower() in serverType.lower():
            serverType = servNginx

        elif servOracle.lower() in serverType.lower():
            serverType = servNginx

        elif servTPD.lower() in serverType.lower():
            serverType = servNginx

        if serverType not in myDictionary:
            myDictionary[serverType] = 1
        else:
            myDictionary[serverType] += 1

    return myDictionary

# Start(10) <= uncomment to gather for 10 more sites
Print_Results()
print("That's all folks!")