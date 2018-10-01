from tkmvc.tkmvc import App

if __name__ == '__main__':
    app = App()

    bank = app.view('bank')
    bank.title('The Bank')

    app.mainloop()
