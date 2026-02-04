#drillapp\summary.py

from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from .models import students, seats, hints, series

summary_bp = Blueprint("summary", __name__, url_prefix = "/summary")


@summary_bp.route("/location")
def show_location():
    locations = []
    for i in range(7):
        location_row = []
        for j in range(6):
            location_row.append(["　", "未登録", "　"])
        locations.append(location_row)
    
    for i in range(7):
        for j in range(6):
            hrno = seats[i][j]
            if hrno != 0:
                question_now = str(students[hrno].question_id) + "問目"
                status_now = students[hrno].status
                locations[6 - i][5 - j] = ["No:" + str(hrno), question_now, status_now]
            
    return render_template("summary/location.html", locations = locations)
    
@summary_bp.route("/")
def show_menu():
    return render_template("summary/menu.html")

@summary_bp.route("/progress")
def show_progress():
    progresses = []
    for i in range(series.question_count):
        progresses.append([i + 1 ,0, 0])
    for i in range(7):
        for j in range(6):
            hrno = seats[i][j]
            if hrno != 0:
                question_now = students[hrno].question_id
                status_now = students[hrno].status
                                
                progresses[question_now - 1][1] += 1
                if status_now == 2:
                    progresses[question_now - 1][2] += 1
                
    return render_template("summary/progress.html", progresses = progresses)

@summary_bp.route("/allhints")
def show_allhints():
    return render_template("summary/allhints.html", hints = hints)
    
@summary_bp.route("/good_by_teacher/<int:hint_id>")
def add_good_by_teacher(hint_id):
    for i in hints:
        if i.hint_id == hint_id:
            i.good_students.add(-1)
            i.good_count = len(i.good_students)
    return redirect(url_for("summary.show_allhints"))
    
@summary_bp.route("/challenge/<int:hrno>")
def show_challenge(hrno):
    student = students[hrno]

    locations = []
    for i in range(7):
        location_row = []
        for j in range(6):
            location_row.append(["　", "挑戦前", "　"])
        locations.append(location_row)
    
    for i in range(7):
        for j in range(6):
            hrno_for_location = seats[i][j]
            student_for_location = students[hrno_for_location]
            if student.hrno == hrno_for_location:
                locations[i][j][1] = "あなた"
            elif student_for_location.question_id == series.question_count:
                locations[i][j][1] = "挑戦中"
            
    return render_template("summary/challenge.html", locations = locations, student=student)