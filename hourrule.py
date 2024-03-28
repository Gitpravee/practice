def divied(num,den):
    qot = num // den
    rem = num % den
    return qot, rem
    
Total = 10000
Effort = int(input("what is Your Daily efforts:"))
#Days = Total // Effort
#Rem_hrs = Total % Effort
days,remhrs = divied(Total,Effort)

#Months = Days // 30
#Days = Days % 30
month,days = divied(days,30)

#Years = Months // 12
#Months = Months % 12
year,month = divied(month,12)

print ( year,"years", month,"months", days,"Days", remhrs, "hrs" )
