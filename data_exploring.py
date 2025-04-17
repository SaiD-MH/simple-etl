from number_parser import parse


class DataExploration:

    def explore_dict(container):
        for key , value in container.items():
            print(f'{key} : {type(value)}')


    def checking_missing_values(list):
        dict_stats = {}

        for record in list:
            for key , value in record.items():
                if isinstance(value , str):
                    if value == '':  #Missing or Null
                        if dict_stats.get(f'missing_{key}') == None:
                            dict_stats[f'missing_{key}'] = 1
                        else:
                            dict_stats[f'missing_{key}']+=1
                

        return dict_stats
    


    def data_cleaning(list_data):
        """  Taking list of dicts and return clean one where missing values of any key is missing"""

        list_keys = list(list_data[0].keys())
        cleaned_data = []
        for record in list_data:
            has_missing_value = False
            for key in list_keys:
                if isinstance(record[key] , str) and record[key] == '' :
                    has_missing_value = True
                    break
                
            if has_missing_value == False:
                cleaned_data.append(record)

        return cleaned_data



    def parse_english_to_numbers(text):
        
        """ Given english text represent numbers , return the interger version
            
                two -> 2
                three -> 3

        """
        year = ''
        for idx in range(0,len(text)):
            curChar = text[idx]

            if curChar == 'o':
                if idx > 0 and text[idx - 1].isdigit():
                    curChar = '0'

            elif curChar == '0':
                if idx > 0 and text[idx - 1].isalpha():
                    curChar = 'o'

            year += curChar

            text = list(text)
            text[idx]  = curChar
            text = ''.join(text)
        
        if '.' in year:
            return float(year)
        else:
            return int(parse(year))



