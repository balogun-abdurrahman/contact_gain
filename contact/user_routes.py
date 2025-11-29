import os, secrets
from flask import render_template, request, redirect, session, flash, jsonify, Response

from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename                                                                  
from datetime import datetime
from contact import app
from contact.models import User, db, Admin
from sqlalchemy import desc
from sqlalchemy.orm.exc import NoResultFound

# @app.errorhandler(404)
# def page_not_found(error):
#     return render_template("user/error404.html",error=error), 404


@app.route("/")
def index_page():
    contact_listed = db.session.query(User).all()
    contact_listed_len = len(contact_listed)
    vcf_status = db.session.query(Admin).filter(Admin.admin_email == "balogunabdurrahman101@gmail.com").first() 
    vc_st = vcf_status.vcf_status
    return render_template("user/home.html",lent = contact_listed_len, vcf_stat = vc_st)



@app.route("/contact_upload/",methods=["POST","GET"])
def upload_page():
    if request.method == "GET":
        return render_template("user/home.html") 
    else:
        fname = request.form.get("fullname")
        email = request.form.get("email")
        number = request.form.get("number")



        existing_email = db.session.query(User).filter(User.user_email==email).first()
        existing_number = db.session.query(User).filter(User.user_number==number).first()
        if existing_email:
            flash("errormsg","Email already exist")
            return redirect("/#form")
        if existing_number:
            flash("errormsg","Number already exist")
            return redirect("/#form")

        user =User(user_fullname=fname,user_email=email,user_number=number)
        db.session.add(user)
        db.session.commit()
        flash("feedback","Contact uploaded successfuly ")
    return redirect("/#form")


@app.route("/download_vcf/",methods=["POST","GET"])
def download_vcf():
    contacts = User.query.all()

    vcf_data = ""

    for c in contacts:
        vcf_data += f"""
            BEGIN:VCARD
            VERSION:1.0
            FN:{c.user_fullname}
            EMAIL:{c.user_email}
            TEL:{c.user_number}
            END:VCARD
            """

    return Response(
        vcf_data,
        mimetype="text/vcard",
        headers={
            "Content-Disposition": "attachment; filename=codex_contact_gain.vcf"
        }
    )


