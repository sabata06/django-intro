from django.http import HttpResponse


def student(request):
    return HttpResponse(
        """
        <h2>
            welcome to student
        </h2>

"""
    )


def goodbye(request):
    return HttpResponse(
        """
        <h2>
           goodbye
        </h2>

"""
    )
