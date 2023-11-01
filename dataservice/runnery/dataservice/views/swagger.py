from flask import Blueprint, jsonify, request
from database_schema import Run, User, db
from datetime import datetime
api_middleman = Blueprint('api', __name__)


@api_middleman.route('/add_runs')
def add_runs():
    # Gets a json with user with different
    # runs eg
    # {1:[{'stava_id':xx, 'distance':xx},{'stava_id':xx, 'distance':xx}],
    # 2:.......}
    added = 0
    for user, runs in request.json.items():
        for run in runs:
            db_run = Run()
            db_run.strava_id = run['strava_id']
            db_run.distance = run['distance']
            db_run.start_date = datetime.fromtimestamp(run['start_date'])
            db_run.elapsed_time = run['elapsed_time']
            db_run.average_speed = run['average_speed']
            db_run.average_heartrate = run['average_heartrate']
            db_run.total_elevation_gain = run['total_elevation_gain']
            db_run.name = run['title']
            db_run.runner = run['runner']
            db.session.add(db_run)
            added += 1

    if added > 0:
        db.session.commit()

    return jsonify({"added":added})


@api_middleman.route('/get_runs/<int:runner_id>')
def get_runs(runner_id):
    runs = db.session.query(Run).filter(Run.runner == str(runner_id))
    return jsonify([run.to_json() for run in runs])



@api_middleman.route('/getusers')
def get_users():
    users = db.session.query(User)
    page = 0
    page_size = None
    if page_size:
        users.limit(page_size)
    if page != 0:
        users = users.offset(page*page_size)

    return {'users': [user.to_json() for user in users]}