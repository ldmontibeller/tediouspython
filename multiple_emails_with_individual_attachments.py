import sys
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from random import randint
from time import sleep

def main():
    sender = 'sender@gmail.com'
    gmail_password = 'password'

    #Make list of recipients from a path with a txt file
    recipients = [line.strip() for line in open('C:\\Users\\...\\recipients.txt')]

    #HTML for the body of email
    html = """<h2>Thank you for reading this header!</h2>
                    <p>\
                     The regular body text goes here                
                     </p>
                    <p><strong>Here are your attachments:</strong></p><br />"""

    #Variable to control the file to attach which need to be in the same order as the recipients list
    current_file = 1

    try:
        #If another email provider is needed check the SMTP parameters online
        with smtplib.SMTP('smtp.gmail.com', 587) as s:
            s.ehlo()
            s.starttls()
            s.ehlo()
            s.login(sender, gmail_password)
            for recipient in recipients:
                # Create the enclosing (outer) message
                outer = MIMEMultipart()
                outer['Subject'] = 'Subject'
                outer['To'] = recipient
                outer['From'] = sender
                outer.preamble = 'You will not see this in a MIME-aware mail reader.\n'

                body = MIMEText(html, 'html')
                outer.attach(body)

                # Path of attachments directory
                path = 'C:\\Users\\...\\attachments\\'

                # Add the attachments to the message
                try:
                    #Attachments file names needs to follow this pattern
                    with open(path + 'Attachment base name '+ str(current_file)+ '.pdf or another file extension', 'rb') as fp:
                        msg = MIMEBase('application', "octet-stream")
                        msg.set_payload(fp.read())
                    encoders.encode_base64(msg)
                    msg.add_header('Content-Disposition', 'attachment', filename= 'Attachment filename')
                    outer.attach(msg)
                except:
                    print("Unable to open one of the attachments. Error: ", sys.exc_info()[0])
                    raise

                composed = outer.as_string()

                s.sendmail(sender, recipient, composed)
                print("Email " + str(current_file) + " sent!")
                current_file += 1
                sleep(randint(1,2))
        s.close()
    except:
        print("Unable to send the email. Error: ", sys.exc_info()[0])
        raise


if __name__ == '__main__':
    main()