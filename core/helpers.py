'''
Created on Sep 23, 2017

@author: dayo_bf
'''

from geopy.distance import vincenty

from .models import Mechanic, QuerySession, TowingVehicle


def distance_between(a,b):
    # a and b are tuples
    return (vincenty(a, b).meters)


def nearest_mechanics(session_id, x=10):
    #get a list of nearest x mechanics
    requester = QuerySession.objects.get(session_id=session_id)
    res = []
    for mechanic in Mechanic.objects.all():
        dist_b = distance_between((requester.loc_cood_x, requester.loc_cood_y), (mechanic.office_cood_x, mechanic.office_cood_y))
        res.append((mechanic.id, dist_b))
    
    #sort
    return (sorted(res, key=lambda tup: tup[1]))[:x]
    
    
def nearest_towing_vehicle(session_id, x=10):
    #get a list of nearest x mechanics
    requester = QuerySession.objects.get(session_id=session_id)
    res = []
    for tow_veh in TowingVehicle.objects.all():
        dist_b = distance_between((requester.loc_cood_x, requester.loc_cood_y), (tow_veh.loc_cood_x, tow_veh.loc_cood_y))
        res.append((tow_veh.id, dist_b))
    
    #sort
    return (sorted(res, key=lambda tup: tup[1]))[:x]