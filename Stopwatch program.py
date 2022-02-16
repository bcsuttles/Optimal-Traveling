



#Timer
import time


start = input('Press enter to start')

print('The timer has started')

begin = time.time()

endtimer = input('Press enter to stop the time')

end=time.time()

elapsed = end - begin

elapsed = int(elapsed)

print('The time elapsed is',elapsed,'seconds')


#Date
from datetime import date
today = date.today()


#Time
from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)





#save in text
with open('database.txt', 'a') as external_file:
    print ('Travel Time: ', elapsed, 'seconds', file=external_file)
    print ("Date:", today, file=external_file)
    print ("Time:", current_time, file=external_file)

external_file.close()
    
    


