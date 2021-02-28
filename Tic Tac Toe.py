from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.button import Button

class TicTacToe(GridLayout):
    # to display The interface
    def __init__(self):
        super(TicTacToe, self).__init__(cols=3, spacing=2)
        self.count=0 # number of moves
        self.symbols = ('X', "O")
        self.symbolNum = 0
        self.grid = [[None for col in range(self.cols)] for row in range(self.cols)]

        for row in range(self.cols):
            for col in range(self.cols):
                tile = Button(font_size=40, on_press=self.action)
                self.grid[row][col] = tile
                self.add_widget(tile)

    def action(self, button1):
        button1.text = self.symbols[self.symbolNum]
        self.symbolNum = (self.symbolNum+1)%2
        self.count += 1
        self.checkResult()

    def checkResult(self):
        winner = self.getWinner()
        if winner:
            CloseButton = Button(text=' '+winner+' won!\nClick here to continue')
        elif self.count == (self.cols*self.cols):
            CloseButton = Button(text='Game finished\nClick here to continue')
        else:
            return
        # if there is a winner or game finished
        mypopUp = Popup(title='result of game', content=CloseButton, size_hint=(.5, .5))
        mypopUp.open()
        CloseButton.bind(on_press=mypopUp.dismiss, on_release=self.Restartgame)

    def getWinner(self):
        # check rows wise, column wise, forward diagonal wise and backward diagoanl wise

        gridValues = [[self.grid[row][col].text for col in range(self.cols)] for row in range(self.cols)]
        # check row wise
        for row in range(self.cols):
            result = self.sameSymbol(gridValues[row])
            if result:
                return result

        # check column wise
        for col in range(self.cols):
            column = [row[col] for row in gridValues]
            result = self.sameSymbol(column)
            if result:
                return result

        # check forword diagonal wise
        diag = [gridValues[i][i] for i in range(self.cols)]
        result = self.sameSymbol(diag)
        if result:
            return result
        
        # check backword diagonal wise
        diag = [gridValues[i][(self.cols-1)-i] for i in range(self.cols)]
        result = self.sameSymbol(diag)
        if result:
            return result

        return False

    def sameSymbol(self, valueList):
        symbol = valueList[0]
        for element in valueList:
            if element!=symbol:
                return False
        return symbol

    def Restartgame(self, btn):
        self.count = 0
        for row in range(self.cols):
            for col in range(self.cols):
                self.grid[row][col].text = ''

class TicTacToeApp(App):
    def build(self):
        return TicTacToe()
    
if __name__ == "__main__":
    TicTacToeApp().run()