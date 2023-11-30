import requests
import json

url = requests.get("https://opentdb.com/api.php?amount=20&category=15&difficulty=medium&type=boolean")
text = url.text

quiz_api_data = json.loads(text)

question_data = quiz_api_data["results"]

# question data = [{
# 'category': 'Entertainment: Video Games',
# 'type': 'boolean',
# 'difficulty': 'medium',
# 'question': 'DragonForce&#039;s &#039;Through the Fire and Flames&#039; is widely considered to be
# the hardest song in the Guitar Hero series.',
# 'correct_answer': 'True',
# 'incorrect_answers': ['False']
# }, {}...]
