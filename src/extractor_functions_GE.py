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
		position = 9 	# if it is a 'constant angle acq' - position 5, 'stationary acq' - position 8 
		return loop_through_acq_parameters(data, n_events, position)
	except:
		return ['']

def get_total_collimation (data, n_events):
	try:
		position = 10	# if it is a 'constant angle acq' - position 6, 'stationary acq' - position 9
		return loop_through_acq_parameters(data, n_events, position)
	except:
		return ['']

def get_pitch_factor (data, n_events):
	try:
		position = 11   # if it is a 'constant angle acq' - no position	
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
		position = 0			# if it is a 'constant angle acq' - no position exists
		return loop_through_ct_doses(data, n_events, position)
	except:
		return ['']

def get_DLP (data, n_events):
	try:
		position = 2			# if it is a 'constant angle acq' - no position exists
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
		for i in range(1,n_events):
			target_region.append(data[0x0040a730][13+i][0x0040a730][1][0x0040a168][0][0x00080104].value)
		return target_region
	except:
		return ['']

def get_acquisition_protocol (data, n_events):
	try:
		acq_protocol = []
		for i in range(1,n_events):
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
	scanning_length, etc., are in 'Content 5' of dcm file. 
	Content 5 is in other larger Content x, (where x is from 14 to n_events). 
	Therefore, we need to loop through Content 5 to get all the parameters.
	'Position' indicates the number of Content in element 'Content 5'.
	If the series are topograms ("constant angle acquisition", "stationary acquisition") - 
	not all parameters will be present"""
	myList = []
	for i in range(1,n_events):
		content_length = len(data[0x0040a730][13+i][0x0040a730][4][0x0040a730].value)  
		"""parameters whose location depends on type of acquisition:
		   position  9 - single collimation, 
		   position 10 - total collimation, 
		   position 11 - pitch
		""" 
		changing_positions = [9, 10, 11]
		if content_length != 14 and position in changing_positions:    
			myList.append('')
		else:
			myList.append(data[0x0040a730][13+i][0x0040a730][4][0x0040a730][position][0x0040a300][0][0x0040a30a].value)
	return myList

	
def loop_through_xray_parameters (data, n_events, position):
	"""'CT X-Ray source parameters' are in the last content (for normal series - "Content 14"; Parameter 'length' will indicate that) of Content 5 (CT acq. parameters), 
	which is in Content (14, ..., n_events). """
	myList = []
	for i in range(1,n_events):
		length = len(data[0x0040a730][13+i][0x0040a730][4][0x0040a730].value)
		acqusition_type = data[0x0040a730][13+i][0x0040a730][2][0x0040a168][0][0x00080104].value
		one_slice_acquisitions = ['Constant Angle Acquisition', 'Stationary Acquisition']
		if acqusition_type not in one_slice_acquisitions:
			myList.append(data[0x0040a730][13+i][0x0040a730][4][0x0040a730][length-1][0x0040a730][position][0x0040a300][0][0x0040a30a].value)
		else:
			myList.append('')	
	return myList	

def loop_through_ct_doses (data, n_events, position):
	myList = []
	for i in range(1,n_events):
		acqusition_type = data[0x0040a730][13+i][0x0040a730][2][0x0040a168][0][0x00080104].value
		if acqusition_type != 'Constant Angle Acquisition': 
			myList.append(data[0x0040a730][13+i][0x0040a730][5][0x0040a730][position][0x0040a300][0][0x0040a30a].value)
		else:
			myList.append('-')
	return myList

