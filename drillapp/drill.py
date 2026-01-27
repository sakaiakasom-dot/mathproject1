#drillapp\drill.py

from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from .models import students, series

drill_bp = Blueprint("drill", __name__, url_prefix = "/drill")

@drill_bp.route("/question/<int:hrno>")
def question_detail(hrno):
    student = students[hrno]
    pdfname = series.question_address(student.question_id)
    return render_template("drill/drill.html", student = student, pdfname = pdfname)

@drill_bp.route("/answer/<int:hrno>")
def answer_detail(hrno):
    student = students[hrno]
    pdfname = series.answer_address(student.question_id)
    return render_template("drill/drill.html", student = student, pdfname = pdfname)
    
@drill_bp.route("/previous/<int:hrno>")
def previous_question(hrno):
    student = students[hrno]
    if student.question_id > 1:
        student.question_id -= 1
    student.status = 1
    return redirect(url_for("drill.question_detail", hrno = hrno))

@drill_bp.route("/start/<int:hrno>")
def start_question(hrno):
    student = students[hrno]
    student.question_id = 1
    student.status = 1
    return redirect(url_for("drill.question_detail", hrno = hrno))
  
@drill_bp.route("/next/<int:hrno>")
def next_question(hrno):
    student = students[hrno]
    if student.question_id < series.question_counts:
        student.question_id += 1
    student.status = 1
    return redirect(url_for("drill.question_detail", hrno = hrno))
  
@drill_bp.route("/support_request/<int:hrno>")
def support_request(hrno):
    student = students[hrno]
    student.status = 2
    return redirect(url_for("drill.question_detail", hrno = hrno))

@drill_bp.route("/support_end/<int:hrno>")
def support_end(hrno):
    student = students[hrno]
    student.status = 1
    return redirect(url_for("drill.question_detail", hrno = hrno))

