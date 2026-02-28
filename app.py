from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    focus_score = None
    timetable = []
    graph_url = None

    if request.method == 'POST':
        study = float(request.form['study'])
        distraction = float(request.form['distraction'])

        focus_score = round((study / (study + distraction)) * 100, 2)

        # AI-style logic
        if focus_score >= 80:
            timetable = [
                "6:00 AM - 8:00 AM : Deep Study",
                "10:00 AM - 12:00 PM : Practice",
                "3:00 PM - 4:00 PM : Revision",
                "8:00 PM - 9:00 PM : Reading"
            ]
        elif focus_score >= 50:
            timetable = [
                "7:00 AM - 8:30 AM : Study",
                "11:00 AM - 12:00 PM : Practice",
                "5:00 PM - 6:00 PM : Revision"
            ]
        else:
            timetable = [
                "Study 30 mins",
                "Break 10 mins",
                "Repeat 3 times",
                "Reduce Mobile Usage"
            ]

        # Create graph
        if not os.path.exists("static"):
            os.mkdir("static")

        plt.figure()
        plt.bar(["Study", "Distraction"], [study, distraction])
        plt.title("Focus Analysis")
        plt.ylabel("Hours")
        plt.savefig("static/graph.png")
        plt.close()

        graph_url = "static/graph.png"

    return render_template('index.html', focus=focus_score, timetable=timetable, graph=graph_url)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)