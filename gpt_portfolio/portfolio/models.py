from django.db import models

# Model representing the portfolio owner's profile
class Profile(models.Model):

    # String field for the person's full name
    # Example: "Muhammad Mustafa"
    
    # Short text field for professional title
    # Example: "Computer Science Student" or "Software Developer"

    # Text field for longer biography/about section
    # Will appear on the homepage "About Me"

    # ImageField for profile picture
    # Requires Pillow to process uploaded images
    # Upload path should be something like "profile_images/"

    # Email contact field
    # Used in contact section

    # Optional GitHub link
    # URLField for linking to GitHub profile

    # Optional LinkedIn link
    # URLField for linking to LinkedIn profile

    # Method returning the profile name as string
    # Used in Django admin and debugging

    pass


# Model representing projects displayed on the portfolio
class Project(models.Model):

    # Title of the project
    # Example: "AI Chatbot" or "Portfolio Website"

    # Short description of the project
    # Appears in project cards

    # Detailed description field
    # Longer explanation shown on project page

    # ImageField for project screenshot
    # Uploaded images stored in "project_images/"

    # URLField linking to the project repository
    # Example: GitHub link

    # Optional URLField for live demo

    # DateField for project completion date

    # BooleanField to mark whether project is featured
    # Featured projects appear on homepage

    # Method returning project title as string
    # Used in admin panel display

    pass


# Model representing skills
class Skill(models.Model):

    # Name of skill
    # Example: "Python", "Django", "React"

    # IntegerField representing proficiency level
    # Could be used for progress bars (0-100)

    # Optional description explaining experience with the skill

    # Method returning skill name as string

    pass