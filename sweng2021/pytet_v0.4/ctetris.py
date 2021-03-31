from tetris import *
from matrix import *
class CTetris(Tetris):

    def deleteFullLines(self):  
        arr = self.oScreen.get_array()
        y = self.oScreen.get_dy()-Tetris.iScreenDw  
        self.line_index = 0   
        for y in range(self.oScreen.get_dy()-Tetris.iScreenDw):
            count = 0 
            for x in range(Tetris.iScreenDw, self.oScreen.get_dx()-Tetris.iScreenDw):
                count += arr[y][x]
                          
            if count == self.oScreen.get_dx()-2*Tetris.iScreenDw:
                self.tempBlk = self.iScreen.clip(self.top, self.left, self.top + self.currBlk.get_dy(), self.left + self.currBlk.get_dx())
                self.line_index = y
                self.tempBlk = self.oScreen.clip(0, Tetris.iScreenDw, self.line_index, Tetris.iScreenDw + self.iScreenDx)
                self.oScreen.paste(self.tempBlk, 1, Tetris.iScreenDw)
        
