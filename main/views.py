from django.shortcuts import render
from main.models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from cors.models import *
from cors.http_codes import http_codes
import pandas as pd
# from helpers.verification import Verifier
import json

# Create your views here.

def index(request):
    return HttpResponse(json.dumps({"response": "success", "message": "Sorry no content here. Maybe download the app."}))

@csrf_exempt
def project_list(request):
       
    project_list = Project.objects.all().values("title")

    resp = (json.dumps({"response": {"task_successful": True, "content": {
                                "code": http_codes["OK"], "projects": list(project_list), "message": ""}, "auth_keys": {"access_token": "NULL"}}}))

    return CORS(resp).allow_all()   
        
@csrf_exempt
def lga_list(request):

    if request.method == 'POST':
        body = json.loads(request.body)
        project_title = body["project"]
        state         = body["state"]
        
        lgas = Project.objects.get(title = project_title).get_lga_for_state(state)
    
        resp = (json.dumps({"response": {"task_successful": True, "content": {
                                "code": http_codes["OK"], "LGAs": list(lgas), "message": ""}, "auth_keys": {"access_token": "NULL"}}}))

        return CORS(resp).allow_all()   
            
    else:    
        resp = HttpResponse(json.dumps({"response": "failure", "message": f"Credentials not added (invalid access token)"}))
        resp = CORS.allow_all(resp)
        return resp

@csrf_exempt
def project_column_list(request):

    if request.method == 'POST':
        body = json.loads(request.body)
        project_title = body["project"]
        
        columns = Project.objects.get(title = project_title).get_data_columns()
    
        resp = (json.dumps({"response": {"task_successful": True, "content": {
                                "code": http_codes["OK"], "LGAs": list(columns), "message": ""}, "auth_keys": {"access_token": "NULL"}}}))

        return CORS(resp).allow_all()   
            
    else:    
        resp = HttpResponse(json.dumps({"response": "failure", "message": f"Credentials not added (invalid access token)"}))
        resp = CORS.allow_all(resp)
        return resp

@csrf_exempt
def compute_columns(request):

    if request.method == 'POST':
        body = json.loads(request.body)
        project_title = body["project"]
        state = body["state"]
        lga = body["lga"]        
        col1 = body["col1"]
        col2 = body["col2"]
        col3 = body["col3"]
        
        columns = Project.objects.get(title = project_title).compute_columns(state, lga, col1, col2, col3)
    
        resp = (json.dumps({"response": {"task_successful": True, "content": {
                                "code": http_codes["OK"], "LGAs": columns, "message": ""}, "auth_keys": {"access_token": "NULL"}}}))

        return CORS(resp).allow_all()   
            
    else:    
        resp = HttpResponse(json.dumps({"response": "failure", "message": f"Credentials not added (invalid access token)"}))
        resp = CORS.allow_all(resp)
        return resp