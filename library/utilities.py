# Import necessary modules
import datetime
from django.utils import timezone
from .models import Fine, Book
from student.models import Student

def calcFine(issue):
    "Calculate fines of each issue if any"
    if issue.issued and not issue.returned and issue.return_date:
        today = timezone.now().date()
        lastdate = issue.return_date.date()
        
        if today > lastdate:
            diff = today - lastdate
            fine, created = Fine.objects.get_or_create(issue=issue, student=issue.student)
            if not fine.paid:
                fine.amount = diff.days * 10
                fine.save()
            else:
                print('Fine already paid')
        else:
            return 'No fine'
    else:
        return 'No fine'

def getmybooks(user):
    "Get issued books or requested books of a student, takes a user & returns a tuple"
    requestedbooks = []
    issuedbooks = []
    
    if user.is_authenticated:
        student = Student.objects.filter(student_id=user).first()
        if student:
            for b in Book.objects.all():
                for i in b.issue_set.all():
                    if i.student == student:
                        if i.issued:
                            issuedbooks.append(b)
                        else:
                            requestedbooks.append(b)
    
    return requestedbooks, issuedbooks
