import sqlite3
def dailywordhistory():
    conn=sqlite3.connect('word.db')
    cn=conn.cursor()
    query="SELECT word FROM dailywords ORDER BY date "
    cn.execute(query)
    x=cn.fetchall()
    z=len(x)
    cn.execute(query)
    k=cn.fetchmany(z-1)
    k.reverse()
    return k
def getdailywordhistory():
    x=dailywordhistory()
    w=[]
    for word in x:
        word=list(word)
        for words in word:
            w.append(words)
    return w
