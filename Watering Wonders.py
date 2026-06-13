import time
import subprocess
from datetime import datetime
def mastercontrol():
        subprocess.run(['python', 'READINGMOISTURESENSOR1.py'])
        current_time = datetime.now()
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
        print(current_time)
        with open("waterlog.txt", "a") as file:
                file.write(formatted_time)
                file.write("    Readingmoisturesensor1\n")
        print ("Readingmoisturesensor1")
        subprocess.run(['python', 'READINGMOISTURESENSOR2.py'])
        current_time = datetime.now()
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
        print(current_time)
        with open("waterlog.txt", "a") as file:
                file.write(formatted_time)
                file.write("    Readingmoisturesensor2\n")
        print ("Readingmoisturesensor2")
        subprocess.run(['python', 'READINGMOISTURESENSOR3.py'])
        current_time = datetime.now()
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
        print(current_time)
        with open("waterlog.txt", "a") as file:
                file.write(formatted_time)
                file.write("    Readingmoisturesensor3\n")
        print ("Readingmoisturesensor3")
        subprocess.run(['python', 'READINGMOISTURESENSOR4.py'])
        current_time = datetime.now()
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
        print(current_time)
        with open("waterlog.txt", "a") as file:
                file.write(formatted_time)
                file.write("    Readingmoisturesensor4\n")
        print ("Readingmoisturesensor4")
        subprocess.run(['python', 'READINGMOISTURESENSOR5.py'])
        current_time = datetime.now()
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
        print(current_time)
        with open("waterlog.txt", "a") as file:
                file.write(formatted_time)
                file.write("    Readingmoisturesensor5\n")
        print ("Readingmoisturesensor5")
while True:
        print ("Test")
        mastercontrol()
        time.sleep(10)
