import dhooks
import os
import time
from os import system
from dhooks import Webhook

init()



system("title webhook tool by kaos")
hook2 = input("enter webhook: ")
while True:
    hook = Webhook((hook2))
    os.system('cls' if os.name == 'nt' else 'clear')
    print("succesfully connected to webhook")
    print("")
    send = input("what do you want to send: ")
    hook.send(send)
    print("succesfully sent", send)
    time.sleep(1)
