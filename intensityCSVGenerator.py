################################################
# output format:
# ParticipandID Calibration Sensation Pain ActualValue
#   1               initial 2.5         5.8     4.5
#   1               middle  2.9         6.3     4.9
#   1               final   3.0         6.4     5.1
#   ...
################################################

import os # for multiplatform os.path

data_folder = "rawdata"

result = list()

# for each participant, read static csv file
directories = os.listdir (data_folder)
nr_participants = len(directories)
for i in range(nr_participants):
    participant_id = (i+1)
    file_to_open = os.path.join (data_folder, str(participant_id))
    file_to_open = os.path.join (file_to_open, str(participant_id) + "_staticLog.log")
    # print(file_to_open)

    with open(file_to_open, "r") as log_file:
        lines = log_file.readlines()

        initial_calibration = lines[19]
        middle_calibration = lines[20]
        final_calibration = lines[21]

        initial_calibration = initial_calibration.replace('(', '')
        initial_calibration = initial_calibration.replace(')', '')

        middle_calibration = middle_calibration.replace('(', '')
        middle_calibration = middle_calibration.replace(')', '')

        final_calibration = final_calibration.replace('(', '')
        final_calibration = final_calibration.replace(')', '')

        initial_values = initial_calibration.split(',')
        middle_values = middle_calibration.split(',')
        final_values = final_calibration.split(',')

        initial_values = [float(x) for x in initial_values]
        middle_values = [float(x) for x in middle_values]
        final_values = [float(x) for x in final_values]

        initial_entry = [participant_id, "initial", initial_values[0], initial_values[1], initial_values[2]]
        middle_entry = [participant_id, "middle", middle_values[0], middle_values[1], middle_values[2]]
        final_entry = [participant_id, "final", final_values[0], final_values[1], final_values[2]]

        result.append(initial_entry)
        result.append(middle_entry)
        result.append(final_entry)

output_file = open("intensities.csv", "w")
output_file.write("ParticipantID,Calibration,Sensation,Pain,ActualValue\n")
for entry in result:
    #print(entry)
    line = ','.join([str(i) for i in entry])
    output_file.write(line + '\n')
output_file.close()


