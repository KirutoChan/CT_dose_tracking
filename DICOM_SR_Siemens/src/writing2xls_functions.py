def set_amount_of_rows(N):	
	rows = [[] for x in range(N)] # determines how many rows will be needed for one file
	for i in range(1, N):
		rows[i] = ['' for x in range(11)]   	
	return rows	

def set_auto_column_width(col):
	max_length = 0
	for cell in col:
		try: # Necessary to avoid error on empty cells
			if len(str(cell.value)) > max_length:
				max_length = len(str(cell.value))
		except:
			pass
	adjusted_width = (max_length + 2)
	return adjusted_width

def creat_rows_for_sheet1(N, extracted_data, Nr):
	rows = set_amount_of_rows(N)
	
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

	for i in range(N):
		j = 0
		for p in extracted_data['acq_protocol']:
			if p == "Topogram":
				j = j+1
			else:
				j = j
				s = extracted_data['acq_protocol'].index('Topogram')
			
				rows[i][0] = Nr
				rows[i].append(extracted_data["target_region"][j])
				rows[i].append(extracted_data["acq_protocol"][j])
				rows[i].append(extracted_data["scanning_length"][j])
				rows[i].append(extracted_data["single_collimation"][j])
				rows[i].append(extracted_data["total_collimation"][j])
				rows[i].append(extracted_data["pitch"][j])
				rows[i].append(extracted_data["KVP"][j])
				rows[i].append(extracted_data["tube_current"][j])
				rows[i].append(extracted_data["max_tube_current"][j])
				rows[i].append(extracted_data["rotation_exposure_time"][j])
				rows[i].append(extracted_data["total_exposure_time"][j])
				rows[i].append(extracted_data["CTDI"][j])
				rows[i].append(extracted_data["DLP"][j])
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

