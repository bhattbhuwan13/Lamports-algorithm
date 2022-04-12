import sys

from modules.process import Event,Process

e1 = Event("e1",1,None)
e2 = Event("e2",2,None)
e3 = Event("e3",4,None)
e4 = Event("e4",3,e2)
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
        all_events.extend(iter(process.events))
    new_events = sorted(all_events, key=lambda event: event.has_order())

    for event in new_events:
        # print(event)
        if event.has_sender():
            for process in all_processes:
                if event in process.events:
                    current_time_for_receiving_event = process.get_time()
                    # print(current_time_for_receiving_event)
                    break
            # print("receiving event")
            for process in all_processes:
                # print(event.sender_event())
                if event.sender_event() in process.events:
                    # print("The process is " + str(process))
                    current_time_for_sending_event = process.get_time()
                    break

            new_time = max(current_time_for_sending_event,
                           current_time_for_receiving_event
                          ) + 1

            for process in all_processes:
                if event in process.events:
                    process.set_time(new_time)
                    break

        else:
            for process in all_processes:
                if event in process.events:
                    current_time_for_receiving_event = process.get_time()

            new_time = current_time_for_receiving_event + 1

            for process in all_processes:
                if event in process.events:
                    process.set_time(new_time)

        event.set_time_stamp(new_time)

    for event in new_events:
        print(f"{str(event.name)} {str(event.order)} {str(event.time_stamp)}")
lamport([p1,p2,p3])
