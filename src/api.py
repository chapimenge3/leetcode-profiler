from typing import List
from config import env_config
from schema import User, QuestionStats, LanguageStats, Question, Solution

import httpx


def login(
    username: str = env_config.LEETCODE_USERNAME,
    password: str = env_config.LEETCODE_PASSWORD,
) -> str:
    """Login to leetcode and get the session

    Args:
        username (str, optional): user username. Defaults to env_config.LEETCODE_USERNAME.
        password (str, optional): user password. Defaults to env_config.LEETCODE_PASSWORD.

    Returns:
        str: leetcode session from cookie
    """
    # to be implemented
    raise NotImplementedError


# User profile related functions


def get_language_stats(
    username: str = env_config.LEETCODE_USERNAME
) -> List[LanguageStats]:
    """Get the language stats of the user

    Args:
        username (str, optional): Leetcode username. Defaults to env_config.LEETCODE_USERNAME.

    Returns:
        List[LanguageStats]: List of language stats
    """
    data = {
        "operationName": "languageStats",
        "query": "\n    query languageStats($username: String!) {\n  matchedUser(username: $username) {\n    languageProblemCount {\n      languageName\n      problemsSolved\n    }\n  }\n}\n    ",
        "variables": {"username": username},
    }
    response = httpx.post(
        env_config.graphql_url, headers=env_config.get_headers(), json=data
    )
    if response.status_code != 200:
        env_config.logger.error("Error getting user language stats")
        raise Exception("Error getting user language stats")
    resp_json = response.json()["data"]["matchedUser"]["languageProblemCount"]
    languages = []
    for language in resp_json:
        languages.append(
            LanguageStats(
                language=language["languageName"],
                solved_count=language["problemsSolved"],
            )
        )

    return languages


def get_question_stats(
    username: str = env_config.LEETCODE_USERNAME
) -> List[QuestionStats]:
    """Get the question stats of the user (total count, solved count, percentage)

    Args:
        username (str, optional): Leetcode username. Defaults to env_config.LEETCODE_USERNAME.

    Returns:
        List[QuestionStats]: List of question stats
    """
    data = {
        "operationName": "userProblemsSolved",
        "query": "\n    query userProblemsSolved($username: String!) {\n  allQuestionsCount {\n    difficulty\n    count\n  }\n  matchedUser(username: $username) {\n    problemsSolvedBeatsStats {\n      difficulty\n      percentage\n    }\n    submitStatsGlobal {\n      acSubmissionNum {\n        difficulty\n        count\n      }\n    }\n  }\n}\n    ",
        "variables": {"username": username},
    }
    response = httpx.post(
        env_config.graphql_url, headers=env_config.get_headers(), json=data
    )
    resp_json = response.json()["data"]
    questions_stat_dict = {}
    for question in resp_json["allQuestionsCount"]:
        questions_stat_dict[question["difficulty"]] = {
            "total_count": question["count"],
            "solved_count": 0,
            "percentage": None,
        }
    for question in resp_json["matchedUser"]["submitStatsGlobal"]["acSubmissionNum"]:
        try:
            questions_stat_dict[question["difficulty"]]["solved_count"] = question[
                "count"
            ]
        except KeyError:
            pass
    for question in resp_json["matchedUser"]["problemsSolvedBeatsStats"]:
        try:
            questions_stat_dict[question["difficulty"]]["percentage"] = question[
                "percentage"
            ]
        except KeyError:
            pass

    questions_stat = []

    for stat in questions_stat_dict:
        q_stat = questions_stat_dict[stat]
        questions_stat.append(
            QuestionStats(
                difficulty=stat,
                total_count=q_stat.get("total_count"),
                solved_count=q_stat.get("solved_count"),
                percentage=q_stat.get("percentage")
                or q_stat.get("solved_count") / q_stat.get("total_count") * 100,
            )
        )

    return questions_stat


def get_user() -> User:
    """
    Get user public profile from leetcode

    Returns:
        User: User public profile
    """
    # get username
    if getattr(env_config, "USER", None):
        return env_config.USER
    data = {
        "operationName": "globalData",
        "query": "\n    query globalData {\n  userStatus {\n    userId\n    isSignedIn\n    isMockUser\n    isPremium\n    isVerified\n    username\n    avatar\n    isAdmin\n    isSuperuser\n    permissions\n    isTranslator\n    activeSessionId\n    checkedInToday\n    notificationStatus {\n      lastModified\n      numUnread\n    }\n  }\n}\n    ",
        "variables": {},
    }
    response = httpx.post(
        env_config.graphql_url, headers=env_config.get_headers(), json=data
    )
    if response.status_code != 200:
        env_config.logger.error("Error getting username")
        raise Exception("Error getting username")
    resp_json = response.json()
    user_data = {
        "username": resp_json["data"]["userStatus"]["username"],
        "avatar": resp_json["data"]["userStatus"]["avatar"],
    }
    env_config.LEETCODE_USERNAME = user_data["username"]
    # get user public profile
    data = {
        "operationName": "userPublicProfile",
        "query": "\n    query userPublicProfile($username: String!) {\n  matchedUser(username: $username) {\n    contestBadge {\n      name\n      expired\n      hoverText\n      icon\n    }\n    username\n    githubUrl\n    twitterUrl\n    linkedinUrl\n    profile {\n      ranking\n      userAvatar\n      realName\n      aboutMe\n      school\n      websites\n      countryName\n      company\n      jobTitle\n      skillTags\n      postViewCount\n      postViewCountDiff\n      reputation\n      reputationDiff\n      solutionCount\n      solutionCountDiff\n      categoryDiscussCount\n      categoryDiscussCountDiff\n    }\n  }\n}\n    ",
        "variables": {"username": user_data["username"]},
    }
    response = httpx.post(
        env_config.graphql_url, headers=env_config.get_headers(), json=data
    )
    if response.status_code != 200:
        env_config.logger.error("Error getting user public profile")
        raise Exception("Error getting user public profile")
    resp_json = response.json()["data"]["matchedUser"]
    env_config.logger.debug(f"Got user public profile {resp_json}")
    profile = resp_json["profile"]
    user_data["github_url"] = resp_json.get("githubUrl")
    user_data["twitter_url"] = resp_json.get("twitterUrl")
    user_data["linkedin_url"] = resp_json.get("linkedinUrl")
    user_data["website_url"] = profile.get("websites")
    user_data[
        "leetcode_profile_url"
    ] = f"{env_config.LEETCODE_URL}/{user_data['username']}"
    user_data["leetcode_rank"] = profile.get("ranking")
    user_data["name"] = profile.get("realName")
    user_data["job_title"] = profile.get("jobTitle")
    user_data["company"] = profile.get("company")
    user_data["country"] = profile.get("countryName")
    user_data["about_me"] = profile.get("aboutMe")

    user_data["languages"] = get_language_stats(user_data["username"])
    user_data["question_stats"] = get_question_stats(user_data["username"])
    env_config.logger.debug(f"Got user data {user_data}")
    env_config.LEETCODE_USERNAME = user_data["username"]
    env_config.USER = User(**user_data)
    return env_config.USER


# Submission Related function


def get_question(question_slug: str) -> Question:
    """Get Question details from leetcode

    Args:
        question_slug (str): question slug

    Returns:
        Question: Question details
    """
    data = {
        "operationName": "questionTitle",
        "query": "\n    query questionTitle($titleSlug: String!) {\n  question(titleSlug: $titleSlug) {\n    questionId\n    questionFrontendId\n    title\n    titleSlug\n    isPaidOnly\n    difficulty\n    likes\n    dislikes\n    categoryTitle\n  }\n}\n    ",
        "variables": {"titleSlug": question_slug},
    }
    response = httpx.post(
        env_config.graphql_url, headers=env_config.get_headers(), json=data
    )
    if response.status_code != 200:
        env_config.logger.error("Error getting question details")
        raise Exception("Error getting question details")
    resp_json = response.json()["data"]["question"]
    env_config.logger.debug(f"Got question title details {resp_json}")
    q = {
        "question_id": resp_json["questionId"],
        "title_slug": resp_json["titleSlug"],
        "title": resp_json["title"],
        "difficulty": resp_json["difficulty"],
        "likes": resp_json["likes"],
        "dislikes": resp_json["dislikes"],
        "category": resp_json["categoryTitle"],
    }
    data = {
        "operationName": "questionContent",
        "query": "\n    query questionContent($titleSlug: String!) {\n  question(titleSlug: $titleSlug) {\n    content\n    mysqlSchemas\n    dataSchemas\n  }\n}\n    ",
        "variables": {"titleSlug": question_slug},
    }
    response = httpx.post(
        env_config.graphql_url,
        headers=env_config.get_headers(),
        json=data,
    )
    if response.status_code != 200:
        env_config.logger.error("Error getting question details")
        raise Exception("Error getting question details")
    resp_json = response.json()["data"]["question"]
    env_config.logger.debug(f"Got question content details {resp_json}")
    q["content"] = resp_json["content"]

    return Question(**q)


def get_solution(submission_id: str) -> Solution:
    """Get the submission details

    Args:
        submission_id (str): submission id

    Returns:
        dict: submission details
    """
    data = {
        "operationName": "submissionDetails",
        "query": "\n    query submissionDetails($submissionId: Int!) {\n  submissionDetails(submissionId: $submissionId) {\n    runtime\n    runtimeDisplay\n    runtimePercentile\n    runtimeDistribution\n    memory\n    memoryDisplay\n    memoryPercentile\n    memoryDistribution\n    code\n    timestamp\n    statusCode\n    user {\n      username\n      profile {\n        realName\n        userAvatar\n      }\n    }\n    lang {\n      name\n      verboseName\n    }\n    question {\n      questionId\n      titleSlug\n      hasFrontendPreview\n    }\n    notes\n    flagType\n    topicTags {\n      tagId\n      slug\n      name\n    }\n    runtimeError\n    compileError\n    lastTestcase\n    totalCorrect\n    totalTestcases\n    fullCodeOutput\n    testDescriptions\n    testBodies\n    testInfo\n  }\n}\n    ",
        "variables": {"submissionId": submission_id},
    }
    response = httpx.post(
        env_config.graphql_url, headers=env_config.get_headers(), json=data
    )
    if response.status_code != 200:
        env_config.logger.error("Error getting submission details")
        raise Exception("Error getting submission details")
    resp_json = response.json()["data"]["submissionDetails"]
    env_config.logger.debug(f"Got submission details {resp_json}")
    sol = {
        "runtime": resp_json["runtimeDisplay"],
        "runtime_percentile": round(int(resp_json["runtimePercentile"] or 0), 2),
        "memory": resp_json["memoryDisplay"],
        "memory_percentile": round(int(resp_json["memoryPercentile"] or 0), 2),
        "code": resp_json["code"],
        "language": resp_json["lang"]["verboseName"],
        "timestamp": resp_json["timestamp"],
    }
    q_slug = resp_json["question"]["titleSlug"]
    question = get_question(q_slug)
    sol["question"] = question
    return Solution(**sol)


def get_all_submissions():
    """Get all submissions of the user. It is a generator function so that it
    can be used in a for loop.

    Status 10 means Accepted and 11 means Wrong Answer

    Raises:
        Exception: Error getting submissions

    Yields:
        dict: submission details

        sample response:
        {
            "id": 1102082701,
            "lang": "python3",
            "lang_name": "Python3",
            "time": "23 hours, 33 minutes",
            "timestamp": 1700398715,
            "status": 11,
            "status_display": "Wrong Answer",
            "runtime": "N/A",
            "url": "/submissions/detail/1102082701/",
            "is_pending": "Not Pending",
            "title": "Reduction Operations to Make the Array Elements Equal",
            "memory": "N/A",
            "code": "....",
            "compare_result": "11110010000001000.....",
            "title_slug": "reduction-operations-to-make-the-array-elements-equal",
            "has_notes": false,
            "flag_type": 1
        }
    """
    url = f"{env_config.LEETCODE_URL}/api/submissions/"
    query = {
        "offset": "0",
        "limit": "100",
        "lastkey": "",
    }
    has_next = True
    while has_next:
        response = httpx.get(url, params=query, headers=env_config.get_headers())
        if response.status_code != 200:
            env_config.logger.error("Error getting submissions")
            raise Exception("Error getting submissions")
        resp_json = response.json()
        has_next = resp_json["has_next"]
        last_key = resp_json["last_key"]
        query["lastkey"] = last_key
        query["offset"] = int(query["offset"]) + 100
        for submission in resp_json["submissions_dump"]:
            env_config.logger.debug(f"Yielding submission {submission['id']}")
            if submission["status"] == 10:
                yield submission
