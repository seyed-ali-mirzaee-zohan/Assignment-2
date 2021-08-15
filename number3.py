Seconds=int(input( "Please enter the total number of seconds : "))
Hour=Seconds//3600
total_Minutes=Seconds-3600*Hour
Minutes=total_Minutes//60
Second=total_Minutes-60*Minutes
print("((",Hour,":",Minutes,":",Second,"))")