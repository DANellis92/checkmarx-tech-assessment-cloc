import smtplib, ssl, getpass, os, os.path, subprocess, git
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from pip._internal import main




smtp_server = "smtp.gmail.com"
senderEmail = input("Enter your email:")
password = getpass.getpass(prompt="Enter your email password: ")
receivingEmail = input("Enter destination email: ")
git_url = input("Type target git repo URL and press enter: ")

print(password, senderEmail)
def parseRepo():
	return(git_url[git_url.rfind('/')+1:git_url.rfind('.')])

def pullRepo():
    repo = parseRepo()
    print ("Working with " + repo)
    if not os.path.exists("./"+repo):
        git.Git("./").clone(git_url)
    
    gitrepo = git.Repo(repo)
    gcmd = git.cmd.Git(repo)
    gcmd.pull()
    print ("Pulling repo")
    gitrepo.git.checkout("-f", "master")
    print ("Executing cloc")
    proc = subprocess.Popen(["./cloc-exe/cloc-1.92.exe","./"+repo, "--csv","--out", report , "--quiet"], stdout=subprocess.PIPE)
    proc.stdout.read()
   
def install(package):
	main(['install', package])		


# Create a secure SSL context

def sendMail():
    message = MIMEMultipart()
    message["Subject"] = "Result of cloc report for: " + git_url
    message["From"] = senderEmail
    message["To"] = receivingEmail
    print ("Preparing email from " + senderEmail + " to " + receivingEmail)
    part = MIMEBase('application', "octet-stream")
    part.set_payload(open(report, "rb").read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="'+ report +'"')
    message.attach(part)
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, 587) as server:
        server.starttls(context=context)
        server.login(senderEmail, password)
        server.sendmail(senderEmail, receivingEmail, message.as_string()) 
    print ("Email successfully sent")

report = parseRepo() + ".csv"
pullRepo()
sendMail()
