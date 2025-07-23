import os
from collections import defaultdict
from tabulate import tabulate

folders = ["algorithm", "python", "didnt_know", "weekly_challenge"]
member_stats = defaultdict(lambda: defaultdict(int))

def get_members_in_folder(folder):
    path = os.path.join(".", folder)
    if folder == "weekly_challenge":
        for week in os.listdir(path):
            week_path = os.path.join(path, week)
            if os.path.isdir(week_path):
                for file in os.listdir(week_path):
                    name, _ = os.path.splitext(file)
                    member_stats[name][folder] += 1
    else:
        for member in os.listdir(path):
            member_path = os.path.join(path, member)
            if os.path.isdir(member_path):
                count = len([f for f in os.listdir(member_path) if f.endswith(".md")])
                member_stats[member][folder] += count

for folder in folders:
    get_members_in_folder(folder)

table = []
for member, counts in sorted(member_stats.items()):
    total = sum(counts.values())
    table.append([
        member,
        counts.get("algorithm", 0),
        counts.get("python", 0),
        counts.get("didnt_know", 0),
        counts.get("weekly_challenge", 0),
        total
    ])

header = ["이름", "algorithm", "python", "didnt_know", "weekly_challenge", "총합"]

os.makedirs("summary", exist_ok=True)
with open("summary/progress.md", "w", encoding="utf-8") as f:
    f.write("# 📊 팀원별 진행 현황\n\n")
    f.write(tabulate(table, headers=header, tablefmt="github"))
