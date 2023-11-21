import argparse
from config import env_config
from generate_files import generate_readme, generate_solution
from api import get_user, get_all_submissions, get_solution, login


logger = env_config.logger

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument(
    "--username",
    type=str,
    help="Leetcode username. you can also pass it as an environment variable LEETCODE_USERNAME",
)
arg_parser.add_argument(
    "--password",
    type=str,
    help="Leetcode password. you can also pass it as an environment variable LEETCODE_PASSWORD",
)
arg_parser.add_argument(
    "--session",
    type=str,
    help="Leetcode session. you can also pass it as an environment variable LEETCODE_SESSION."
    " If you pass this, username and password will be ignored",
)
arg_parser.add_argument(
    "--no-input",
    action="store_true",
    help="If set, no input will be asked",
)
args = arg_parser.parse_args()
NO_INPUT = args.no_input or env_config.NO_INPUT
LEETCODE_USERNAME = args.username or env_config.LEETCODE_USERNAME
LEETCODE_PASSWORD = args.password or env_config.LEETCODE_PASSWORD
LEETCODE_SESSION = args.session or env_config.LEETCODE_SESSION

if not NO_INPUT:
    logger.debug("NO_INPUT is not set. Asking for input")
    if not LEETCODE_SESSION:
        # TODO: implement a way to login with username and password.
        # please use the function api.login(username, password) to login
        session = input(
            "Enter your leetcode session. (enter n to login with username and password): "
        )
        if session.lower() != "n":
            env_config.LEETCODE_SESSION = session
        else:
            if not LEETCODE_USERNAME:
                logger.debug("LEETCODE_USERNAME is not set. Asking for input")
                env_config.LEETCODE_USERNAME = input("Enter your leetcode username: ")
            else:
                logger.debug("LEETCODE_USERNAME is set. Ignoring input")
            if not LEETCODE_PASSWORD:
                logger.debug("LEETCODE_PASSWORD is not set. Asking for input")
                env_config.LEETCODE_PASSWORD = input("Enter your leetcode password: ")
            else:
                logger.debug("LEETCODE_PASSWORD is set. Ignoring input")

        env_config.LEETCODE_SESSION = login(
            env_config.LEETCODE_USERNAME, env_config.LEETCODE_PASSWORD
        )
    else:
        logger.debug("LEETCODE_SESSION is set. Ignoring username and password")
else:
    logger.debug("NO_INPUT is set. Ignoring username and password")
    if not LEETCODE_SESSION and not (LEETCODE_USERNAME and LEETCODE_PASSWORD):
        logger.error(
            "You must set LEETCODE_SESSION or LEETCODE_USERNAME and LEETCODE_PASSWORD"
        )
        exit(1)


def start_action():
    env_config.logger.info("Starting action")
    questions_table = []
    get_user()
    # Generate a Question README.md file for each question
    # plus the solution code file
    for subs in get_all_submissions():
        solution = get_solution(subs["id"])
        questions_table.append(generate_solution(solution))
        env_config.logger.info('Generated solution for question "%s"', subs["title"])

    env_config.logger.info("Generated solutions for all questions")

    # Generate a README.md file for the user
    env_config.logger.info("Generating README.md file for the user")
    generate_readme(get_user(), questions_table)
    env_config.logger.info("Generated README.md file for the user")
    return


if __name__ == "__main__":
    start_action()
