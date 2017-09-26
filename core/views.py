from django.shortcuts import render
from django.conf import settings
from django import views
from africastalking.AfricasTalkingGateway import (AfricasTalkingGateway, AfricasTalkingGatewayException)
from .models import Query, QuerySession, Requester, Mechanic, TowingVehicle
from django.db.models import Q
from .helpers import nearest_mechanics
from core.helpers import nearest_towing_vehicle
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# Create your views here.


class Uapp(views.View):
    template_name = 'core/user.html'
    params = {}
    
    def get(self, request):
        self.params["SERVICE_CODE"] = settings.SERVICE_CODE
        return render(self.request, self.template_name, self.params)


username = "dedayoa@gmail.com"
apikey   = "15a977d5795aa310d9b3b8fc7b859d23f05c1440dcc7f674702ee613fdbc8343"


@method_decorator(csrf_exempt, name='dispatch')
class ACUSSDCallback(views.View):
    # africastalking callback
    def post(self, request):
        session_id = request.POST.get("sessionId", None)
        print(session_id)
        serviceCode = request.POST.get("serviceCode", None)
        print(serviceCode)
        phoneNumber = request.POST.get("phoneNumber", None)
        print(phoneNumber)
        text = request.POST.get("text", None)
        print(text)
        
        requester = Requester.objects.filter(Q(mobile_1=phoneNumber) | Q(mobile_2=phoneNumber))
        
        if not requester.count():
            menu_text = "END User Not Found"
        
        elif text == "":
            menu_text = "END Invalid Entry"
            
        elif text == "1":
            if not QuerySession.objects.filter(session_id=session_id).exists():
                menu_text = "END Please Provide Your Coordinates"
            else:
                menu_text = "CON Mechanics near you... \n"
                for mechanic in nearest_mechanics(session_id, 3):
                    m_obj = Mechanic.objects.get(id=mechanic[0])
                    menu_text += "%s, %s \n"%(m_obj.user.first_name, m_obj.phone_1)
                    menu_text += "Press 1 to Call a Mechanic, 0 to end.\n"
        
        elif text == "2":
            if not QuerySession.objects.filter(session_id=session_id).exists():
                menu_text = "END Please Provide Your Coordinates"
            else:
                menu_text = "CON Towing Vehicles near you... \n"
                for tow_vehicle in nearest_towing_vehicle(session_id, 3):
                    tv_obj = TowingVehicle.objects.get(id=tow_vehicle[0])
                    menu_text += "%s, %s \n"%(tv_obj.user.first_name, tv_obj.phone_1)
                    menu_text += "Press 1 to Call a Towing Vehicle, 0 to end.\n"
        
        elif text == "3":
            if not QuerySession.objects.filter(session_id=session_id).exists():
                menu_text = "END Please Provide Your Coordinates"
            else:
                menu_text = "END"
        
        elif text == "4":
            if not QuerySession.objects.filter(session_id=session_id).exists():
                menu_text = "END Please Provide Your Coordinates"
            else:
                menu_text = "END"
        
        
        elif text == "1*1":
            menu_text = "END Calling Mechanics"
            
        elif text == "2*1":
            menu_text = "END Calling Towing Vehicle"
        
        elif text == "0":
            menu_text = "END Goodbye"
        
        
        else:
            #iterate through text and get coordinates
            coods = text.split("*")
            QuerySession.objects.create(
                session_id = session_id,
                loc_cood_x = int(coods[0])/10000,
                loc_cood_y = int(coods[1])/10000,
                service_code = serviceCode
                )
            
            
            menu_text = "CON Welcome %s. What help do you require?"%(requester.user.first_name)
            menu_text += "1. Mechanic \n"
            menu_text += "2. Towing Van \n"
            menu_text += "3. Car Part \n"
            menu_text += "4. Cab"
            
        return HttpResponse(menu_text, content_type="text/plain", status=200)
        