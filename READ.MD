1. Title
    # Calculator App
2. Description
   A simple command-line calculator built with Python that performs basic and advanced mathematical operations.
3. Features
   - Addition
   - Subtraction
   - Multiplication
   - Division (with zero handling)
   - Modulus (remainder)
   - Power (exponentiation)
   - Square Root
   - Percentage
   - Input validation
   - Error handling
4. How to Run
    1. Make sure Python is installed on your computer
   2. Download the file `calculate.py`
   3. Open terminal/command prompt
   4. Navigate to the folder containing the file
   5. Run: python calculate.py
5. Usage
   1. Choose an operation from the menu by typing a number
   2. Enter the numbers when prompted
   3. View the result
   4. Continue with another calculation or exit
6. Technologies
   - Python 3.x (for example 3.10.14 version)
   - math module (for square root)
7. Author
    - GitHub: ApsarShaik888
8. Screenshot
    ![img.png](img.png)
    ![img_1.png](img_1.png)
    ![img_2.png](img_2.png)
    ![img_3.png](img_3.png)
    ![img_4.png](img_4.png)
    ![img_5.png](img_5.png)
    ![img_6.png](img_6.png)
    ![img_7.png](img_7.png)
    ![img_8.png](img_8.png)
    ![img_9.png](img_9.png)
    ![img_10.png](img_10.png)


THANK YOU! HAPPY CODING
    
🚀 CI/CD Integration: GitHub + Harness Pipeline
This document outlines the step-by-step process to integrate a GitHub repository with Harness CI using Webhooks to automatically trigger pipelines on code push.

Prerequisites
A GitHub account and a repository containing your code (e.g., Python).
A Harness account (Free tier is sufficient).
A Harness Project and a working Pipeline (e.g., a Python Build Stage).

Step 1: Create a GitHub Personal Access Token (PAT)
Harness needs a secure way to communicate with GitHub.
Go to GitHub -> Settings -> Developer settings -> Personal access tokens (classic).
Click Generate new token.

Select the following required scopes:
repo (Full control of private repositories)
user (Read user profile data)
admin:repo_hook (Full control of repository hooks - crucial for webhooks)
Generate the token and copy it.

Step 2: Configure the Harness GitHub Connector
In Harness, go to Project Settings -> Connectors -> + New Connector -> GitHub.
URL: Enter your GitHub repo URL (e.g., https://github.com/Username/Calculator-App).
Authentication: Select Username and Token.
Username: Your GitHub username.
Token: Paste the PAT generated in Step 1 (store it as a Harness Secret).
API Access: Check Enable API access and select the same token. (This allows Harness to auto-create webhooks).
Click Test Connection and Save.

Step 3: Create the Harness Pipeline
Go to Pipelines -> Create Pipeline.
Add a Build Stage (e.g., running on Harness Cloud).
Configure the Codebase:
Connector: Select your GitHub connector.
Repository: Select your repo.
Add Execution Steps (e.g., a Run step):
Install dependencies: python3 -m pip install pytest-cov
Run code/tests: echo "9" | python3 calculate.py (or pytest).
Save and run the pipeline manually once to ensure it works.

Step 4: Create the Webhook Trigger in Harness
On your pipeline page, click the Triggers tab -> + New Trigger.
Name: Push-Trigger (or similar).
Event: Select Push.
Connector & Repo: Select your GitHub Connector and Repository.
Pipeline Input: Specify the branch (e.g., main) so the trigger knows which code to pull.
Save the Trigger.

Step 5: Verify the Webhook in GitHub
If Harness auto-registered the webhook:
Go to GitHub Repo -> Settings -> Webhooks.
You should see a webhook pointing to a Harness URL.
If Harness failed to auto-register (Manual Setup):
In Harness Triggers, copy the Webhook URL.
In GitHub, click Add webhook.
Payload URL: Paste the Harness URL.
Content type: application/json.
Which events: Select Just the push event.
Click Add webhook.
Step 6: Ensure Branch Names Match
Important: Ensure the branch you are pushing to matches the branch your Harness pipeline and trigger are configured for.
To change your local Git branch from master to main:
bash
git push origin master:main
git branch -m master main
git branch -u origin/main main
✅ How to Test It
Make a small change to your code (e.g., add a comment to calculate.py).
Commit and push to GitHub: git push origin main.

Go to Harness -> Executions.
You should see a new pipeline execution appear, triggered by the Webhook.
