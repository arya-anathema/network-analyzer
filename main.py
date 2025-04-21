import os

# data directory
data_dir = "data"
websites = {}

# string to write to CSV file
data_str = "Packet_Count,Total_Length,Average_Packet_Interval,Maximum_Packet_Interval,Minimum_Packet_Interval,Average_Packet_Length,Maximum_Packet_Length,Minimum_Packet_Length,Most_Common_Packet_Length,Label\n"

# loop through each website in data directory
for subfolder in os.listdir(data_dir):
    subfolder_path = os.path.join(data_dir, subfolder)

    websites[subfolder] = 0

    # loop through each CSV file in the website folder
    for filename in os.listdir(subfolder_path):
        file_path = os.path.join(subfolder_path, filename)
        websites[subfolder] += 1

        # open CSV file
        with open(file_path, 'r') as file:
            # toss out the header line
            file.readline()

            packet_count = 0
            total_length = 0
            total_interval = 0
            previous_interval = 0
            max_interval = 0
            min_interval = 9999999999
            max_length = 0
            min_length = 9999999999
            most_common_packet_length = 0
            packet_lengths = []

            # loop through packets, taking important stats
            for line in file:
                line = line.strip()
                packet_info = line.split(",")

                packet_count += 1
                length = int(packet_info[5][1:-1])
                total_length += length
                interval = float(packet_info[1][1:-1]) - previous_interval
                total_interval += interval

                if interval > max_interval:
                    max_interval = interval
                if interval < min_interval:
                    min_interval = interval
                if length > max_length:
                    max_length = length
                if length < min_length:
                    min_length = length

                packet_lengths.append(length)
                previous_interval = interval

            average_packet_interval = total_interval / packet_count
            average_packet_length = total_length / packet_count
            most_common_packet_length = max(set(packet_lengths), key=packet_lengths.count)

            # compile data into list
            data = [
                str(packet_count),
                str(total_length),
                str(average_packet_interval),
                str(max_interval),
                str(min_interval),
                str(average_packet_length),
                str(max_length),
                str(min_length),
                str(most_common_packet_length),
                str(subfolder)
            ]
            data_str = data_str + ",".join(data) + "\n"

# write all the data to a new CSV file
with open("formatted_data.csv", "w") as f:
    f.write(data_str)

# extra data for another, smaller CSV file
label_data_str = "label,Size\n"

for key, value in websites.items():
    label_data_str = label_data_str + key + "," + str(value) + "\n"

with open("website_data_counts.csv", "w") as f:
    f.write(label_data_str)