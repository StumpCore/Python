import smtplib, ssl
import threading
import time

#smtplib , python built in library to send emails SMTP or ESMTP listener daemon
class MyThread(threading.Thread):
    def __init__(self, threadID, name, counter,sdr,pwp,rcv,msg,spm, *args, **kwargs):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.sdr = sdr
        self.pwp = pwp
        self.rcv = rcv
        self.msg = msg
        self.args = args
        self.kwargs = kwargs
        self.spm =spm

    def run(self):
        print("Starting " + self.name)
        sending_mail(self.sdr, self.pwp, self.rcv, self.msg, self.spm)
        print("Exiting " + self.name)


def sending_mail(sender_adr, pw, receiver_adr, msg, spam, *args, **kwargs):
    """Sending an email to specific contact.
    Please use on test purposes only.
    The file was created for learning purpose only.
    """

    print(sender_adr, pw, receiver_adr,msg)

    #Creating the SMTP_SSL
    port = 465 #For SSL
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context = context) as server:
        server.login(sender_adr, pw)

        try:
            for i in range(1,spam):
                server.sendmail(sender_adr, receiver_adr, msg)
    
        except SMTPException as e:
            print("Error: unable to send email:", str(e))


if __name__ == '__main__':

    sender_adr = input("Please enter your sender gmail account: ")
    pw = input("Please enter your sender email-pw: ")
    receiver_adr = input("Please enter your target email: ")
    msg = input("Please enter your message: ")
    spm_ct = input("Please enter your SPAM amount: ")


    #increase number of threads by copy
    t1 = MyThread(1, "Thread-1",1,sender_adr,pw,receiver_adr,msg, spm_ct)
    t1.start()



