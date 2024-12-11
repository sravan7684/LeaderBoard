from flask import Flask, render_template
from platform_data import fetch_codechef_data, fetch_hackerrank_data, fetch_leetcode_data

app = Flask(__name__)

users = [
    {"name": "Sravan", "codechef": "sravan7684", "hackerrank": "sravankumar7684", "leetcode": "sravan7684"},
    {"name": "Friend", "codechef": "friend_codechef", "hackerrank": "friend_hackerrank", "leetcode": "friend_leetcode"},
]

@app.route("/")
def leaderboard():
    leaderboard_data = []
    for user in users:
        codechef_score = fetch_codechef_data(user["codechef"])
        hackerrank_score = fetch_hackerrank_data(user["hackerrank"])
        leetcode_score = fetch_leetcode_data(user["leetcode"])
        total_score = sum(filter(None, [codechef_score, hackerrank_score, leetcode_score]))
        leaderboard_data.append({"name": user["name"], "total_score": total_score})
    leaderboard_data.sort(key=lambda x: x["total_score"], reverse=True)
    return render_template("index.html", leaderboard=leaderboard_data)

if __name__ == "__main__":
    app.run(debug=True)
