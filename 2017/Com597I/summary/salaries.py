SALARIES = "salary_data.tsv"

with open(SALARIES) as salary_file:
	raw_salaries = []
	salaries = []
	salary_file.readline()
	for line in salary_file:
		line = line.strip().split('\t')
		line[-1] = float(line[-1])
		salaries.append(dict(zip(['Agency', 'JobTitle', 'Salary'], line)))
		raw_salaries.append(line[-1])
