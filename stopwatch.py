import time, sys

def watch(start):
    laps = [start]
    while True:
        option = input('stop or lap? \n> ')
        if option == 'stop':
            end = time.time()
            break
        elif option == 'lap': laps.append(int(time.time()))
    print(str(round(end - start,2)),'seconds')
    
    for i in range(1, len(laps)):
        print("Lap %d: %f"%(int(i), laps[i] - laps[i-1]))

def starter():
    option = input("input start to start stopwatch \n> ")
    if option == 'start': watch(time.time())
    elif option in ("quit","exit"): sys.exit()
    print('-'* 60)
    starter()

starter()


