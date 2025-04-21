import os

# data directory
data_dir = "data"
websites = {}

# loop through each website in data directory
for subfolder in os.listdir(data_dir):
    subfolder_path = os.path.join(data_dir, subfolder)

    websites[subfolder] = 0

    # loop through each CSV file in the website folder
    for filename in os.listdir(subfolder_path):
        file_path = os.path.join(subfolder_path, filename)
        websites[subfolder] += 1

        # print(f"subfolder name: {subfolder}, file name: {filename}")

        # open CVS file
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

            print(f"total packet count: {packet_count}")
            print(f"total packet length: {total_length}")
            print(f"average packet interval: {total_interval / packet_count}")
            print(f"max packet interval: {max_interval}")
            print(f"min packet interval: {min_interval}")
            print(f"average packet length: {total_length / packet_count}")
            print(f"max packet length: {max_length}")
            print(f"min packet length: {min_length}")
            print(f"most common packet length: {max(set(packet_lengths), key=packet_lengths.count)}")
            print(f"label: {subfolder}")
            print()

for key, value in websites.items():
    print(f"{key}: {value}")