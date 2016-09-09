import json
courses = json.loads(open('new_plan.json').read())
num_class = int(input("Enter the number of courses to be scheduled:\n"))
inputs = []
#record the courses to be scheduled
for i in range(0, num_class):
        inputs.append(raw_input())
def plan(outputs, slots, cursor, no_of_section):
        #finished
        if cursor == num_class * 3:
                print(outputs)
        else:
                if cursor % 3 == 1:
                        #tutorial
                        tp = 'T'
                elif cursor % 3 == 2:
                        #lab
                        tp = 'LA'
                else:
                        #lecture
                        tp = 'L'
                for i in range(0, len(courses[ inputs[cursor/3] ][tp]) ):
                        #reset the sets
                        while len(outputs) > no_of_section:
                                outputs.pop()
                                slots.pop()

                        clash = False
                        #EXAMPLE: courses[ inputs[cursor/3] ][tp][i]['Period']: [  [101, 103] , [ 202, 203]  ]
                        #EXAMPLE: slot: [[[115, 116, 117], [506, 507, 508]], [[121, 122]]]
                        for section in courses[ inputs[cursor/3] ][tp][i]['Period']:
                                for hour in section:
                                        for slot in slots:
                                                for section_ in slot:
                                                        if hour in section_:
                                                                clash = True
                                                                break
                        if clash == False:                                
                                if tp == 'L':
                                        outputs.append(str(inputs[cursor/3])+' '+str(courses[ inputs[cursor/3] ][tp][i]['Name']))
                                else:
                                        outputs.append( str(courses[ inputs[cursor/3] ][tp][i]['Name']) )
                                slots.append(courses[ inputs[cursor/3] ][tp][i]['Period'])
                                
                                plan(outputs, slots, cursor+1, no_of_section+1)
                if len(courses[ inputs[cursor/3] ][tp]) == 0:
                        #reset the sets
                        while len(outputs) > no_of_section:
                                outputs.pop()
                                slots.pop()
                        plan(outputs, slots, cursor+1, no_of_section)
print(plan([], [], 0, 0))

                
                 

