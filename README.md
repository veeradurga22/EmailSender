# EmailSender

Email Sender is a Python program to send Email using python Tkinter interface..

Python offers a library to send emails- “SMTP lib”.
"smtplib" creates a Simple Mail Transfer Protocol client session object which is used to send emails 
to any valid email id on the internet. 

In this code I had used the SMTP module and Tkinter..

Here We are going to learn how i was sent email in this code..

  1) First we have to import the Tkinter module and make the interface as shown in the 'Output.png' image.
  2) Take the inputs from the Tkinter i.e toaddress , subject , Body of the mail and if user wanna upload attachment(file),he can attach..
  3) Pass these inputs to the Email File. 
  4) In this Email file first we need to import the SMTP module.
  5) After that create a session, we will be using its instance SMTP to encapsulate an SMTP connection. 
  6) For security reasons, now put the SMTP connection in TLS mode. TLS (Transport Layer Security) encrypts all the SMTP commands.
     After that, for security and authentication, you need to pass your Gmail account credentials in the login instance. 
     The compiler will show an authentication error if you enter an invalid email id or password.
  7) After that store the Subject we want to send , body and file in the variables 
  8) then after click on the Send email. The mail will send to the 'toaddr' person. 


# Note:
 While giving the login credentials in the code .. we are using the third party app ( Using python code ), Email won't allow them .. For that we need to 'ON' the 'Less Security Apps' in the Manage My account in gmail.
  
