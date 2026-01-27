#drillapp\hint.py

from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from .models import students, Hint, hints

hint_bp = Blueprint("hint", __name__, url_prefix = "/hint")

@hint_bp.route("/<int:hrno>/detail")
def hint_detail(hrno):
    student = students[hrno]
    question_id = student.question_id

    return render_template("hint/detail.html", hints = hints, student = student)


@hint_bp.route("/<int:hrno>/new", methods = ["GET", "POST"])
def new_hint(hrno):
    student = students[hrno]
    if request.method == "POST":
        question_id = student.question_id
        content = request.form["content"]
        
        new_hint = Hint(hrno, question_id, content)
        new_hint.hint_id = len(hints) + 1
        hints.append(new_hint)
        flash("ヒントを登録しました")
        return redirect(url_for("hint.hint_detail", hrno = hrno))
    return render_template("hint/new.html", student = student)
    
@hint_bp.route("/good/<int:hint_id>/<int:hrno>")
def add_good(hint_id, hrno):
    student = students[hrno]
    for i in hints:
        if i.hint_id == hint_id:
            i.good_students.add(hrno)
            i.good_count = len(i.good_students)
    return redirect(url_for("hint.hint_detail", hrno = hrno))
    
