class Event:
    def __init__(self,name="NONE",order=0,sender_is=None,time_stamp = 0):

        self.name = name
        self.order = order
        self.sender_is = sender_is
        self.time_stamp = time_stamp

    def __str__(self):
        return(self.name)

    def has_sender(self):
        if self.sender_is != None:
            return True
        else:
            return False

    def sender_event(self):
        return self.sender_is

    def has_time_stamp(self):
        return(self.time_stamp)

    def set_time_stamp(self,time):
        self.time_stamp = time
    def has_order(self):
        return(self.order)


class Process(Event):
    def __init__(self,name=None,events=[],clock=0):
        self.name = name
        self.events = events
        self.clock = clock
        # super().__init__(self)
    def __str__(self):
        return(self.name)

    def add_event(self,event):
        self.events.append(event)

    def process_name(self):
        print(self.name)

    def get_time(self):
        return self.clock

    def set_time(self,time):
        self.clock = time
    def display_events(self):
        for event in self.events:
            print(event.name)
            print(event.has_sender())
