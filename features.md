# Leetcode profiler features

## Features

- Fetch all correct submissions for a problem
    - question title
    - question content
        - description
        - test cases
    - solution code
    - language
    - test case number
    - runtime(ms)
        - runtime
        - beats
    - memory usage(MB)
        - memory
        - beats
    - timestamp
- Format the question using markdown
- Put the solution in its own file
- Generate a table of contents
- Generate a README.md

## Folder structure

```
README.md (table of contents)
solutions/
    1-two-sum/
        README.md(question with markdown and solution details)
        solution.py
    2-add-two-numbers/
        README.md
        solution.cpp
    ...
```

## Root README.md content

- User details
    - Name(realName)
    - userAvatar
    - User country
    - Leetcode Ranks
    - Leetcode profile link
    - githubUrl(if provided)
    - twitterUrl(if provided)
    - linkedinUrl(if provided)
    - websites(if provided) (can be multiple)
- Language Stat
    - language
    - problems solved
- Problem Solved
    - Difficulty
        - Total 
        - Solved
        - beats(percent)
        - Title
- Problem Table
    - Question title(sorted by title)
    - Link to solution
    - Difficulty tag

## Solution README.md content

- Question title
- Question content
    - description
    - test cases
- Solution Stats
    - language
    - test case number
    - runtime(ms)
        - runtime
        - beats
    - memory usage(MB)
        - memory
        - beats
    - timestamp
- Solution code Link

