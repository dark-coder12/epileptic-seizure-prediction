data = """
File Name: chb01_03.edf
File Start Time: 13:43:04
File End Time: 14:43:04
Number of Seizures in File: 1
Seizure Start Time: 2996 seconds
Seizure End Time: 3036 seconds

File Name: chb01_04.edf
File Start Time: 14:43:12
File End Time: 15:43:12
Number of Seizures in File: 1
Seizure Start Time: 1467 seconds
Seizure End Time: 1494 seconds

File Name: chb01_15.edf
File Start Time: 01:44:44
File End Time: 2:44:44
Number of Seizures in File: 1
Seizure Start Time: 1732 seconds
Seizure End Time: 1772 seconds

File Name: chb01_16.edf
File Start Time: 02:44:51
File End Time: 3:44:51
Number of Seizures in File: 1
Seizure Start Time: 1015 seconds
Seizure End Time: 1066 seconds

File Name: chb01_18.edf
File Start Time: 04:45:06
File End Time: 5:45:06
Number of Seizures in File: 1
Seizure Start Time: 1720 seconds
Seizure End Time: 1810 seconds

File Name: chb01_21.edf
File Start Time: 07:33:46
File End Time: 8:33:46
Number of Seizures in File: 1
Seizure Start Time: 327 seconds
Seizure End Time: 420 seconds

File Name: chb01_26.edf
File Start Time: 12:34:22
File End Time: 13:13:07
Number of Seizures in File: 1
Seizure Start Time: 1862 seconds
Seizure End Time: 1963 seconds
"""

# Split the data into blocks using double line breaks
blocks = data.strip().split('\n\n')

# Initialize an empty dictionary to store the data
data_dict = {}

for block in blocks:
    lines = block.strip().split('\n')
    file_info = {}
    
    for line in lines:
        key, value = line.split(': ')
        file_info[key] = value
    
    file_name = file_info['File Name']
    start_time = file_info['File Start Time']
    end_time = file_info['File End Time']
    
    data_dict[file_name] = {
        'File Start Time': start_time,
        'File End Time': end_time
    }

print(data_dict)
