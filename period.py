start_time = input("start time (HH:MM):")
start_time_h = int(start_time[0:2])
start_time_m = int(start_time[3:5])

end_time = input("end time (HH:MM):")
end_time_h = int(end_time[0:2])
end_time_m = int(end_time[3:5])

duration_h = end_time_h - start_time_h 
duration_m = end_time_m - start_time_m

duration_m_f = duration_h * 60 + duration_m + 24 * 60 * (start_time_h > end_time_h)
print("Event duration:", duration_m_f, "minutes")

duration_h_m = duration_m_f // 60
duration_m_m = duration_m_f % 60

if duration_h_m < 10:
    print("Event duration:", "0" + str(duration_h_m), "hour", duration_m_m, "minutes")
else:
    print("Event duration:", duration_h_m, "hour", duration_m_m, "minutes")