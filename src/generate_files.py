import os
from string import Template
from datetime import datetime

from config import env_config
from schema import User, Solution
from api import get_user


def create_profile_dir():
    """
    Create a profile directory if it does not exist

    Returns:
        str: fully qualified path of the directory created
    """
    dir_name = env_config.LEETCODE_USERNAME
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
        env_config.logger.debug(f"Created directory {dir_name}")
    else:
        env_config.logger.debug(f"Directory {dir_name} already exists")

    return os.path.abspath(dir_name)


def create_solution_dir(solution: Solution):
    profile_dir = create_profile_dir()
    solution_dir = os.path.join(
        profile_dir, 'solutions', solution.question.title_slug)
    if not os.path.exists(solution_dir):
        os.makedirs(solution_dir)
        env_config.logger.debug(f"Created directory {solution_dir}")
    else:
        env_config.logger.debug(f"Directory {solution_dir} already exists")

    return solution_dir


def generate_readme(user: User = None, questions_table: list = []):
    """Create a README.md file for the user

    Args:
        user (User): User object

    Returns:
        str: fully qualified path of the README.md file created
    """
    with open(env_config.README_TMLT, "r") as f:
        readme_tmlt = Template(f.read())

    if not user:
        user = get_user()

    subs = {
        "name": user.name,
        "about_me": user.about_me,
        "avatar": user.avatar,
        "job_title": user.job_title,
        "company": user.company,
        'country': user.country,
        'leetcode_rank': user.leetcode_rank,
        "username": env_config.LEETCODE_USERNAME,
        "linkedin_url": user.linkedin_url,
        "twitter_url": user.twitter_url,
        "github_url": user.github_url,
    }

    # Add languages
    languages = []
    for language in user.languages:
        languages.append(
            env_config.LANGUAGE_TMLT.format(
                language=language.language, language_count=language.solved_count
            )
        )
    subs["languages"] = "\n".join(languages)

    # add problem stats
    problems = {
        'easy': {},
        'medium': {},
        'hard': {},
        'total': {},
    }

    for stat in user.question_stats:
        difficulty = stat.difficulty.lower()
        percent = stat.percentage
        if percent:
            percent = f'{percent:.2f}%'
        if stat.difficulty.lower() != 'all':
            problems[difficulty] = {
                f'{difficulty}_total': stat.total_count,
                f'{difficulty}_solved': stat.solved_count,
                f'{difficulty}_percentile': percent,
            }
        else:
            problems['total'] = {
                'total': stat.total_count,
                'total_solved': stat.solved_count,
                'total_percentile': percent,
            }
    
    for stat in problems:
        env_config.logger.debug(f"Problems: {stat} {problems[stat]}")
        subs.update(problems[stat])

    # generate website links
    websites = []
    for site in user.website_url:
        websites.append(env_config.WEBSITES_TMLT.format(website=site))

    # question table
    q_tables = []
    for q in questions_table:
        q_tables.append(env_config.PROBLEM_TMPT.format(
            title=q['title'],
            problem_url=f'https://leetcode.com/problems/{q["title_slug"]}',
            language=q['language'],
            solution_link=q['file_link'],
            difficulty=q['difficulty'],
            run_beats=q['runtime_beats'],
            memory_beats=q['memory_beats'],
        ))

    subs['question_tables'] = "\n".join(q_tables)
    subs['websites'] = "\n".join(websites)
    rendered = readme_tmlt.safe_substitute(subs)
    readme_path = os.path.join(create_profile_dir(), "README.md")
    with open(readme_path, "w") as f:
        f.write(rendered)
    env_config.logger.debug(f"Created README.md at {readme_path}")
    return readme_path


def generate_solution(solution: Solution) -> dict:
    """
    Generate a solution, question read me file for the question solved by the user

    each question will have it's own folder inside that solution and question read me file will be created
    """
    with open(env_config.QUESTION_TMLT, "r") as f:
        QUESTION_TEMPLATE = Template(f.read())

    solution_dir = create_solution_dir(solution)

    # timestamp is in unix format so convert it to human readable format
    human_readable_date = datetime.fromtimestamp(
        solution.timestamp).strftime('%d %B %Y')

    file_name = solution.question.title_slug + '.' + \
        env_config.FILE_MAPPING[solution.language]['ext']
    subs = {
        'title': solution.question.title,
        'description': solution.question.content,
        'slug': solution.question.title_slug,
        'runtime': solution.runtime,
        'runtime_beats': f'{solution.runtime_percentile}%',
        'memory': solution.memory,
        'memory_beats': f'{solution.memory_percentile}%',
        'timestamp': human_readable_date,
        'file_name': file_name,
        'language': env_config.FILE_MAPPING[solution.language]['md'],
        'code': solution.code,
    }

    # subtitle the template with the values
    rendered = QUESTION_TEMPLATE.substitute(subs)

    # create a file with the question title as the file name
    file_path = os.path.join(solution_dir, 'README.md')

    with open(file_path, 'w') as f:
        f.write(rendered)

    # write the code to the file
    file_path = os.path.join(solution_dir, file_name)
    with open(file_path, 'w') as f:
        f.write(solution.code)

    env_config.logger.debug(f"Created {file_path}")

    return {
        'title': solution.question.title,
        'title_slug': solution.question.title_slug,
        'file_path': file_path,
        'file_link': f'solutions/{solution.question.title_slug}/README.md',
        'language': solution.language,
        'runtime_beats': solution.runtime_percentile,
        'memory_beats': solution.memory_percentile,
        'difficulty': solution.question.difficulty,
    }
