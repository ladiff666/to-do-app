from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Push_Button_1(QPushButton):
    def __init__(self,text_bottom='0776225199',icon_text='AL',text_top='Aymen Ladiff',text_color='#647783'
                 ,color_background='#fff',hover_bg='#fafbfc',
                 text_alignment=Qt.AlignTop,icon_color='#ac395d',*args,**kwargs):
        QPushButton.__init__(self,*args,**kwargs)
        self.color_background = color_background
        self.text_alignment = text_alignment
        self.text = text_top
        self.text_bottom = text_bottom
        self.icon_text = icon_text
        self.a = False 
        self.text_color = text_color
        self.setFixedHeight(45)
        self.setMinimumWidth(120)
        self.icon_color = icon_color
        self.hover_bg = hover_bg

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing,True)
        painter.setRenderHint(QPainter.SmoothPixmapTransform)
        painter.setPen(Qt.NoPen)

        icon_rect = QRect(QPoint(10,6),QSize(27,27))
        rect = QRect(QPoint(0,0),QSize(self.width(),self.height()))
        text_rect = QRect(QPoint(45,3),QSize(self.width()-35,self.height()-10))

        if self.a: color_bg = self.hover_bg
        else: color_bg= self.color_background
        painter.setBrush(QColor(color_bg))
        painter.drawRect(rect)
        painter.setBrush(QColor(self.icon_color))
        painter.drawEllipse(icon_rect)
        painter.setFont(QFont('Yu Gothic Medium',11))
        painter.setPen(QColor('#000'))
        painter.drawText(text_rect,self.text_alignment,self.text)
        painter.setFont(QFont('Yu Gothic UI',8))
        painter.setPen(QColor('#fff'))
        painter.drawText(icon_rect,Qt.AlignCenter,self.icon_text)
        painter.setPen(QColor(self.text_color))
        painter.drawText(text_rect,Qt.AlignBottom,self.text_bottom)

        

    def enterEvent(self, a0):
        self.a = True 
    
    def leaveEvent(self, a0):
        self.a = False


