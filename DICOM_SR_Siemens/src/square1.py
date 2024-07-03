import pydicom as dicom
from pydicom.tag import Tag
import extractor_functions as ef
import pprint

def read_dcm(file_name):
	"""Read Dicom SR file"""
	return dicom.dcmread(file_name)

def get_data(data):
	"""Extract and format relevant data to dictionary"""
	#print (data) 
	n_events = int(data[0x0040a730][12][0x0040a730][0][0x0040a300][0][0x0040a30a].value)

	# n_events = update_n_events(uncleaned_data, n_events)

	extracted_data = {}
	extracted_data['study_description'] = data.StudyDescription
	extracted_data['acq_protocol'] = ef.get_acquisition_protocol(data, n_events)
	extracted_data['study_date'] = data.StudyDate 
	extracted_data['patient_birth_date'] = data.PatientBirthDate
	extracted_data['patient_ID'] = data.PatientID
	extracted_data['accession_number'] = data.AccessionNumber
	extracted_data['patient_age'] = data.PatientAge 
	extracted_data['patient_sex'] = data.PatientSex 

	extracted_data['patient_size'] = tryexcept(data, 'PatientSize')
	extracted_data['patient_weight'] = tryexcept(data, 'PatientWeight') 
	extracted_data['n_events'] = n_events
	extracted_data['total_DLP'] = ef.get_total_DLP(data)
	extracted_data['target_region'] = ef.get_target_region(data, n_events)
	extracted_data['total_exposure_time'] = ef.get_total_exposure_time(data, n_events)
	extracted_data['scanning_length'] = ef.get_scanning_length(data, n_events)
	extracted_data['single_collimation'] = ef.get_single_collimation(data, n_events)
	extracted_data['total_collimation'] = ef.get_total_collimation(data, n_events)
	extracted_data['pitch'] = ef.get_pitch_factor(data, n_events)
	extracted_data['KVP'] = ef.get_KVP(data, n_events)
	extracted_data['max_tube_current'] = ef.get_max_tube_current(data, n_events)
	extracted_data['tube_current'] = ef.get_tube_current(data, n_events)
	extracted_data['rotation_exposure_time'] = ef.get_rotation_exposure_time(data, n_events)
	extracted_data['CTDI'] = ef.get_CTDI(data, n_events)
	extracted_data['DLP'] = ef.get_DLP(data, n_events)
	extracted_data['BMI'] = ef.BMI_calculator(data)
	extracted_data['mean_CTDI'] = ef.mean_CTDI_calculator(data, n_events)

	return extracted_data

# info that we will need (Tags that we will use - easier way to call tags)

def tryexcept(x, parameter):
	try:
	  return x[parameter].value
	except:
	  return ""	

#my_data = read_dcm('../input/zivile.dcm')
#pp = pprint.PrettyPrinter(indent=4);
#pp.pprint (get_data(my_data))



