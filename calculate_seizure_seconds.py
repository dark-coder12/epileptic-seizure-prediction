from datetime import datetime, timedelta


# Define the text in the given format
data = """

File Name: chb07_01.edf
File Start Time: 16:58:28
File End Time: 20:58:39
Number of Seizures in File: 0

File Name: chb07_02.edf
File Start Time: 21:00:13
File End Time: 25:00:13
Number of Seizures in File: 0

File Name: chb07_03.edf
File Start Time: 01:00:21
File End Time: 5:00:21
Number of Seizures in File: 0

File Name: chb07_04.edf
File Start Time: 05:00:29
File End Time: 9:00:29
Number of Seizures in File: 0

File Name: chb07_05.edf
File Start Time: 09:00:36
File End Time: 13:00:36
Number of Seizures in File: 0

File Name: chb07_06.edf
File Start Time: 13:00:44
File End Time: 14:22:44
Number of Seizures in File: 0

File Name: chb07_07.edf
File Start Time: 14:23:26
File End Time: 15:41:06
Number of Seizures in File: 0

File Name: chb07_08.edf
File Start Time: 15:45:54
File End Time: 19:45:54
Number of Seizures in File: 0

File Name: chb07_09.edf
File Start Time: 19:45:58
File End Time: 23:45:58
Number of Seizures in File: 0

File Name: chb07_10.edf
File Start Time: 23:46:06
File End Time: 27:46:06
Number of Seizures in File: 0

File Name: chb07_11.edf
File Start Time: 03:46:13
File End Time: 7:46:13
Number of Seizures in File: 0

File Name: chb07_12.edf
File Start Time: 07:46:22
File End Time: 11:46:22
Number of Seizures in File: 1
Seizure 1 Start Time: 4920 seconds
Seizure 1 End Time: 5006 seconds

File Name: chb07_13.edf
File Start Time: 11:46:29
File End Time: 12:48:35
Number of Seizures in File: 1
Seizure 1 Start Time: 3285 seconds
Seizure 1 End Time: 3381 seconds

File Name: chb07_14.edf
File Start Time: 12:48:54
File End Time: 16:48:54
Number of Seizures in File: 0

File Name: chb07_15.edf
File Start Time: 16:48:58
File End Time: 20:48:58
Number of Seizures in File: 0

File Name: chb07_16.edf
File Start Time: 20:49:06
File End Time: 24:49:06
Number of Seizures in File: 0

File Name: chb07_17.edf
File Start Time: 00:49:19
File End Time: 4:49:19
Number of Seizures in File: 0

File Name: chb07_18.edf
File Start Time: 04:49:28
File End Time: 8:10:28
Number of Seizures in File: 0

File Name: chb07_19.edf
File Start Time: 08:12:32
File End Time: 12:12:43
Number of Seizures in File: 1
Seizure 1 Start Time: 13688 seconds
Seizure 1 End Time: 13831 seconds

"""

# Split the data into individual sections for each file
file_sections = data.strip().split('\n\n')

# Initialize variables to store information
results = []

# Iterate through each file section
for section in file_sections:
    lines = section.split('\n')
    file_info = {}
    seizure_info = None
    
    # Parse and store the information for each file
    for line in lines:
        key, value = line.split(': ')
        if key == "File Start Time" or key == "File End Time":
            # Add leading zeros to hours if less than 10
            time_parts = value.split(':')
            if int(time_parts[0]) < 10 and key == "File End Time":
                value = f"0{time_parts[0]}:{time_parts[1]}:{time_parts[2]}"
        file_info[key] = value
        
        if key == "Number of Seizures in File" and int(value) > 0:
            # If seizures exist in the file, look for seizure information
            for line in lines:
                if line.startswith("Seizure 1 Start Time"):
                    # Include seizure information
                    seizure_start_seconds = int(line.split(': ')[1].split(' seconds')[0])
                elif line.startswith("Seizure 1 End Time"):
                    seizure_end_seconds = int(line.split(': ')[1].split(' seconds')[0])
                    seizure_duration = seizure_end_seconds - seizure_start_seconds
                    
                    # Calculate the seizure start and end times in h:mm:ss format relative to the file start and end times
                    file_start_time_parts = file_info["File Start Time"].split(':')
                    file_start_time_seconds = int(file_start_time_parts[0]) * 3600 + int(file_start_time_parts[1]) * 60 + int(file_start_time_parts[2])
                    seizure_start_hms = divmod(file_start_time_seconds + seizure_start_seconds, 3600)
                    seizure_end_hms = divmod(file_start_time_seconds + seizure_end_seconds, 3600)
                
                    seizure_info = (
                        f"Seizure Start Time (h:mm:ss): {seizure_start_hms[0]:02d}:{seizure_start_hms[1] // 60:02d}:{seizure_start_hms[1] % 60:02d} - "
                        f"Seizure End Time (h:mm:ss): {seizure_end_hms[0]:02d}:{seizure_end_hms[1] // 60:02d}:{seizure_end_hms[1] % 60:02d} \n\n"
                        f"Seizure Start Time: {seizure_start_seconds} seconds - Seizure End Time: {seizure_end_seconds} seconds (Duration: {seizure_duration} seconds)"
                          
                    )

    # Construct the result string for each file
    result_str = (
        f"File = {file_info['File Name']} - "
        f"Time: {file_info['File Start Time']} - {file_info['File End Time']} - "
        f"Number of Seizures in File: {file_info['Number of Seizures in File']}"
    )
    
    results.append(result_str)
    
    # Add seizure information if available
    if seizure_info:
        results.append("")
        results.append(seizure_info)
        results.append("______________________________________________")
    else:
        results.append("______________________________________________")

for result in results:
    print(result)
    