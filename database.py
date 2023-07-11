class Hakoniwa:
    def __init__(self, filename) -> None:
        self.__data_records:list[dict] = self.parseJSON(filename)
    @staticmethod
    def parseJSON(file):
        import json
        with open(file) as f:
            return json.load(f)
        
    def find(self, dict_find:dict) -> list[dict]:
        ret_list = []
        for data in self.__data_records:
            for diction in dict_find:
                if diction in data and dict_find[diction] == data[diction]:
                    ret_list.append(data)
        return ret_list
    def insert(self, dict_update):
        self.__data_records.append(dict_update)
        self.updateDB()
        
    def updateDB(self):
        import json
        with open("DB.json", "w") as file:
            json.dump(self.__data_records, file, indent=2)

    def update_insert(self,dict_find, dict_insert):
        matches:list[dict] = self.find(dict_find)
        for match in matches:
            match.update(dict_insert)
    
    @property
    def data_records(self):
        return self.__data_records