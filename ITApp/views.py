from django.shortcuts import render
from .models import ItInstitute,ItContactInformation
from .serializers import ItInstituteSerializer,ItContactInformationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK,HTTP_201_CREATED,HTTP_400_BAD_REQUEST

# Create your views here.

class GetPostITAPI(APIView):
  
  def get(self,request):
    Itinsts = ItInstitute.objects.all()
    Itinsts_serial = ItInstituteSerializer(Itinsts,many=True)
    return Response(Itinsts_serial.data,status=HTTP_200_OK)
  
  def post(self,request):
    Itinst_serial = ItInstituteSerializer(data=request.data)
    if Itinst_serial.is_valid()==True:
      Itinst_serial.save()
      return Response(Itinst_serial.data,status=HTTP_201_CREATED)
    else:
      return Response(Itinst_serial.errors, status=HTTP_400_BAD_REQUEST)
    
class PutFetchDeleteITAPI(APIView):
  
  def put(self,request,pk):
    Itinst = ItInstitute.objects.get(It_id = pk)
    Itinst_serial = ItInstituteSerializer(Itinst, data=request.data)
    if Itinst_serial.is_valid()==True:
      Itinst_serial.save()
      return Response(Itinst_serial.data,status=HTTP_200_OK)
    else:
      return Response(Itinst_serial.errors, status=HTTP_400_BAD_REQUEST)
    
  def get(self,request,pk):
    Itinst = ItInstitute.objects.get(It_id = pk)
    Itinst_serial = ItInstituteSerializer(Itinst)
    return Response(Itinst_serial.data,status=HTTP_200_OK)
  
  def delete(self,request,pk):
    Itinst = ItInstitute.objects.get(It_id=pk)
    Itinst.delete()
    return Response(status=HTTP_200_OK)
  
class GetPostITContactAPI(APIView):
  
  def get(self,request):
    Itconts = ItContactInformation.objects.all()
    Itconcts_serial =ItContactInformationSerializer(Itconts,many=True)
    return Response(Itconcts_serial.data,status=HTTP_200_OK)

  def post(self,request):
    Itcont_serial = ItContactInformationSerializer(data=request.data)
    if Itcont_serial.is_valid()==True:
      Itcont_serial.save()
      return Response(Itcont_serial.data,status=HTTP_201_CREATED)
    return Response(Itcont_serial.errors,status=HTTP_400_BAD_REQUEST)
  
class PutFetchDeleteITContactAPI(APIView):
  
  def put(self,request,pk):
    Itcont = ItContactInformation.objects.get(it_contact_id = pk)
    Itcont_serial =ItContactInformationSerializer(Itcont, data = request.data)
    if Itcont_serial.is_valid()==True:
      Itcont_serial.save()
      return Response(Itcont_serial.data,status=HTTP_200_OK)
    return Response(Itcont_serial.errors,status=HTTP_400_BAD_REQUEST)
  
  def get(self,request,pk):
    Itcont = ItContactInformation.objects.get(it_contact_id = pk)
    Itcont_serial =ItContactInformationSerializer(Itcont)
    return Response(Itcont_serial.data, status=HTTP_200_OK)
  
  def delete(self,request,pk):
    Itcont = ItContactInformation.objects.get(it_contact_id = pk)
    Itcont.delete()
    return Response(status=HTTP_200_OK)