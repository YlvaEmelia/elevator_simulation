# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 15:38:01 2015

@author: Ylva Lindberg
"""

import csv
import numpy
import matplotlib.pyplot as plt
from RepeatedTimer import RepeatedTimer


class Elevator_tracker(object):
    def __init__(self, building, TRACKER_INTERVAL = 1):
        self.building = building
        self.elevators = building.get_elevators()
        self.elevator_count = len(self.elevators)
        self.TRACKER_INTERVAL = TRACKER_INTERVAL
        self.visited_floors = [x[:] for x in [[]*self.elevator_count]*self.elevator_count]
        self.tracker_timer = RepeatedTimer(self.TRACKER_INTERVAL, self.get_elevators_floors)

    def start_tracking(self):    
        self.tracker_timer.start()
        
    def end_tracking(self):
        self.tracker_timer.stop()
        return self.visited_floors
        
    def get_tracker_status(self):
        if self.tracker_timer.isRunning():
            return "Running"
        else: 
            return "Terminaed"
        
    def get_elevators_floors(self):
        for i in range(0, self.elevator_count):
            self.visited_floors[i].append(self.elevators[i].get_current_floor())
        
    def save_result(self):      
        print (self.visited_floors)
        with open('visited_floors.csv', 'a') as fp:
            a = csv.writer(fp, delimiter=',', lineterminator="\n")
            a.writerows(self.result)
            
    def plot_track(self):
        #plt.hold(True)
        fig = plt.figure() 
        ax = fig.add_subplot(1,1,1)   
        x_axis = numpy.arange(0, len(self.visited_floors[0])*self.TRACKER_INTERVAL, self.TRACKER_INTERVAL)
        labels = []
        lines = [] 
        for i in range(0, self.elevator_count):
            lines += plt.plot(x_axis, self.visited_floors[i], label='Elevator '+ str(i))
            #plt.plot(x_axis, self.visited_floors[i])
        
        # Plot decorations        
        major_ticks = numpy.arange(0, self.building.get_floor_count(), 1)                                              
        ax.set_yticks(major_ticks)
        labels = [l.get_label() for l in lines]
        plt.legend(lines, labels)
        plt.xlabel('Time [s]')
        plt.ylabel('Floor')
        plt.show()
