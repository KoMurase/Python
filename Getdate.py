#現在の日時を取得する
#フォーマットを指定して取得する
#日付を計算するモジュール
#扱うクラス[date,time,datetime]=[日付,時刻,日付と時刻]を表現
#date.time.today/datetime.datetime.now で日付を取得する
import datetime
class getdate:
    def goal(m,n):
    #現在の日付
    today=datetime.date.today()
    print(today)
    #現在の日付と日時
    date2=datetime.datetime.now()
    print(date2)
    goal_day=datetime.date(m,n)
    dt=goal_day-today
    return '目標まで'+str(dt.days)+'日あります'

#次やりたいこと>>>curri.pyで継承させる
