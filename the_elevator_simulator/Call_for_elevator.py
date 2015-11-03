# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 21:13:21 2015

@author: Ylva Lindberg
"""

from random import randint

class Call_for_elevator(object):
    def __init__(self, building, customer_floor, direction):
        self.building = building
        self.floor = customer_floor
        self.direction = direction
        self.assigned_elevator = None
        self.on_the_way = False #if this call is on the way for currently performed call
        self.select_floor()
        
    def get_floor(self):
        return self.floor
    
    def get_direction(self):
        return self.direction
    
    def get_assigned_elevator(self):
        return self.assigned_elevator
        
    def get_on_the_way(self):
        return self.on_the_way
        
    def get_selected_floor(self):        
        return self.selected_floor
    
    def set_assigned_elevator(self, elevator):
        self.assigned_elevator = elevator
        return self.assigned_elevator
        
    def set_on_the_way(self, elevator_floor):
        # on the way if: self.floor btw elevator.current_floor and elevator.dist_floor
        #                AND elevator.direction == self.direction
        self.on_the_way = (elevator_floor - self.floor == self.direction)
        return self.on_the_way
        
    def set_selected_floor(self, floor):
        self.selected_floor = floor
        
    def select_floor(self):
        # get direction from call_elevator()
        if self.get_direction() == -1:
            selected_floor = randint(0, self.floor-1)
        elif self.get_direction() == 1:
            selected_floor = randint(self.floor+1, self.building.get_floor_count())
        else:
            selected_floor = self.floor
            
        self.set_selected_floor(selected_floor)
        #print ("Elevator " + str(self.name) + " is selected to go to " + str(selected_floor) + ".")