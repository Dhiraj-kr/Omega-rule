prompt = f"""
You are given information in checkers delimited by triple backticks.
Checkers: ```{checkers}```
Your task is to map all the information with one or more
disa stig V5 rules.
"""
response = get_completion(prompt)
print(response)