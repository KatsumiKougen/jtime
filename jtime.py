import time

week={
    "Sun":"日",
    "Mon":"月",
    "Tue":"火",
    "Wed":"水",
    "Thu":"木",
    "Fri":"金",
    "Sat":"土",
}
month={
    "Jan":1,
    "Feb":2,
    "Mar":3,
    "Apr":4,
    "May":5,
    "Jun":6,
    "Jul":7,
    "Aug":8,
    "Sep":9,
    "Oct":10,
    "Nov":11,
    "Dec":12,
}

def gz_jikan():
    strlist=time.asctime().split(" ")
    hhmmss=strlist[3].split(":")
    return "%s年%s月%s日 (%s) %s時%s分%s秒"%(strlist[4],month[strlist[1]],strlist[2],week[strlist[0]],hhmmss[0],hhmmss[1],hhmmss[2])
