from mailbox import Message

from django import forms
from . models import Booking,Feedback
class DateInput(forms.DateInput):
    input_type='date'


class BookingForm(forms.ModelForm):
    class Meta:
        model=Booking
        fields='__all__'

        widgets={
            'booking_date':DateInput(),
        }

        labels={
            'cus_name':"Customer Name:",
            'cus_ph':"Customer Phone:",
            'name':"Event Name:",
            'booking_date':"Booking Date:",
        }
class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'feedback']

from django import forms
from .models import Message

class MessageForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'id_name'}),
        label="Your Name"
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'id': 'id_email'}),
        label="Your Email"
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'id_message'}),
        label="Your Message"
    )

