def sorting_task(dic):
    soted_by_values = dict(sorted(dic.items(), key=lambda item:item[1]))
    return soted_by_values


task = {"Buy groceries": "2024-12-20", "Pay bills": "2024-12-22","Go to the market": "2024-12-28","Go to sky": "2024-12-19"}
sored_task = sorting_task(task)

for i, (key, value) in enumerate(sored_task.items()):
    if i < len(sored_task) - 1:
        print(f"{key}: {value},")
    else:
        print(f"{key}: {value}")
        

    





