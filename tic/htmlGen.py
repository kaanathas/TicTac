import webbrowser
from tic import data as db

def htmlPage():
    pastPlays=db.pastPlays()
    tableData=""
    for recod in pastPlays:
        
        row="""
        <tr>
        <td>{}</td>
        <td>{}</td>
        <td>{}</td>
        <td>{}</td>
        <td>{}</td>
        </tr>
        """.format(str(recod[0]),recod[1],recod[2],recod[3],str(recod[4]))
        tableData=tableData+row

    f = open('playHistory.html','w')
    table=""" <table id="t01" style="width:50%">
    <tr>
        <th>id</th>
        <th>played_date</th>
        <th>player1</th>
        <th>player2</th>
        <th>win_player</th>
    </tr>
    {}
    </table> """.format(tableData)
    message = """<html>
    <head>
    <style>
        table, th, td {{
        border: 1px solid black;
        border-collapse: collapse;
        }}
        th, td {{
        padding: 15px;
        text-align: left;
        }}
        #t01 tr:nth-child(even) {{
        background-color: #eee;
        }}
        #t01 tr:nth-child(odd) {{
        background-color: #fff;
        }}
        #t01 th {{
        background-color: black;
        color: white;
        }}

    </style>
    </head>
    <body>
    <h1>Plays History</h1>
    {}
    </body>
    </html>""".format(table)

    f.write(message)
    f.close()

    webbrowser.open_new_tab('playHistory.html')