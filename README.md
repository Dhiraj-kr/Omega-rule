# Omega-rule
setup.py contains pip command to install libraries.
This project uses openAI API keys to prompt chatgpt.
It uses chatgpt 3.5 model.

Chatgpt does not know about klocwork checkers. We are web scraping klocwork Java checkers docs and giving it to chatgpt.
Chatgpt have restriction on tokens limit which is 16k. So we have only send fraction of klocwork checkers which can be loaded to chatgpt within its token limit.

Chatgpt already knows about standards like DISA STIG, CWE, OWASP etc.

In this project, we are trying to find the mapping regarding which klocwork checkers are implementing rules of standards like DISA STIG, CWE, OWASP etc.

We use jupyter notebook to prompt chatgpt.
