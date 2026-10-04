#%% Task 4.1 

#Create a Python file object, i.e., a link to the file's contents
with open(file='data/raw/transshipment_vessels_20180723.csv',mode='r') as file_obj:

    #Read the entire contents into a list object
    line_list = file_obj.readlines()

#Save the contents of the first line in the list of lines to the variable "headerLineString"
header_line = line_list[0].strip()

#Print the contents of the headerLine
print(header_line)
#%% Task 4.2

#Split the headerLineString into a list of header items
header_items = header_line.split(',')

#List the index of the mmsi, shipname, and fleet_name values
mmsi_idx = header_items.index('mmsi')
name_idx = header_items.index('shipname')
fleet_idx = header_items.index('fleet_name')

#Print the values
print(mmsi_idx,name_idx,fleet_idx)
#%% Task 4.3
#Create an empty dictionary
vessel_dict = {}
#Iterate through all lines (except the header) in the data file:
for data_line in line_list[1:]:
# Split the row and extract its MMSI and fleet using the indices above.
    vessel_items = data_line.strip().split(',')
#Extract the mmsi value from the list using the mmsi_idx value
    mmsi = vessel_items[mmsi_idx]
#Extract the fleet value
    fleet = vessel_items[fleet_idx]
#Adds info to the vesselDict dictionary
    vessel_dict[mmsi] = fleet
print(len(vessel_dict))
#%% Task 4.4
vesselID = "312887000"
fleet = vessel_dict[vesselID]
print(f"Vessel # {vesselID} flies the flag of {fleet}")


#%% Task 4.5
MIN_END_LONGITUDE = 120.0
MAX_END_LONGITUDE = 135.0
MIN_START_LONGITUDE = 145.0
MAX_START_LONGITUDE = 155.0

with open(file='data/raw/loitering_events_20180723.csv', mode='r') as file_obj:
    loitering_lines = file_obj.readlines()

loitering_headers = loitering_lines[0].strip().split(",")
event_mmsi_idx = loitering_headers.index("transshipment_mmsi")
start_lat_idx = loitering_headers.index("starting_latitude")
start_lon_idx = loitering_headers.index("starting_longitude")
end_lat_idx = loitering_headers.index("ending_latitude")
end_lon_idx = loitering_headers.index("ending_longitude")

ending_band_matches = []
starting_band_matches = []
for event_line in loitering_lines[1:]:
    event_items = event_line.strip().split(",")
    mmsi = event_items[event_mmsi_idx]
    starting_latitude = float(event_items[start_lat_idx])
    starting_longitude = float(event_items[start_lon_idx])
    ending_latitude = float(event_items[end_lat_idx])
    ending_longitude = float(event_items[end_lon_idx])

    # An event crosses north over the equator if it starts south and ends north.
    crosses_equator_northward = starting_latitude < 0 < ending_latitude
    ends_in_longitude_band = MIN_END_LONGITUDE <= ending_longitude <= MAX_END_LONGITUDE
    starts_in_longitude_band = MIN_START_LONGITUDE <= starting_longitude <= MAX_START_LONGITUDE

    # Keep the two corrected result groups separate for clear output.
    if crosses_equator_northward and ends_in_longitude_band:
        fleet = vessel_dict.get(mmsi, "Unknown")
        ending_band_matches.append((mmsi, fleet))
    if crosses_equator_northward and starts_in_longitude_band:
        fleet = vessel_dict.get(mmsi, "Unknown")
        starting_band_matches.append((mmsi, fleet))

print("Crosses equator south to north; ends at 120-135 E:")
if ending_band_matches:
    for mmsi, fleet in ending_band_matches:
        print(f"Vessel #{mmsi} flies the flag of {fleet}")
else:
    print("No vessels met criteria")

print("Crosses equator south to north; starts at 145-155 E:")
if starting_band_matches:
    for mmsi, fleet in starting_band_matches:
        print(f"Vessel #{mmsi} flies the flag of {fleet}")
else:
    print("No vessels met criteria")
# %%
