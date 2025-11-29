from flask import render_template, request, redirect, session, flash

from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from contact import app
from contact.models import User, db, Admin

@app.route("/admin/",methods=["POST","GET"])
def admin():
   users = User.query.all()
   lens=len(users)
   vcf_status = db.session.query(Admin).filter(Admin.admin_email == "balogunabdurrahman101@gmail.com").first() 
   vc_st = vcf_status.vcf_status
   return render_template("admin/home.html", user=users, lenn=lens,vcf_stat = vc_st)

@app.route("/activate_vcf/")
def activate_vcf():

   id=1   
   prof = Admin.query.get(id)
   prof.vcf_status = "Active"
   db.session.commit()
   flash("feedback","VCF activated succesfully ")
   return redirect("/admin/")

@app.route("/deactivate_vcf/")
def deactivate_vcf():
   id=1   
   prof = Admin.query.get(id)
   prof.vcf_status = "Inactive"   
   db.session.commit()
   flash("feedback","VCF Deactivated succesfully ")
   return redirect("/admin/")

