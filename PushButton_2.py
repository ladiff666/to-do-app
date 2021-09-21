from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Push_Button_(QPushButton):
    def __init__(self,text='Ma journée',toggled=True,text_color='#7d5294',active_bg='#f5f9f7',color_background='#fff',hover_active_bg='#f7f3f8',hover_background='#f5f4f4',color_Border=None,path_icon='icons\sun_active.png'
                 ,icon_size=QSize(16,16),
                 text_alignment=Qt.AlignVCenter,*args,**kwargs):
        QPushButton.__init__(self,*args,**kwargs)
        self.color_background = color_background
        self.color_border = color_Border
        self.hover_bg = hover_background
        self.path_Icon = path_icon
        self.hover_active_bg = hover_active_bg
        self.text_alignment = text_alignment
        self.text = text
        self.a = False
        self.icon_size = icon_size
        if toggled :
            self.setCheckable(True)
        self.setChecked(False)
        self.text_color = text_color
        self.setFixedHeight(40)
        self.setMinimumWidth(120)
        self.active_bg = active_bg



    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(Qt.NoPen)
        

        rect = QRect(QPoint(0,0),QSize(self.width(),self.height()))
        content_rect = QRect(QPoint(7,5),QSize(self.width()-5,self.height()-10))
        border_rect = QRect(QPoint(5,8),QSize(self.width()-5,self.height()-16))
        text_rect = QRect(QPoint(40,5),QSize(self.width()-35,self.height()-10))

        if self.isChecked():
            if self.a: color_bg = self.hover_active_bg 
            else: color_bg= self.active_bg
            painter.setBrush(QColor(color_bg))
            painter.drawRect(rect)
            if self.color_border :
                painter.setBrush(QColor(self.color_border))
                painter.drawRect(border_rect)
            painter.setBrush(QColor(color_bg))
            painter.drawRect(content_rect)
            painter.setFont(QFont('Yu Gothic UI',11,75))
            painter.setPen(QColor(self.text_color))

        else :
            if self.a : color_bg = self.hover_bg 
            else: color_bg = self.color_background
            painter.setBrush(QColor(color_bg))
            painter.drawRect(rect)
            painter.setBrush(QColor(color_bg))
            painter.drawRect(content_rect)
            painter.setFont(QFont('Yu Gothic UI',11))
            painter.setPen(QColor('#000'))

        
        painter.drawText(text_rect,self.text_alignment,self.text)
        self.draw_icon(painter,self.icon_size,self.path_Icon)

    def enterEvent(self, a0):
        self.a = True 
    
    def leaveEvent(self, a0):
        self.a = False


    def draw_icon(self,qp, icon_size, path_icon):
        icon = QPixmap(path_icon)
        icon =icon.scaled(icon_size,Qt.KeepAspectRatio,Qt.SmoothTransformation)
        rect = QRect(QPoint(self.width()-(self.width()-12),self.height()-12-icon.height()),QSize(16,16))
        qp.drawPixmap(
            rect,
            icon
        )        
        qp.end()