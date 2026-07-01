import json

# AI related skills needed
required_skills = [
    "NLP",
    "Fine-tuning LLMs",
    "LoRA",
    "Milvus",
    "AWS",
    "Python"
]

candidates = []

# Read file
with open("candidates.jsonl", "r", encoding="utf-8") as file:
    for line in file:
        candidate = json.loads(line)

        score = 0

        # Experience score (5-9 years preferred)
        exp = candidate["profile"]["years_of_experience"]
        if 5 <= exp <= 9:
            score += 30

        # Skills score
        candidate_skills = [skill["name"] for skill in candidate["skills"]]

        matched_skills = 0
        for skill in required_skills:
            if skill in candidate_skills:
                matched_skills += 1

        score += matched_skills * 10

        # GitHub activity score
        github = candidate["redrob_signals"]["github_activity_score"]
        score += github

        # Recruiter response rate
        response = candidate["redrob_signals"]["recruiter_response_rate"]
        score += response * 20

        candidates.append({
            "candidate_id": candidate["candidate_id"],
            "score": round(score, 2)
            })


# Sort by score
candidates.sort(key=lambda x: (-x["score"], x["candidate_id"]))

# Debug check for tie rows
print("Checking rank 18-19")
for i in range(17, 19):
    print(candidates[i])

print("Checking rank 93-94")
for i in range(92, 94):
    print(candidates[i])

# Print top 10
for i in range(10):
    print(i+1, candidates[i])

import csv

# Save top 100 candidates
with open("submission.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    # Header
    writer.writerow(["candidate_id", "rank", "score", "reasoning"])

    # Top 100
    for i in range(100):
        writer.writerow([
            candidates[i]["candidate_id"],
            i + 1,
            candidates[i]["score"],
            "Matched AI skills, experience, github activity and recruiter response."
            ])
print("submission.csv created successfully!")
