
from django.shortcuts import render,redirect
import pyttsx3
from .models import UserData, University
from .forms import UserDataForm
from .forms import UniversityData

# Create your views here.
def adminpanel(request):
    return render(request, "admin_panel.html")

# def add_uni(request):
#     return render(request, "add_uni.html")

def home(request):
    return render(request, "index.html")

def forms(request):
    return render(request, 'forms.html')

def list(request):
    return render(request, 'list.html')


def uni_shortlist(request):
    if request.method == "POST":
        country = request.POST.get("country")
        course = request.POST.get("course")
        intake = request.POST.get("intake")
        level = request.POST.get("level")
        lang_test = request.POST.get("lang_test")

        # Convert input values to float
        test_score = float(request.POST.get("test_score"))
        marks_10th = float(request.POST.get("marks_10th"))
        marks_12th = float(request.POST.get("marks_12th"))
        CGPA = float(request.POST.get("CGPA"))

        # Save user data to the UserData model
        user_data = UserData(
            country=country,
            course=course,
            intake=intake,
            level=level,
            lang_test=lang_test,
            test_score=test_score,
            marks_10th=marks_10th,
            marks_12th=marks_12th,
            CGPA=CGPA
        )
        user_data.save()  # Save to the database

        # Calculate the aggregate percentage of 10th and 12th marks
        aggregate_marks = (marks_10th + marks_12th) / 2

        # Filter universities based on criteria
        shortlisted_uni = University.objects.filter(
            country=country,
            course=course,
            intake=intake,
            level=level,
            accepted_lt=lang_test,
            lt_score__lte=test_score,  # User's score must be >= required
            min_marks__lte=aggregate_marks,  # User's marks must be >= required
            min_CGPA__lte=CGPA  # User's CGPA must be >= required
        )

        return render(request, "list.html", {"universities": shortlisted_uni})

    return render(request, "list.html")



def table(request):
    return render(request, 'table.html')



def add_university(request):
    if request.method == "POST":
        form = UniversityData(request.POST)
        if form.is_valid():
            form.save()  # Save the data to the database
            return redirect('add_university')  # Redirect to the admin panel after submission
        else:
            print(form.errors)
    else:
        form = UniversityData()

    return render(request, "add_uni.html", {"form": form})
