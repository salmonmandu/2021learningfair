daylist=[]
namelist=[]
homelist=[]
templist=[]

for i in range(0,3,1):

    day = input("날짜 입력 : 예)21/11/01 --->")
    daylist.append(day)

    name = input("이름 입력 : 예)홍길동 --->")
    namelist.append(name)

    home = input("거주구 입력 : 예)종로구 --->")
    homelist.append(home)

    temp = float(input("체온입력 : 예)37.5 --->"))
    templist.append(temp)

    print('-'*40)

    if templist[i] > 37.5:

        print(daylist[i], namelist[i], '님은 출입이 불가능 하십니다.')

        print('-'*40)
