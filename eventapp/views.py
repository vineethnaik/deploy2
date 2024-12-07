from django.shortcuts import render, redirect
from .models import Event  # Import the Event model
from .forms import BookingForm, FeedbackForm, MessageForm  # Import forms in a single line


# Create your views here.

def index(request):
    """Render the homepage."""
    return render(request, 'index.html')

def bookingsuccess(request):
    """Render the homepage."""
    return render(request, 'booking success.html')


def about(request):
    """Render the about page."""
    return render(request, 'about.html')


def events(request):
    """Render the events page with a list of events."""
    dict_eve = {
        'eve': Event.objects.all()  # Fetch all events from the database
    }
    return render(request, 'events.html', dict_eve)


def booking(request):
    """Handle event booking."""
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bookingsuccess')  # Redirect to the homepage after successful booking

    # Display the empty booking form
    form = BookingForm()
    dict_form = {
        'form': form
    }
    return render(request, 'booking.html', dict_form)


from django.shortcuts import render, redirect
def feedback_view(request):
    """Handle feedback form submissions."""
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feedback_success')  # Redirect to feedback success page
    else:
        form = FeedbackForm()

    return render(request, 'feedback.html', {'form': form})


from django.shortcuts import render, redirect
from django.contrib import messages

# Contact form view
from django.shortcuts import render, redirect
from django.urls import reverse
def contact_view(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            # Process the form (e.g., send an email, save to database, etc.)
            return redirect(reverse('Message_success'))
    else:
        form = MessageForm()
    return render(request, 'contact.html', {'form': form})


# Success page view
from django.shortcuts import render, redirect
from django.contrib import messages

def submit_feedback(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        feedback = request.POST.get("feedback")
        rating = request.POST.get("rating")

        # You can save the data to the database here if needed
        # For now, we just display a success message
        messages.success(request, "Your feedback was successfully saved!")

        # Redirect back to the feedback form
        return redirect('success')  # Replace 'feedback' with your form's URL name

    return render(request, 'feedback.html')  # Update with the correct template path
def success_view(request):
    return render(request, 'success.html')

def Messagesuccess_view(request):
    return render(request, 'messagesuccess.html')

def event1_description(request):
    return render(request, 'event1_description.html')
def event2_description(request):
    return render(request, 'event2_description.html')
def event3_description(request):
    return render(request, 'event3_description.html')
def event4_description(request):
    return render(request, 'event4_description.html')
def event5_description(request):
    return render(request, 'event55_description.html')
from django.http import HttpResponse

def chatbot(request):
    return render(request, "chatbot.html")

