import smtplib
server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login("alexandergarces987k@gmail.com","humblemeansfake")
server.sendmail("alexandergarces987k@gmail.com","kcsamjhana61@gmail.com","hi, this is an automated mail from krish sir, thank you")
server.quit()
