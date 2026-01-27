#drillapp\auth.py

from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from .models import students, seats, series

auth_bp = Blueprint("auth", __name__, url_prefix = "/auth")


@auth_bp.route("/login", methods = ["GET", "POST"])
def student_register():
    if request.method == "POST":
        hrno = int(request.form["hrno10"]) * 10 + int(request.form["hrno01"])
        
        for i in seats:
            for j in i:
                if j == hrno:
                    flash("HRNOは使用されています")
                    return redirect(url_for("auth.student_register"))
        
        student = students[hrno]
        
        seat_x = int(request.form["seat_x"])
        seat_y = int(request.form["seat_y"])

        if seats[seat_y - 1][seat_x - 1] != 0:
            flash("座席が重なっています")
            return redirect(url_for("auth.student_register"))
        
        else:
            seats[seat_y - 1][seat_x - 1] = hrno
            student.seat_x = seat_x
            student.seat_y = seat_y
        
        flash("登録完了！")
        return redirect(url_for("auth.student_confirm", hrno = hrno))
    return render_template("auth/login.html")

@auth_bp.route("/trial", methods = ["GET", "POST"])
def teacher_trial():
    if request.method == "POST":
        hrno = int(request.form["hrno10"]) * 10 + int(request.form["hrno01"])
        
        student = students[hrno]
        
        if student.seat_x == -1:
            flash("どなたががこの番号を利用中です。")
            return redirect(url_for("teacher_trial"))
        
        else:
            student.seat_x = -1
        
        return redirect(url_for("drill.start_question", hrno = hrno))
    return render_template("auth/trial.html")

@auth_bp.route("/confirm/<int:hrno>")
def student_confirm(hrno):
    student = students[hrno]
    return render_template("auth/confirm.html", student = student)
    
@auth_bp.route("/logout/<int:hrno>")
def reset_seat(hrno):
    student = students[hrno]
    seats[student.seat_y - 1][student.seat_x - 1] = 0
    flash("登録解除")
    return redirect(url_for("auth.student_register"))
                
@auth_bp.route("/setting", methods = ["GET", "POST"])
def set_questions():
    if request.method == "POST":
        series.question_series = int(request.form["series_id"])
        series.question_counts = int(request.form["question_counts"])
        flash("フォルダを"+str(series.question_series) + "番に設定しました。")
        flash("問題数を" + str(series.question_counts)+"に設定しました。")
        return redirect(url_for("auth.set_questions"))
    return render_template("auth/setting.html")