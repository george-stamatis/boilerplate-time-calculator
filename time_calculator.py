def add_time(start, duration, start_day=None):
  flag = False
  next_day = False
  # Parse start time
  start_time, time_of_day = start.split()
  start_h, start_m = [int(x) for x in start_time.split(":")]
  #print (start_h, start_m)

  # Parse duration
  duration_h, duration_m = [int(x) for x in duration.split(":")]

  # Calculate total hours and minutes
  total_h = start_h + duration_h
  total_m = start_m + duration_m

  # Handle overflow of minutes
  if total_m >= 60:
    total_m -= 60
    total_h += 1
    flag = True

  # Handle overflow of hours (12-hour clock)
  result_h = total_h % 12

  if result_h == 0:
    result_h = 12

  if time_of_day == "PM":
    if (start_h + (1 if flag else 0) + (duration_h % 12)) < 12:
      result_time_of_day = "PM"
    else:
      result_time_of_day = "AM"
  else:
    if (start_h + (1 if flag else 0) + (duration_h % 12)) < 12:
      result_time_of_day = "AM"
    else:
      result_time_of_day = "PM"

  # Determine if it's the next day
  if time_of_day == "PM" and result_time_of_day == "AM" and duration_h <= 12:
    next_day = True
  if time_of_day == "AM" and result_time_of_day == "AM" and 12 <= duration_h <= 24:
    next_day = True
  if time_of_day == "PM" and result_time_of_day == "PM" and 12 <= duration_h <= 24:
    next_day = True
  if time_of_day == "AM" and result_time_of_day == "PM" and 24 < duration_h + (
      1 if flag else 0) > 12:
    next_day = True

  num_days_later = (duration_h // 24)
  if num_days_later == 0:
    if flag == False:
      num_days_later = 1 if next_day else 0
    else:
      num_days_later = 2 if total_h == 36 else 1
  elif num_days_later > 0:
    if flag == False:
      num_days_later = num_days_later + (1 if (start_h + duration_h) % 24 >= 12
                                         else 0)
    else:
      num_days_later = num_days_later + (1 if
                                         (start_h + 1 + duration_h) % 24 >= 12
                                         else 0)

  # Format the result
  result_time = f"{result_h}:{total_m:02d} {result_time_of_day}"
  if start_day:
    start_day = start_day.lower().capitalize()
    days_of_week = [
        "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday",
        "Sunday"
    ]
    start_day_index = days_of_week.index(start_day)
    result_day_index = (start_day_index + num_days_later) % 7
    result_day = days_of_week[result_day_index]
    result_time += f", {result_day}"
    if next_day:
      result_time += " (next day)"
    elif num_days_later > 1:
      result_time += f" ({num_days_later} days later)"
  else:
    if next_day:
      result_time += " (next day)"
    elif num_days_later > 1:
      result_time += f" ({num_days_later} days later)"

  return result_time
