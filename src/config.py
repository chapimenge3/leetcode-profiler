import os
import logging

LEETCODE_SESSION = os.environ.get('LEETCODE_SESSION')
LEETCODE_USERNAME = os.environ.get('LEETCODE_USERNAME')
LEETCODE_PASSWORD = os.environ.get('LEETCODE_PASSWORD')
LOG_LEVEL = os.environ.get('LOG_LEVEL', 'DEBUG')
NO_INPUT = os.environ.get('NO_INPUT')

if LOG_LEVEL:
    LOG_LEVEL = LOG_LEVEL.upper()

logging.basicConfig(
    level=getattr(logging, LOG_LEVEL),
    format='%(asctime)s %(levelname)s %(message)s',
)
logger = logging.getLogger(__name__)
# logger.setLevel(getattr(logging, LOG_LEVEL))
if logger.hasHandlers() is False:
    logger.addHandler(logging.StreamHandler())

logger.debug("Log Level set to %s", LOG_LEVEL)

FILE_MAPPING = {
    "C++": {'ext': 'cpp', 'md': 'cpp'},
    "Java": {'ext': 'java', 'md': 'java'},
    "Python": {'ext': 'py', 'md': 'python'},
    "Python3": {'ext': 'py', 'md': 'python'},
    "MySQL": {'ext': 'sql', 'md': 'sql'},
    "MS SQL Server": {'ext': 'sql', 'md': 'sql'},
    "Oracle": {'ext': 'sql', 'md': 'sql'},
    "C": {'ext': 'c', 'md': 'c'},
    "C#": {'ext': 'cs', 'md': 'csharp'},
    "JavaScript": {'ext': 'js', 'md': 'javascript'},
    "TypeScript": {'ext': 'ts', 'md': 'typescript'},
    "Bash": {'ext': 'sh', 'md': 'bash'},
    "PHP": {'ext': 'php', 'md': 'php'},
    "Swift": {'ext': 'swift', 'md': 'swift'},
    "Kotlin": {'ext': 'kt', 'md': 'kotlin'},
    "Dart": {'ext': 'dart', 'md': 'dart'},
    "Go": {'ext': 'go', 'md': 'go'},
    "Ruby": {'ext': 'rb', 'md': 'ruby'},
    "Scala": {'ext': 'scala', 'md': 'scala'},
    "Rust": {'ext': 'rs', 'md': 'rust'},
    "Racket": {'ext': 'rkt', 'md': 'racket'},
    "Erlang": {'ext': 'erl', 'md': 'erlang'},
    "Elixir": {'ext': 'ex', 'md': 'elixir'},
    "Pandas": {'ext': 'py', 'md': 'python'},
    "React": {'ext': 'jsx', 'md': 'jsx'},
    "Vanilla JS": {'ext': 'js', 'md': 'javascript'},
    "PostgreSQL": {'ext': 'sql', 'md': 'sql'}
}


class Config:
    LEETCODE_SESSION = LEETCODE_SESSION
    LEETCODE_USERNAME = LEETCODE_USERNAME
    LEETCODE_PASSWORD = LEETCODE_PASSWORD
    NO_INPUT = NO_INPUT
    LEETCODE_URL = 'https://leetcode.com'

    # template values
    WEBSITES_TMLT = "[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)]({website})"
    LANGUAGE_TMLT = "- **{language}** - solved {language_count} problems"
    PROBLEM_TMPT = "| [{title}]({problem_url}) | [{language}](./{solution_link}) | {difficulty} | {run_beats} | {memory_beats} |"

    # logger
    logger = logger

    # graphql url
    graphql_url = f'{LEETCODE_URL}/graphql'
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    README_TMLT = os.path.join(BASE_DIR, 'templates', 'README.md')
    QUESTION_TMLT = os.path.join(BASE_DIR, 'templates', 'QUESTION.md')
    FILE_MAPPING = FILE_MAPPING

    def get_headers(self) -> dict:
        return {
            "Content-Type": "application/json",
            "Cookie": f"LEETCODE_SESSION={self.LEETCODE_SESSION}",
        }


env_config = Config()
env_config.logger.debug("Loaded config")
