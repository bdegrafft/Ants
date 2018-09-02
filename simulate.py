import numpy as np
import pantograph

class entity(object):
    def __init__(self,loc):
        self.id=id(self)
        self.loc=loc
        self.x=loc[0]
        self.y=loc[1]
        self.color="#800"
        self.guiObject=pantograph.Rect(self.x*5, self.y*5, 5, 5, fill_color = self.color, line_color = None)

class AntFarm():
    def __init__(self,height,width):
        self.objectRefDict={}
        self.arr = np.zeros((height, width), dtype = np.int64)
        for x in range(height):
            for y in range(width):
                e = entity((x, y))
                self.objectRefDict[id(e)] = e
                self.arr[x, y] = id(e)
    def __getitem__(self, item):
        try:
            return self.objectRefDict[self.arr[item]]
        except:
            return KeyError