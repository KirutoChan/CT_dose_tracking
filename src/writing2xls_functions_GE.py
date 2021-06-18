def set_amount_of_rows(n_events):	
	rows = [[] for x in range(n_events-1)] # determines how many rows will be needed for one file
	for i in range(1, n_events-1):
		rows[i] = ['' for x in range(11)]   
	return rows	



def creat_rows_for_sheet1(n_events, extracted_data, Nr):
	rows = set_amount_of_rows(n_events)
	
	rows[0].append(Nr)
	rows[0].append(extracted_data["patient_ID"])
	rows[0].append(extracted_data["study_description"])
	rows[0].append(extracted_data["n_events"])
	rows[0].append(extracted_data["study_date"])
	rows[0].append(extracted_data["patient_birth_date"])
	rows[0].append(extracted_data["patient_age"])
	rows[0].append(extracted_data["patient_sex"])
	rows[0].append(extracted_data["patient_size"])
	rows[0].append(extracted_data["patient_weight"])
	rows[0].append(extracted_data["BMI"])

	for i in range(n_events-1):
		rows[i].append(extracted_data["target_region"][i])
		rows[i].append(extracted_data["acq_protocol"][i])
		rows[i].append(extracted_data["scanning_length"][i])
		rows[i].append(extracted_data["single_collimation"][i])
		rows[i].append(extracted_data["total_collimation"][i])
		rows[i].append(extracted_data["pitch"][i])
		rows[i].append(extracted_data["KVP"][i])
		rows[i].append(extracted_data["tube_current"][i])
		rows[i].append(extracted_data["max_tube_current"][i])
		rows[i].append(extracted_data["rotation_exposure_time"][i])
		rows[i].append(extracted_data["total_exposure_time"][i])
		rows[i].append(extracted_data["CTDI"][i])
		rows[i].append(extracted_data["DLP"][i])
	rows[0].append(extracted_data["mean_CTDI"])
	rows[0].append(extracted_data["total_DLP"])

	return rows

def creat_rows_for_sheet2(extracted_data, Nr):
	rows = [[]]
	rows[0].append(Nr)
	rows[0].append(extracted_data["patient_ID"])
	rows[0].append(extracted_data["study_description"])
	rows[0].append(extracted_data["n_events"])
	rows[0].append(extracted_data["study_date"])
	rows[0].append(extracted_data["patient_birth_date"])
	rows[0].append(extracted_data["patient_age"])
	rows[0].append(extracted_data["patient_sex"])
	rows[0].append(extracted_data["patient_size"])
	rows[0].append(extracted_data["patient_weight"])
	rows[0].append(extracted_data["BMI"])
	rows[0].append(extracted_data["mean_CTDI"])
	rows[0].append(extracted_data["total_DLP"])

	return rows

