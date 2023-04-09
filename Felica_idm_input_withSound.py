# 2023/04/08 Python IDm Input 1 time/sec and keyboard input

from smartcard.util import toHexString
from smartcard.System import readers as get_readers
from playsound import playsound
import pyautogui
import time

### Setting ###
pathToSoundFile="./playsound/soundFileName.mp3"
###############

readers = get_readers()
print(readers)

def main():
    previousIDm=None
    while True:
        try:
            currentIDm=readIDm()
            if previousIDm != currentIDm:
                playsound(pathToSoundFile)
                keyboardInput(currentIDm)                
                previousIDm=currentIDm
        except:
            previousIDm=None
        time.sleep(1)

def readIDm():
    conn = readers[0].createConnection()
    conn.connect()

    send_data = [0xFF, 0xCA, 0x00, 0x00, 0x00]
    recv_data, sw1, sw2 = conn.transmit(send_data)
    print(toHexString(recv_data))
    return(toHexString(recv_data))

def keyboardInput(input):
    pyautogui.write(input)
    pyautogui.press("enter")

if __name__ == "__main__":
    main()
