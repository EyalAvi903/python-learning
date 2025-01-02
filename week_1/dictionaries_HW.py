def sorting_task(dic):
    """
    Sorts a dictionary by its values in ascending order.

    Args:
        dic (dict): Dictionary with keys as tasks and values as deadlines.

    Returns:
        dict: Dictionary sorted by deadlines.
    """
    sorted_by_values = dict(sorted(dic.items(), key=lambda item:item[1]))
    return sorted_by_values


task = {"Buy groceries": "2024-12-20", "Pay bills": "2024-12-22","Go to the market": "2024-12-28","Go to sky": "2024-12-19"}
sorted_task = sorting_task(task)

print(",\n".join([f"{key}: {value}" for key, value in sorted_task.items()]))    ## code review fix  print key value (shortly code)

# for i, (key, value) in enumerate(sorted_task.items()):
#     if i < len(sorted_task) - 1:
#         print(f"{key}: {value},")
#     else:
#         print(f"{key}: {value}")
        

    





