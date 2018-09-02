import pantograph
import math
import random
import simulate

class AntCanvas(pantograph.PantographHandler):
    def setup(self):
        self.height, self.width = 1000, 100
        self.farm=simulate.AntFarm(self.height,self.width)
        self.on_mouse_down = self.test
        for x in range(self.height):
            for y in range(self.width):
                self.farm[x,y].guiObject.draw(self)
    def update(self):
        pass
    def test(self,event):
        x,y=event.x//5, event.y//5
        print(self.farm[x,y].color)


if __name__ == '__main__':
    app = pantograph.SimplePantographApplication(AntCanvas)
    app.run()
