from tkmvc.tkmvc import App

if __name__ == '__main__':
    app = App()

    root = app.view('root')
    root.title('The Bank')

    app.mainloop()
