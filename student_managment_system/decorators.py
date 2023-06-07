from django.shortcuts import redirect

def administrator_required(function):
    def wrap(*args, **kwargs):
        if args[0].user.uloga.name == "administrator":
            return function(*args, **kwargs)
        else:
            return redirect('home')
    return wrap

def profesor_required(function):
    def wrap(*args, **kwargs):
        if args[0].user.uloga.name == "profesor":
            return function(*args, **kwargs)
        else:
            return redirect('home')
    return wrap

def student_required(function):
    def wrap(*args, **kwargs):
        if args[0].user.uloga.name == "student":
            return function(*args, **kwargs)
        else:
            return redirect('home')
    return wrap

def administrator_or_profesor_required(function):
    def wrap(*args, **kwargs):
        if args[0].user.uloga.name == "administrator" or args[0].user.uloga.name == "profesor":
            return function(*args, **kwargs)
        else:
            return redirect('home')
    return wrap