import json
import pickle

courses = json.loads(open('new.json').read())

course_slots=dict()


current_course = ""
for course_id in courses:
	
    enter = dict()
    #enter["Abbr"] = courses[course_id]["Abbr"]
    enter["L"] = []
    enter["T"] = []
    enter["LA"] =[]
    for section in courses[course_id]["Sections"]:
    	sec = dict()
    	sec["Name"] = section["Name"]
    	sec["Period"] = []
    	for i in range(0, len(section["ParsedTime"]["MeetTimes"])):
    		sec["Period"].append([])
    		#[ [start, end] [] []]
    		st=section["ParsedTime"]["MeetTimes"][i]["Day"]*100+section["ParsedTime"]["MeetTimes"][i]["StartTime"]
    		ed=section["ParsedTime"]["MeetTimes"][i]["Day"]*100+section["ParsedTime"]["MeetTimes"][i]["EndTime"]
    		for t in range(st, ed+1):
    			sec["Period"][i].append(t)
    		
    		
    	if "LA" in section["Name"]:
    		enter["LA"].append(sec)
    	elif "T" in section["Name"]:
    		enter["T"].append(sec)
    	elif "L" in section["Name"]:
    		enter["L"].append(sec)
    course_slots[courses[course_id]["Abbr"]] = enter
    
    
with open ('new_plan.json','w') as fp:
    json.dump(course_slots, fp, indent = 4)