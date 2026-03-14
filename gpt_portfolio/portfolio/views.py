from django.shortcuts import render

# View for homepage
def home(request):

    # Query database for profile information
    # Retrieve the first Profile object

    # Query for featured projects
    # Filter Project objects where featured=True

    # Query for skills
    # Retrieve all Skill objects

    # Create context dictionary
    # Pass profile, projects, and skills to template

    # Render homepage template
    # Template name likely "portfolio/home.html"

    pass


# View for projects page
def projects(request):

    # Query all Project objects

    # Create context dictionary containing project list

    # Render projects template
    # Template name likely "portfolio/projects.html"

    pass


# View for individual project detail
def project_detail(request, project_id):

    # Retrieve specific project using project_id

    # Handle case where project does not exist

    # Create context dictionary with project details

    # Render project detail template
    # Template name likely "portfolio/project_detail.html"

    pass


# View for about page
def about(request):

    # Retrieve Profile information

    # Retrieve skills

    # Pass information to template

    # Render about page template

    pass


# View for contact page
def contact(request):

    # If request method is POST
    #   Retrieve form data from request.POST
    #   Example: name, email, message

    # Validate form fields

    # Optionally save message to database
    # OR send email notification

    # Show success message after submission

    # If request method is GET
    #   Display empty contact form

    # Render contact page template

    pass