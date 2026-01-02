from django import forms

class EmailForm(forms.Form):
    message_content = forms.CharField(
        widget=forms.Textarea(attrs={
            "placeholder": "Paste the email content here..."
        })
    )
