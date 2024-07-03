'''data[0x0040a730][13+i][0x0040a730][5][0x0040a730][position][0x0040a043][0][0x00080104].value  
--> name pf parameters in content 6 (CT acquisition parameters) of content '13+i' '''


def get_total_DLP (data):
	try:
		return data[0x0040a730][12][0x0040a730][1][0x0040a300][0][0x0040a30a].value
	except:
		return ['']

def get_total_exposure_time (data, n_events):
	try:
		position = 0
		return loop_through_acq_parameters(data, n_events, position)
	except:
		return ['']	

def get_scanning_length (data, n_events):
	try:
		position = 1
		return loop_through_acq_parameters(data, n_events, position)	
	except:
		return ['']	

def get_single_collimation (data, n_events):
	try:
		position = 2
		return loop_through_acq_parameters(data, n_events, position)
	except:
		return ['']

def get_total_collimation (data, n_events):
	try:
		position = 3
		return loop_through_acq_parameters(data, n_events, position)
	except:
		return ['']

def get_pitch_factor (data, n_events):
	try:
		position = 4	
		return loop_through_acq_parameters(data, n_events, position)
	except:
		return ['']

def get_KVP (data, n_events):
	try:
		inner_position = 1
		return loop_through_xray_parameters(data, n_events, inner_position)
	except:
		return ['']

def get_max_tube_current (data, n_events):
	try:
		inner_position = 2
		return loop_through_xray_parameters(data, n_events, inner_position)	
	except:
		return ['']

def get_tube_current (data, n_events):
	try:
		position = 3
		return loop_through_xray_parameters(data, n_events, position)	
	except:
		return ['']

def get_rotation_exposure_time (data, n_events):
	inner_position = 4
	return loop_through_xray_parameters(data, n_events, inner_position)	
	

def get_CTDI (data, n_events):
	try:
		position = 0
		return loop_through_ct_doses(data, n_events, position)
	except:
		return ['']

def get_DLP (data, n_events):
	try:
		position = 2
		return loop_through_ct_doses(data, n_events, position)
	except:
		return ['']

def mean_CTDI_calculator(data, n_events):
	try:
		total_CTDI = 0
		for i in get_CTDI(data, n_events):
			if type(i) != str:
				total_CTDI = total_CTDI + i
		return round(total_CTDI/(n_events-1), 2)
	except:
		return ''

def get_target_region (data, n_events):
	try:
		target_region = []
		for i in range(0,n_events):
			target_region.append(data[0x0040a730][13+i][0x0040a730][1][0x0040a168][0][0x00080104].value)
		return target_region
	except:
		return ['']

def get_acquisition_protocol (data, n_events):
	try:
		acq_protocol = []
		for i in range(0,n_events):
			acq_protocol.append(data[0x0040a730][13+i][0x0040a730][0][0x0040a160].value)
		return acq_protocol
	except:
		return ['']

def BMI_calculator(data):
	try:
		weight = data.PatientWeight
		height = data.PatientSize
		return round(weight / height ** 2, 2)	
	except:
		return ''	

def loop_through_acq_parameters (data, n_events, position):
	"""Most of "CT Acquisition parameters", such as exposure_time, 
	scanning_length, etc., are in 'Content 6' of dcm file. 
	Content 6 is in each larger Content x, (where x is from 14 to n_events). 
	Therefore, we need to loop through Content 6 to get all the parameters.
	'Position' indicates the number of Content in element 'Content 6'."""
	myList = []
	for i in range(0,n_events):
		content_length = len(data[0x0040a730][13+i][0x0040a730][5][0x0040a730].value)  # if there is no "pitch", there will be 6 elements in content 6 instead of 7 elements
		if content_length == 6 and position == 4:
			myList.append('')
		else:
			myList.append(data[0x0040a730][13+i][0x0040a730][5][0x0040a730][position][0x0040a300][0][0x0040a30a].value)
	return myList

	
def loop_through_xray_parameters (data, n_events, position):
	"""'CT X-Ray source parameters' are in Content 6 or 7 (Parameter 'length' will indicate that) of Content 6 (CT acq. parameters), 
	which is in Content (14, ..., n_events). """
	myList = []
	for i in range(0,n_events):
		length = len(data[0x0040a730][13+i][0x0040a730][5][0x0040a730].value)
		protocol_name = data[0x0040a730][13+i][0x0040a730][0][0x0040a160].value
		if protocol_name != 'Topogram':
			myList.append(data[0x0040a730][13+i][0x0040a730][5][0x0040a730][length-1][0x0040a730][position][0x0040a300][0][0x0040a30a].value)
		else:
			myList.append('')	
	return myList	

def loop_through_ct_doses (data, n_events, position):
	myList = []
	for i in range(0,n_events):
		protocol_name = data[0x0040a730][13+i][0x0040a730][0][0x0040a160].value
		if protocol_name != 'Topogram':
			myList.append(data[0x0040a730][13+i][0x0040a730][6][0x0040a730][position][0x0040a300][0][0x0040a30a].value)
		else:
			myList.append('')
	return myList
