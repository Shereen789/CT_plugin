from flask import Flask
app = Flask(__name__)


@app.route("/")
def index():
    return "Welcome to CT0"


@app.route("/repo/contributors?identifier=${encodedIdentifier}")
def route1():
    return "route_1 /repo/contributors"


@app.route("/data/apptoken?token=${nowInSecs()}")
def route2():
    return "route_2 /data/apptoken?token=${nowInSecs()} "


@app.route("/users/plugin/state")
def route3():
    return "route_3 /users/plugin/state "


@app.route("/users/me")
def route4():
    return "route_4 /users/me"


@app.route("/users/${user.id}")
def route5():
    return "route_5 /users/${user.id}"


@app.route("/dashboard/commits")
def route6():
    return "route_6 /dashboard/commits "


@app.route("/projects/codeSummary${qryStr}")
def route7():
    return "route_7 /projects/codeSummary$"


@app.route("/projects/contributorSummary${qryStr}")
def route8():
    return "route_8 projects/contributorSummary$"


@app.route("/dashboard?showMusic=false&showGit=${showGitMetrics}&showRank=false&linux=${isLinux()}&showToday=false")
def route9():
    return "route_9/dashboard?showMusic=false&showGit"


@app.route("/ping")
def route10():
    return "route_10 /ping "


@app.route("/sessions/summary?refresh=true")
def route11():
    return "route_11 /sessions/summary?refresh=true"


@app.route("/projects${qryStr}")
def route12():
    return "route_12 /projects${qryStr}"


@app.route("/repo/info")
def route13():
    return "route_13 /repo/info"


@app.route("/commits/latest?identifier=${encodedIdentifier}&tag=${encodedTag}&branch=${encodedBranch}")
def route14():
    return "route_14 /commits/latest?identifier"
# SoftwarePost
@app.route("/users/invite")
def route15():
    return "route_15 /users/invite"


@app.route("/data/heartbeat")
def route16():
    return "route_16 /data/heartbeat"


@app.route("/data/liveshare")
def route17():
    return "route_17 /data/liveshare"


@app.route("/repo/contributors")
def route18():
    return "route_18 /repo/contributors"


@app.route("/commits")
def route19():
    return "route_19 /commits"


@app.route("/data/onboard")
def route20():
    return "route_20 /data/onboard"


@app.route("/favicon.ico")
def route21():
    return "Route_21 favicon"
