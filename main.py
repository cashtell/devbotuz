import os
import random
from datetime import datetime, timedelta

percent = 30  # Процент дней, которые будут задействованы
total_days = 150  # Общее количество дней

# Задайте диапазон для commit_frequency (минимальное и максимальное количество коммитов в день)
min_commit_frequency = 2
max_commit_frequency = 5

repo_link = "https://github.com/cashtell/devbotuz.git"

now = datetime.now()

f = open("commit.txt", "w")
os.system("git config user.name")
os.system("git config user.email")
os.system("git init")

for day in range(1, total_days + 1):
    if random.randint(1, 100) <= percent:  # Генерируем случайное число и сравниваем с процентом
        commit_frequency = random.randint(min_commit_frequency, max_commit_frequency)  # Случайное количество коммитов
        for _ in range(commit_frequency):
            f = open("commit.txt", "a+")
            l_date = now - timedelta(days=day)
            formatdate = l_date.strftime("%Y-%m-%d")
            f.write(f"commit ke {day}: {formatdate}\n")
            f.close()
            os.system("git add .")
            os.system(f"git commit --date=\"{formatdate} 12:15:10\" -m \"commit ke {day}\"")
            print(f"commit ke {day}: {formatdate}, commits: {commit_frequency}")

os.system(f"git remote add origin {repo_link}")
os.system("git branch -M main")
os.system("git push -u origin main -f")
os.rmdir('.git')
os.remove('commit.txt')

