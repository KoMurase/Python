import math
from getdate import Getdate
print("本:「Pythonで動かして学ぶ深層学習の教科書」があと何日で終了するか計算します")

Page_All=770
print("全部で"+str(Page_All)+"ページあります")

yesterday=int(input("前回は何ページまでやった？"))
today=int(input("どこまで進んだ？"))
if (yesterday==today):
    print("進んでませんね～やる気あります？")
else:
    rest=Page_All-today
    rate=rest/(today-yesterday)
    print("あと"+str(rest)+"ページ残っていて"+"このペースだと"+str(rate)+"日かかります")
    #goal_tuki=int(input("いつまでに終わらせる？(月を入力)"))
    #goal_niti=int(input("日にちを入力"))
    goal_tuki=3
    goal_niti=4
    print('目標は'+str(goal_tuki)+'月'+str(goal_niti)+'日に終えることです')
    today_tuki=int(input("今日は(月を入力)"))
    today_niti=int(input("(日にちを入力)"))
    limit=goal_tuki-today_tuki
    goal=0
    i=1
    if(limit>1):
        if( goal_tuki==4 or goal_tuki==6 or goal_tuki==8 or goal_tuki==9 or goal_tuki==11):
            goal_tuki=31
        elif(goal_tuki==3):
            goal_tuki=28
        else:
            goal_tuki=30
        for i in limit:
            goal+=30
        goal+=today_niti
    elif(limit==1):
        if( goal_tuki==4 or goal_tuki==6 or goal_tuki==8 or goal_tuki==9 or goal_tuki==11):
            goal_tuki=31
        elif(goal_tuki==3):
            goal_tuki=28
        else:
            goal_tuki=30
        goal=goal_tuki+goal_niti
    else:
        goal=goal_niti-today_niti
    print("約"+str(goal)+"日あります")
    print("じゃあ一日"+str(math.ceil(rest/goal))+"ページやろう！！")
getdate1=Date(gatedate)
