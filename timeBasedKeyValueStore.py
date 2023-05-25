class TimeMap:

    def __init__(self):
        self.dataStruct = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dataStruct:
            self.dataStruct[key] = [(value, timestamp)]
        else:
            self.dataStruct[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        for x in self.dataStruct[key]:
            if timestamp == x[1]:
                return x[0]
        
        maxTimeStampVal = 0
        maxTimeStamp = 0
        minTimeStamp = float('inf')
        minTimeStampVal = ""

        print(self.dataStruct[key])

        for x in self.dataStruct[key]:
            if maxTimeStamp < x[1]:
                maxTimeStamp = x[1]
                maxTimeStampVal = x[0]
            if minTimeStamp > x[1]:
                minTimeStamp = x[1]
                minTimeStampVal = x[0]


        if minTimeStamp > timestamp:
            return ""

        maxTimeStampVal = 0
        maxTimeStamp = 0
        minTimeStamp = float('inf')
        minTimeStampVal = ""

        maxTimeStampVal = self.dataStruct[key][0][0]
        maxTimeStamp = self.dataStruct[key][0][1]

        for x in self.dataStruct[key]:
            if x[1] <= timestamp:
                if maxTimeStamp < x[1]:
                    maxTimeStamp = x[1]
                    maxTimeStampVal = x[0]

        return maxTimeStampVal



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)