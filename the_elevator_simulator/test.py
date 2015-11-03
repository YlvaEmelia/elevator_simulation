# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 10:49:51 2015

@author: Ylva Lindberg
"""

from time import sleep
from Elevator_tracker import Elevator_tracker
from Building import Building


# from imp import reload
# reload(elevator_simulation)
# elevator_simulation.test_elevators()


def test2():         
    ELEVATOR_COUNT = 2
    theBuilding = Building("Blair Plaza", 17, ELEVATOR_COUNT)
    theBuilding.start_elevators()
    theTracker = Elevator_tracker(theBuilding, 1) #0.2
    theTracker.start_tracking()
    print ("The End")
    theTracker.end_tracking()

def test_elevators():
    ELEVATOR_COUNT = 2
    theBuilding = Building("Blair Plaza", 17, ELEVATOR_COUNT)
    theBuilding.start_elevators()
    print("Elevator status: " + ', '.join(theBuilding.get_elevators_statuses()))
    
    theTracker = Elevator_tracker(theBuilding, 0.2)
    theTracker.start_tracking()
    
    
    sleep(1.5)
    theBuilding.call_elevator(4, -1)
    sleep(2.5)
#    theBuilding.call_elevator(8, 1)
    sleep(5)
#    theBuilding.call_elevator(2, 1)
#    sleep(10)
    
    print ("The End")
    theBuilding.stop_elevators()
    print("Elevator status: " + ', '.join(theBuilding.get_elevators_statuses()))
    theTracker.end_tracking()
    #print("Tracker status: " + theTracker.get_tracker_status())
    theTracker.plot_track()
    