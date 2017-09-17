#make new folders in files automatically

import os
n = 5
while n < 14:
    newpath = r'C:\Users\Davidlwl\Desktop\CAT\Lesson'+' '+str(n) 
    if not os.path.exists(newpath):
        os.makedirs(newpath)
        n +=1
