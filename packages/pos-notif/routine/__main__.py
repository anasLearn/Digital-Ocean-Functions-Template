from src.functionalities.routine import main_call
from datetime import datetime


def main(args):
    test = args.get("test", False)
    manual = args.get("manual", False)
    main_call(test=test, manual=manual)
    return {
        "time": 'now: {}'.format(datetime.now()),
        "message": "Running the main call with parameters\n{}".format(args)
    }
