from dataclasses import dataclass
from typing import List, Optional


@dataclass
class LanguageStats:
    language: str
    solved_count: int


@dataclass
class QuestionStats:
    difficulty: str
    total_count: int
    solved_count: int
    percentage: Optional[float]


@dataclass
class User:
    name: str
    about_me: str
    username: str
    avatar: str
    job_title: str
    company: str
    country: str
    leetcode_rank: int
    github_url: Optional[str]
    twitter_url: Optional[str]
    linkedin_url: Optional[str]
    website_url: Optional[List[str]]
    languages: List[LanguageStats]
    question_stats: List[QuestionStats]
    leetcode_profile_url: str


@dataclass
class Question:
    question_id: str
    title_slug: str
    title: str
    content: str
    difficulty: str
    likes: int
    dislikes: int
    category: str


@dataclass
class Solution:
    runtime: str
    runtime_percentile: str
    memory: str
    memory_percentile: str
    code: str
    language: str
    timestamp: str
    question: Question
