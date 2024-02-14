from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt,ensure_csrf_cookie
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import action
from TaskApp.models import Table 
from TaskApp.serializers import TableSerializer , GroupSerializer, UserSerializers
from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets,  status
import sqlite3

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializers
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


# Create your views here.

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    permission_classes = [permissions.IsAuthenticated]
   # @action(detail=True, methods=["post"])
@csrf_exempt
def tableApi(request,SubjectA,SubjectB):
    conn = sqlite3.connect("db.sqlite3")
    cursor = conn.cursor()
    # if request.method=='GET':
    #     table= Table.objects.all()
    #     table_serializer = TableSerializer(table, many = True)
    #     return JsonResponse(table_serializer.data, safe=False)

    #Creating connection with database

    if request.method=='POST':
        data = JSONParser().parse(request)
        # print("data request parse:")---> output: {'SubjectA': 2, 'SubjectB': 23}
        # print(data)
        SubjectA = int(data.get('SubjectA'))
        # print(data.get('SubjectA'))----> output: 2(Example)
        SubjectB = int(data.get('SubjectB')) # output: 3(Example)
        
        # SubjectAs = int(SubjectA)
        # print("direct ako value")
        # print(SubjectAs)
        Total = SubjectA + SubjectB # output: 5(Example)
        Average = Total/2
        print(Average)
        tables_data= {'SubjectA': SubjectA,'SubjectB': SubjectB,'Total': Total,'Average':Average}
        tables_serializer = TableSerializer(data= tables_data)
        # print(tables_serializer)

        if tables_serializer.is_valid():
            
            # query = 'UPDATE TaskApp_table SET SubjectA = {}, SubjectB= {}, Total= {} '
            
            cursor.execute("UPDATE TaskApp_table SET SubjectA = {}, SubjectB= {}, Total= {}, Average={}".format(SubjectA,SubjectB,Total,Average))
            conn.commit()
            print(tables_serializer.data)
            return JsonResponse(tables_serializer.data)
        
        
        
         
        # if tables_serializer.is_valid():
        
        # tables_serializer.save()
        
        #print(tables_serializer)
        
        #     tables_serializer.save()
        #     print((tables_serializer.data))
        #     serialized_data = json.dumps(tables_serializer.data)
        #     print("Serialized Data:", serialized_data)
        #     # return JsonResponse("Added Successfully!!" , safe=False)
        #     return JsonResponse(serialized_data, safe= False)
        # return JsonResponse(tables_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # if tables_serializer.is_valid():
        #     try:
        #         tables_serializer.save()
        #         return JsonResponse(tables_serializer.data)
        #     except Exception as e:
        #         print(f"Error saving serializer: {e}")
        #         return JsonResponse({"error": str(e)})
        # else:
        #     print(tables_serializer.errors)
        #     return JsonResponse(tables_serializer.errors)
        
        #     return tables_serializer.data
        #     includes all serialized fields
 