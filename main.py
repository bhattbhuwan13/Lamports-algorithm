import sys

from modules.process import Event,Process

e1 = Event("e1",1,None)
e2 = Event("e2",2,None)
e3 = Event("e3",3,None)
e4 = Event("e4",4,e2)
e5 = Event("e5",5,None)
e6 = Event("e6",6,None)
e7 = Event("e7",7,e6)
e8 = Event("e8",8,None)
e9 = Event("e9",9,e3)


p1 = Process("P1",[e1,e2,e5],0)
p2 = Process("P2",[e4,e3,e6],0)
p3 = Process("P3",[e7,e8,e9],0)
# p2.display_events()
# if p1.search_event(e1):
#     print("Element found")


# sys.exit()
def lamport(all_processes):
    all_events = []
    for process in all_processes:
        for event in process.events:
            all_events.append(event)

    print("Before sorting")
    [print(event.name) for event in all_events]

    print("After sorting")
    new_events = sorted(all_events, key=lambda event: event.has_order())
    for event in new_events:
        print(event.name)
lamport([p1,p2,p3])
