from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_fun):
    def wrapper_func(request,*args,**kwargs):
          if request.user.is_authenticated:
            return redirect('home')
          else:   
            return view_fun(request,*args,**kwargs)
    return wrapper_func    


def allowed_users(allowed_rules=[]):
    def decorater(view_func):
        def wrapper_func(request,*args, **kwargs):

            group=None
            if request.user.groups.exists():
                group=request.user.groups.all()[0].name
            if group in allowed_rules:
                return view_func(request,*args, **kwargs)
            else:
                return HttpResponse('You are notauthorized')    
        return wrapper_func
    return decorater        

# def adminonly(view_func):
#         def wrapper_func(request,*args, **kwargs):

#             group=None
#             if request.user.groups.exists():
#                 group=request.user.groups.all()[0].name
#             if group == 'customer':
#                 return redirect('userpage')
#             if group == 'admin':
#                 return view_func(request,*args, **kwargs)
#         return wrapper_func