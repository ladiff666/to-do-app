from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
import sys
from PushButton_2 import Push_Button_
from pushButton_1 import Push_Button_1
from LineEdit import *
MainUI, _ = loadUiType(R'UIs\to_do_app.ui')
class Window(QMainWindow,MainUI) :
    def __init__(self):
        super(Window, self).__init__()
        self.setupUi(self)
        self.status = 0
        self.Add_Widgets()
        self.buttons = [self.pushButton_0,self.pushButton_1,self.pushButton_2,self.pushButton_3,self.pushButton_4
                        ,self.pushButton_5,self.pushButton_6]
        self.index = [x for x in range(0,len(self.buttons))]
        self.connect_button_with_slots()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.close_btn.clicked.connect(self.close)
        self.maximize_btn.clicked.connect(self.maximize_restore)
        self.minimize_btn.clicked.connect(self.showMinimized)
        
        def moveWindow(event):
            if self.status == 1 :
                self.maximize_restore()
            if event.buttons() == Qt.LeftButton :
                self.move(self.pos()+event.globalPos()-self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()
        self.frame_8.mouseMoveEvent = moveWindow

    def mousePressEvent(self,event):
        self.dragPos = event.globalPos()

    def maximize_restore(self):
        if self.status == 0 :
            self.showMaximized()
            self.status = 1
        else :
            self.showNormal()
            self.status = 0


    def Add_Widgets(self):
        self.pushButton_0 = Push_Button_(color_Border="#7d5294")
        self.pushButton_0.setChecked(True)
        self.pushButton_1 = Push_Button_(text='Important',text_color='#ac395d',color_Border="#ac395d"
            ,hover_active_bg='#faf2f4',hover_background='#fbf6f7',path_icon='icons\star_active.png',active_bg='#f9f3f4')
        self.pushButton_2 = Push_Button_(text='Planifié',text_color='#166f6b',color_Border='#166f6b'
            ,hover_active_bg='#f0f6f6',hover_background='#f4f5f4',path_icon='icons\calendar_active.png')
        self.pushButton_3 = Push_Button_(text='Taches',text_color='#5c70be',color_Border='#5c70be',hover_active_bg='#f1f3fa',
            hover_background='#f4f5f4',active_bg='#f4f6fb',path_icon='icons\home_active.png')
        self.pushButton_4 = Push_Button_(text='Attribué a vous-meme',text_color='#1e704d',color_Border='#1e704d'
            ,hover_active_bg='#f0f6f3',hover_background='#f1f2f4',path_icon=R'icons\user_active.png')
        self.pushButton_5 = Push_Button_(text='Prise en Main',text_color='#5c70be',color_Border='#5c70be',hover_active_bg='#f1f3fa'
           , hover_background='#f4f5f4',active_bg='#f4f6fb',path_icon='icons\waving-hand.png')
        self.pushButton_6 = Push_Button_(text='Courses',path_icon ='icons\cart.png',text_color='#586570',color_Border='#586570'
            ,hover_active_bg='#f4f6f6',hover_background='#f4f5f4',active_bg='#f4f6f6')
        self.acount_button =Push_Button_1()
        self.CustomLine = LineEdit(parent=self.frame_15,parent_=self.frame_9)
        self.horizontalLayout_7.addWidget(self.CustomLine)
        self.verticalLayout_5.setAlignment(Qt.AlignTop)
        self.verticalLayout_5.addWidget(self.pushButton_5)
        self.verticalLayout_5.addWidget(self.pushButton_6)
        self.horizontalLayout_5.addWidget(self.acount_button,Qt.AlignLeft)
        self.verticalLayout_3.addWidget(self.pushButton_0)
        self.verticalLayout_3.addWidget(self.pushButton_1)
        self.verticalLayout_3.addWidget(self.pushButton_2)
        self.verticalLayout_3.addWidget(self.pushButton_4)
        self.verticalLayout_3.addWidget(self.pushButton_3)

    def connect_button_with_slots(self):
        self.pushButton_0.clicked.connect(lambda:self.clicked_button(0))
        self.pushButton_1.clicked.connect(lambda:self.clicked_button(1))
        self.pushButton_2.clicked.connect(lambda:self.clicked_button(2))
        self.pushButton_3.clicked.connect(lambda:self.clicked_button(3))
        self.pushButton_4.clicked.connect(lambda:self.clicked_button(4))
        self.pushButton_5.clicked.connect(lambda:self.clicked_button(5))
        self.pushButton_6.clicked.connect(lambda:self.clicked_button(6))

    def clicked_button(self,index):
        for button in self.buttons:
            i = self.buttons.index(button)
            if i != index:
                button.setChecked(False)
        """if index == 1 :
            self.frame_8.setStyleSheet("background-color:#ffe4e9")
        elif index == 0 :
            self.frame_8.setStyleSheet("background-color:#f2e7f9")"""
        self.stackedWidget.setCurrentIndex(index)



if __name__ =='__main__':
    app= QApplication(sys.argv)
    window =Window()
    window.show()
    sys.exit(app.exec())
