from datetime import datetime
dateDict = {0: '월요일', 1:'화요일', 2:'수요일', 3:'목요일', 4:'금요일', 5:'토요일', 6:'일요일'}
start_date = input("시작 날짜(연/월/일) -->" )
a = datetime.today().date().weekday()
today_date = datetime.today().date().strftime("%Y/%m/%d")
date_diff = datetime.now() - datetime.strptime(start_date, "%Y/%m/%d")
print(f"{start_date} 부터 오늘({today_date})까지는 {date_diff.days}일이 지났습니다")
print(f"오늘은 {dateDict[a]} 입니다.")




