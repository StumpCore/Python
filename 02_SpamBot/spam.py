import smtplib
import threading
#smtplib , python built in library to send emails SMTP or ESMTP listener daemon


class MyThread(threading.Thread):
    def __init__(self, threadID, name, counter, sdr, rpr):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.sdr = sdr
        self.rpr = rpr

    def run(self):
        print("Starting " + self.name)
        sending_mail(self.sdr, self.rpr, self.name)
        print("Exiting " + self.name)


def sending_mail(sadr, radr, *args):
    port = 1025  # FOr SSL
    server = smtplib.SMTP("localhost", port=port)
    sender_adr = sadr
    receiver_adr = radr

    try:
        for i in range(1,10000):
            message = str(args)+ " SPAM No.:"+ str(i)
            server.sendmail(sender_adr, receiver_adr, message)

    except:
        print("not possible")

#Step: 1 SMTP_SSL() First


sendermail = "Sender@gmx.net"
receivermail = "Receiver@gmx.net"


t1 = MyThread(1, "Thread-1",1, sendermail, receivermail)
t2 = MyThread(2, "Thread-2",2, sendermail, receivermail)
t3 = MyThread(3, "Thread-3",3, sendermail, receivermail)
t4 = MyThread(4, "Thread-4",4, sendermail, receivermail)
t5 = MyThread(5, "Thread-5",5, sendermail, receivermail)

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()


