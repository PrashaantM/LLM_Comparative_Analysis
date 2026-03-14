# LLM_Comparative_Analysis

Set up and installation:

Python:

Once installed, check with python3 --version in the terminal.




Django:

pip install django
pip install pillow (useful when used for images)
python -m django --version

- creating django project
django-admin startproject config .

- Creating main app
python3 manage.py startapp portfolio

- running migration
python manage.py migrate

- running server
python3 manage.py runserver

- saving all the dependencies to requirements.txt
pip freeze > requirements.txt

- deactivating venv
deactivate


Creating folders: mkdir folder_name
changing directory: cd folder_name
back to start directory: cd
list of directories: ls




Useful git commands:

- creating a virtual environment
- activating the virtual environment
python3 -m venv venv
source venv/bin/activate

- creates a branch named branch_name
git checkout -b branch_name 

- tells you what branch you are on
git branch

- deletes branch_name
git -D branch_name

- "resource management -remove file file_name"
rm -rf file_name

- staging changes and pushing them to branch_name
git add .
git push branch_name

- pulling code from branch_name
git pull branch_name

- temporarily stores staged and unstaged commits and reverts branch to HEAD (the position it was at the last commit on the time line)
git stash
