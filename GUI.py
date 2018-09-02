import pantograph
import math
import random
import simulate

class AntCanvas(pantograph.PantographHandler):
    def setup(self):
        self.farm=simulate.AntFarm()
        self.on_mouse_down = self.test
        self.height,self.width=100,100
        for x in range(50):
            for y in range(50):
                self.farm[x,y].guiObject.draw(self)
    def update(self):
        pass
    def test(self,event):
        x,y=event.x//5, event.y//5
        print(self.farm[x,y].color)


if __name__ == '__main__':
    app = pantograph.SimplePantographApplication(AntCanvas)
    app.run()
