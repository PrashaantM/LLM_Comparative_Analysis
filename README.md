# LLM_Comparative_Analysis

Set up and installation:

Python:

Once installed, check with python3 --version in the terminal.



Django:

pip install django
pip install pillow (useful when used for images)

django-admin startproject config .
- creating django project

python3 manage.py startapp portfolio
- Creating main app

- running server
python3 manage.py migrate
python3 manage.py runserver



Creating folders: mkdir folder_name
changing directory: cd folder_name



Useful git commands:

python3 -m venv venv
source venv/bin/activate
- creating a virtual environment
- activating the virtual environment

git checkout -b branch_name 
- creates a branch named branch_name

git branch
- tells you what branch you are on

git -D branch_name
- deletes branch_name

rm -rf file_name
- "resource management -remove file file_name"

git add .
git push branch_name
- staging changes and pushing them to branch_name

git pull branch_name
- pulling code from branch_name

git stash
- temporarily stores staged and unstaged commits and reverts branch to HEAD (the position it was at the last commit on the time line)
