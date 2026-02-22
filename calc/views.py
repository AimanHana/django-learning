from django.shortcuts import render
#from django.views.decorators.csrf import csrf_exempt
#from django.http import HttpResponse

# Create your views here.
def add(a,b):
    return a+b

#@csrf_exempt
def home(request):
    #return HttpResponse("Hello from calc!")
    #result_html = ""
    result = None
    
    if request.method == "POST":
        a = float(request.POST.get("a",0))
        b = float(request.POST.get("b",0))
        result = add(a, b)
        #result_html = f"<p><b>Result: </b> {add(a, b)}</p>"
    #html = f"""
    #<html>
     #   <body>
      #      <h2> Sum Calculator</h2>
       #     <form method = "post">
        #        <input type = "number" name = "a" required> +
         #       <input type = "number" name = "b" required>
          #      <button type = "submit">Calculate</button>
           # </form>
            #{ result_html}
#
        #</body>
    #</html>
 #   """
    #return HttpResponse(html)
    return render(request, "calc/home.html",{"result": result})
            
