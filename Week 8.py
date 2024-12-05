Dam = {True: [1234, 1121], False: {'s':[12, 22, 12, 9]}, 'Colleges':['BelfastMet','QUB','Ulster Uni'],0.245:'This is a Float'}
print(Dam[False]['s'][1])

ep1 = {'EmployeeID':[221092], 'EmployeeName':['Fedrick Zocco'], 'NumberOfExperience':[2], 'CurrentPosition':['Research Scientist']}
for ep_data in ep1.values():
    if ep_data == 'EmployeeID':
        ep1[ep_data]=50057852
    elif ep_data == 'EmployeeName':
        ep1[ep_data]='Matthew Gribben'
    elif ep_data == 'CurrentPosition':
        ep1[ep_data]='Apprentice'
    print(ep1)