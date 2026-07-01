# AI Candidate Ranking System

## Problem Statement
Build an AI-based candidate ranking system that matches candidates to a job description.

## Dataset
The dataset contains:
- Candidate profiles
- Skills
- Career history
- Education
- Redrob signals

## Approach
1. Read candidate data from `candidates.jsonl`
2. Extract:
   - Skills
   - Years of experience
   - GitHub activity score
   - Recruiter response rate
3. Calculate candidate score
4. Rank candidates based on score

## Scoring Formula
Total Score =
- Experience (5–9 years): +30
- Matched skills: +10 each
- GitHub activity: direct score
- Recruiter response rate: ×20

## Ranking Logic
Candidates are sorted by:
1. Higher score first
2. If scores are equal, lower candidate_id first

## Output
Generated top 100 ranked candidates in `submission.csv`

## Files
- `ranking.py` → Ranking logic
- `submission.csv` → Final output
