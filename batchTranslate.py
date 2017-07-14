# Translating a CSV list of words from English to another language
# with Yandex.translate API

import json, requests, csv

# Some important variables
apiEndP = "https://translate.yandex.net/api/v1.5/tr.json/translate?key="
apiKey = "YOUR-API-KEY-HERE"
newfilecontents = []

# Reading and saving words from original file.
with open('mostCommonWords.csv', newline='') as csvFile :
	reader = csv.reader(csvFile)
	for row in reader:
		newfilecontents.append([row[0],""])

# Making a single request URL with all English words.
giant_text_str = ""
for line in newfilecontents:
	giant_text_str = giant_text_str + "&text=" + line[0]
apiUrl = apiEndP + apiKey + giant_text_str + "&lang=en-nl"

# Making the API request and getting the JSON result.
apiresponse = requests.get(apiUrl)
jsonresult = json.loads(apiresponse.text)

# Iterating through the JSON result and adding to array.
for index, response in enumerate(jsonresult['text']):
	newfilecontents[index][1] = response

# Printing the final array.
with open('mostCommonWords.csv', 'w', newline='') as csvFile :
	writer = csv.writer(csvFile)
	writer.writerows(newfilecontents)

# ~ fin
print('Finished.')
