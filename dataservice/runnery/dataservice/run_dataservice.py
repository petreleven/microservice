import argparse
from chaussette.server import make_server
from app import create_app
import sys
import signal
from database_schema import db, init_database


def _quit(signal, frame):
    print("Stopping dataservice!")
    # add any cleanup code here
    sys.exit(0)


def main(args=sys.argv[1:]):
    parser = argparse.ArgumentParser(description="Runnerly dataservice")
    parser.add_argument('--fd', type=int, default=None)
    parser.add_argument(
        '--config-file', help='path_to_config_file', type=str, default=None)
    args = parser.parse_args(args=args)

    # Load in config file and create app
    
    app = create_app(args.config_file)
    host = app.config.get('HOST', '0.0.0.0')
    port = app.config.get('PORT', 5000)
    debug = app.config.get('DEBUG', False)

    signal.signal(signal.SIGINT, _quit)
    signal.signal(signal.SIGTERM, _quit)
    db.init_app(app)
    with app.app_context():
        db.create_all()
        init_database()

    if args.fd is not None:
        make_server(app=app, host=f"fd://{int(args.fd)}", )
    else:
        app.run(debug=debug, host=host, port=port)


if __name__ == "__main__":
    main()
