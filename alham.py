hour, minute = map(int,input().split())

if minute - 45 < 0:
    
    hour -= 1
    minute = 60 + (minute-45)

    if hour < 0:
        hour = hour*0 + 23

else:
    minute=minute-45

print('{0} {1}'.format(hour,minute))



    

