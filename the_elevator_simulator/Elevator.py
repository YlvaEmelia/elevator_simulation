# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 21:11:43 2015

@author: Ylva Lindberg
"""

from RepeatedTimer import RepeatedTimer
from time import sleep
import numpy

class Elevator(object):
    'An elevator'
    elevator_count = 0
    def __init__(self, building, name, current_floor):
        self.name = name
        self.current_floor = current_floor
        self.building = building
        self.destination_floor = []
        self.active_calls = []
        self.SPEED = 1 # s / floor
        self.TIME_AT_FLOOR = 5 # s / floor
        Elevator.elevator_count += 1
        self.run_timer = RepeatedTimer(self.SPEED, self.execute_call())
             
    def start_elevator(self):
        self.run_timer.start()
        
    def get_name(self):
        return self.name
        
    def get_current_floor(self):
        return self.current_floor
        
    def get_destination_floor(self):
        return self.destination_floor

    def get_direction(self):
        if not self.destination_floor:# or len(self.destination_floor) == 0:
            return 0
        else:
            return numpy.sign(self.destination_floor[0] - self.current_floor)       
    
    def get_speed(self):
        return self.SPEED
        
    def get_time_to_floor(self, floor):
        distance_to_destination = abs(floor - self.get_current_floor())  
        time_to_destination = self.get_speed()*distance_to_destination
        return time_to_destination
    
    def set_current_floor(self, floor):
        self.current_floor = floor
      
    def set_destination_floor(self, floor, on_the_way = False):
        if self.current_floor != floor:
            if on_the_way:
                self.destination_floor = [floor] + self.destination_floor
            else:
                self.destination_floor.append(floor)
               
    def execute_call(self):
        ''' checks if there is a call to execute. if yes, run elevator '''
        print('execute_call()')
        if self.active_calls:
            print("I got a call, Elevator " + str(self.name) + " will start!")
            self.run_timer.stop()
            self.run_elevator()
    
    def run_elevator(self):
        curret_call = self.active_calls[0]
        while self.current_floor != self.destination_floor[0]:
            new_floor = self.current_floor + self.get_direction() 
            self.set_current_floor(new_floor)
            sleep(self.SPEED)
        
        self.stop_at_floor(curret_call)

    def stop_at_floor(self, call):
        floor = call.get_floor()
        print ("Elevator " + str(self.name) + " now at floor " + str(floor) + ".")
        sleep(self.TIME_AT_FLOOR)
        self.destination_floor = [x for x in  self.destination_floor if x != floor]
        call.get_selected_floor()
        self.run_timer.start()

    def recieve_call(self, call):
        print ("Elevator " + str(self.name) + "has recieved a call.")
        self.active_calls.append(call)
        self.set_destination_floor(call.get_floor(), call.get_on_the_way())

    def stop_elevator(self):
        print ("Elevator to stop: " + str(self.name))
        if self.get_elevator_status() == "Running":
            self.run_timer.stop()
    
    def get_elevator_status(self):
        if self.run_timer.isRunning():
            return "Running"
        else: 
            return "Terminated"