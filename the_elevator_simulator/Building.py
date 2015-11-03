# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 21:12:23 2015

@author: Ylva Lindberg
"""

import numpy

from Elevator import Elevator
from Call_for_elevator import Call_for_elevator

class Building(object):
    'A building with elevators'
    def __init__(self, name, FLOOR_COUNT, elevator_count):
        self.name = name
        self.FLOOR_COUNT = FLOOR_COUNT
        self.elevator_count = elevator_count
        self.elevators = []
        self.calls_for_elevator = []
        for i in range(0, self.elevator_count):
            self.elevators.append(Elevator(self, i, 1))

    def get_name(self):
        return self.name
    def get_floor_count(self):
        return self.FLOOR_COUNT
    def get_elevator_count(self):
        return self.elevator_count
    def get_elevators(self):
        return self.elevators
    
    def start_elevators(self):    
        for i in range(0, self.elevator_count):
            self.elevators[i].start_elevator()
            
    def stop_elevators(self):
        for i in range(0, self.elevator_count):
            self.elevators[i].stop_elevator()
    
    def get_elevators_statuses(self):
        status = []
        for i in range(0, self.elevator_count):
            status.append(self.elevators[i].get_elevator_status())
        return status
        
    def call_elevator(self, customer_floor, direction):
        # get this direction to select_floor
        call = Call_for_elevator(self, customer_floor, direction)
        self.calls_for_elevator.append(call)
        self.select_elevator(call)
        
        selected_elevator = call.get_assigned_elevator()    
        selected_elevator.recieve_call(call)
        
        print ("Elevator " + str(selected_elevator.get_name()) + " will go to " + str(customer_floor) + ".")
        return selected_elevator
        
    def select_elevator(self, call):
        '''
        Select the elevator closest going in the right direction.
        If all in wrong direction, choose elevator with destination closest to customer_floor.
        '''
        closeness = []
        for i in range(0, self.elevator_count):
            closeness.append(self.elevators[i].get_time_to_floor(call.get_floor()))
        priority = [i[0] for i in sorted(enumerate(closeness), key=lambda x:x[1])]
        for i in range(0, self.elevator_count):
            this_elevator = self.elevators[priority[i]]
            direction_to_selected_floor = numpy.sign(call.get_floor() - this_elevator.get_current_floor())
            
            if this_elevator.get_direction() == direction_to_selected_floor or this_elevator.get_direction() == 0:
                call.set_assigned_elevator(self.elevators[priority[i]])        
                
                if not this_elevator.get_destination_floor():
                    call.set_on_the_way(False)
                elif (this_elevator.get_direction() * call.get_floor() 
                        < this_elevator.get_direction()*this_elevator.get_destination_floor()[0]):
                    call.set_on_the_way(True)
                else:
                    call.set_on_the_way(False)
                    
                print('Selected elevator: ' + str(priority[i]))
                break
    
        if call.get_assigned_elevator() == None:
            closeness = []
            for i in range(0, self.elevator_count):
                closeness.append(abs(call.get_floor() - self.elevators[i].get_destination_floor()[0]))
            priority = [i[0] for i in sorted(enumerate(closeness), key=lambda x:x[1])]
            call.set_assigned_elevator(self.elevators[priority[0]])
            call.set_on_the_way(False)
            print('Selected elevator: ' + str(call.get_assigned_elevator()))