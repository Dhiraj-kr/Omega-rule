prompt = f"""
You are given information in checkers delimited by triple backticks.
Checkers: ```{checkers}```
Your task is to tell which checkers are related to android.
"""
response = get_completion(prompt)
print(response)