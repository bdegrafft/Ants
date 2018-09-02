import numpy as np
import pantograph
import random

class entity(object):
    def __init__(self,loc):
        self.id=id(self)
        self.loc=loc
        self.x=loc[0]
        self.y=loc[1]
        self.color=f"#{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}"
        self.guiObject=pantograph.Rect(self.x*5, self.y*5, 5, 5, fill_color = self.color, line_color = "#000")

class AntFarm():
    def __init__(self):
        self.objectRefDict={}
        self.arr = np.zeros((50, 50), dtype = np.int64)
        for x in range(50):
            for y in range(50):
                e = entity((x, y))
                self.objectRefDict[id(e)] = e
                self.arr[x, y] = id(e)
    def __getitem__(self, item):
        try:
            return self.objectRefDict[self.arr[item]]
        except:
            return KeyError