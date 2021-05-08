
"""import os
import smtplib,ssl

email_address=os.environ.get('EMAIL_USER')
email_password=os.environ.get('EMAIL_PASS')

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(email_address,email_address)

    subject="lets go out tomorrow"
    body="lets go to the cinema"

    msg=f'subject: {subject}\n\n{body}'

    smtp.sendmail(email_address, 'favourfunke97@gmail.com', msg)"""



import smtplib
from smtplib import SMTP

context="""\
subject: HANNY JOB APPLICATION

Dear favour,
 Thank you for applying for project Hanny. we'll need you to complete the following task by clicking on the link below:
 www.Hanny.Job.com
"""

mail=smtplib.SMTP('smtp.gmail.com', 587)
mail.ehlo()
mail.starttls()
mail.login('favourfunke97@gmail.com','Oloruntoba97')
mail.sendmail('favourfunke97@gmail.com','daviskatin11@gmail.com', context)
mail.close()