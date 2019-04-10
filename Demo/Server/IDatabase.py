import json, urllib

class IDatabase(object):

    def __init__(self, DBS = "http://127.0.0.1:50001"):
        self.DBS = DBS
        pass

    def post(self, url, data):
        data = urllib.parse.urlencode(data).encode(encoding='utf-8')
        header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko', "Content-Type": "application/x-www-form-urlencoded"}
        req = urllib.request.Request(url=url, data=data, headers=header_dict)
        res = urllib.request.urlopen(req)
        res = res.read()
        return res

    def getSensor(self, RID):
        res = self.post(self.DBS + "/server/Hardware", {"RID": RID, "Ctrl": 0})
        obj = json.loads(res)
        if obj["status"] != 0: return []
        return obj["info"]

    def getDevice(self, RID):
        res = self.post(self.DBS + "/server/Hardware", {"RID": RID, "Ctrl": 1})
        obj = json.loads(res)
        if obj["status"] != 0: return []
        return obj["info"]

    def getAllRoom(self):
        res = self.post(self.DBS+"/server/room",{})
        obj = json.loads(res)
        if obj["status"]!=0: return []
        return obj["info"]

    def getRoom(self, HID):
        res = self.post(self.DBS+"/server/room",{"HID":HID})
        obj = json.loads(res)
        if obj["status"]!=0: return []
        return obj["info"]

    def getHardware(self, HID):
        res = self.post(self.DBS + "/server/hardwareInfo", {"HID": HID})
        obj = json.loads(res)
        if obj["status"] != 0: return []
        return obj["info"]

    def getUser(self, UID):
        res = self.post(self.DBS + "/server/user", {"UID": UID})
        obj = json.loads(res)
        if obj["status"] != 0: return []
        return obj["info"]

    def checkUserHardware(self, UID, HID): return True

