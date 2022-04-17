import csv


class GetData:

    def get_csv_data(self):
        json_data = []
        with open("questions.csv") as csv_file:
            csv_reader = csv.reader(csv_file)
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                else:
                    question_data = {
                        'id': row[0],
                        'question': row[1],
                        'options': [row[2], row[3], row[4], row[5]],
                        'answer': row[6]
                    }
                    json_data.append(question_data)
                    line_count += 1

        return json_data

    def get_api_data(self):
        pass
