from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PushButton_2 import Push_Button_
import sys

class LineEditStyle(QProxyStyle):
    def __init__(self,icon_width,icon_height):
        QProxyStyle.__init__(self)
        self.icon_width = icon_width 
        self.icon_height = icon_height
    
    def drawPixmap_icon(self,icon_path,painter,pos=None,icon_rect=None):
        icon =QPixmap(icon_path)
        if pos:
            icon =icon.scaled(QSize(20,20),Qt.KeepAspectRatio,Qt.SmoothTransformation)
            pos.setY(int(pos.y() - icon.height()/2))
            painter.drawPixmap(pos,icon)
        else :
            painter.drawPixmap(icon_rect,icon)

    def drawRects(self,p_icon_1,p_icon_2,p_icon_3
                  ,p_icon_4,width,painter,widget,text=None):
        Xpoint = width-43
        button_rect_4 = QRect(Xpoint,0,31,51)
        Xpoint -= 31
        button_rect_3 = QRect(Xpoint,0,31,51)
        Xpoint -= 31
        button_rect_2 = QRect(Xpoint,0,31,51)
        Xpoint -= 75
        button_rect_1 = QRect(Xpoint,0,75,51)
        if widget.a == 1 :
            painter.setPen(Qt.NoPen)
            painter.setBrush(QColor(71,71,71,20))
            painter.drawRect(button_rect_1)
        elif widget.a == 2 :
            painter.setPen(Qt.NoPen)
            painter.setBrush(QColor(71,71,71,20))
            painter.drawRect(button_rect_2)
        elif widget.a == 3 :
            painter.setPen(Qt.NoPen)
            painter.setBrush(QColor(71,71,71,20))
            painter.drawRect(button_rect_3)
        elif widget.a == 4 :
            painter.setPen(Qt.NoPen)
            painter.setBrush(QColor(71,71,71,20))
            painter.drawRect(button_rect_4)
        pos_1 = QPoint(button_rect_1.center().x()-30,button_rect_1.center().y())
        self.drawPixmap_icon(p_icon_1,painter,pos=pos_1)
        pos_2 = QPoint(button_rect_2.center().x()-9,button_rect_2.center().y())
        self.drawPixmap_icon(p_icon_2,painter,pos=pos_2)
        pos_3 = QPoint(button_rect_3.center().x()-9,button_rect_3.center().y())
        self.drawPixmap_icon(p_icon_3,painter,pos=pos_3)
        pos_4 = QPoint(button_rect_4.center().x()-9,button_rect_4.center().y())
        self.drawPixmap_icon(p_icon_4,painter,pos=pos_4)
        pos_text = QPoint(button_rect_1.center().x()-5,button_rect_1.center().y()+7)
        if text :
            pen = QPen(QColor('#7d5294'))
            painter.setFont(QFont('Yu Gothic UI',11))
            painter.setPen(pen)
            painter.drawText(pos_text,text)


    def drawPrimitive(self, element, option, painter, widget=None):
        if element == QStyle.PE_PanelLineEdit:
            painter.setRenderHint(QPainter.Antialiasing)
            painter.setPen(Qt.NoPen)
            brush = QColor('#e9dbf0')
            painter.setBrush(brush)
            painter.drawRoundedRect(QRect(0,0,widget.width(),widget.height()), 7, 7)
            if not widget.text(): 
                pen = QPen(QColor('#7d5294'))
                pen.setWidth(2)
                painter.setPen(pen)
                painter.drawEllipse(QRect(13,13,23,23))
            else :
                icon_rect = QRect(13,15,20,20)
                self.drawPixmap_icon("icons\plus.png",painter,icon_rect=icon_rect)
                self.drawRects('icons\home_l.png','icons\calendar_l.png',
                               R'icons\alarm-clock.png','icons\event.png',width=widget.width(),painter=painter,widget=widget,text='Tache')
        elif element == QStyle.PE_FrameLineEdit:
            painter.setRenderHint(QPainter.Antialiasing)
            painter.setPen(Qt.NoPen)
            painter.drawRoundedRect(QRect(0,0,widget.width(),widget.height()), 7, 7)
        else:
            super().drawPrimitive(element, option, painter, widget)

    def subElementRect(self, element, option, widget=None):
        if element == QStyle.SE_LineEditContents :
            if  not widget.text():
                return QRect(self.icon_width+5,4,
                        widget.width()-self.icon_width-5,widget.height()-8)
            else :
                return QRect(self.icon_width+5,4,
                        widget.width()-self.icon_width-10-31*3-75,widget.height()-15)
        else :
            return super().subElementRect(element, option, widget)
        
class LineEdit(QLineEdit):
    clicked_ = pyqtSignal()
    def __init__(self, parent_,class_style=None,*args, **kwargs):
        QLineEdit.__init__(self,*args,**kwargs)
        self.class_style = class_style
        self.setMaximumHeight(50)
        self.setMinimumHeight(50)
        self.setMinimumWidth(474)
        self.setMouseTracking(True)
        self.parent_ = parent_
        self.a = 0
        self.b = 0
        self.setStyleSheet('color:#7d5294')
        self.style_ = LineEditStyle(icon_width=41,icon_height=41)
        self.setStyle(self.style_)
        self.setFont(QFont('Yu Gothic UI',11))
        self.Buttons_Rects()
        self.create_the_frame()
        self.clicked_.connect(self.on_clicked)

    
    def on_clicked(self):
        self.b = not self.b 
        if self.b : 
            self.f.show()
        else : 
            self.f.hide()
    
    def create_the_frame(self):
        self.f = Frame_Menu(parent=self.parent_)
        x = self.button_rect_1.x() - (self.f.width() /2 ) +40
        y = self.f.parent().height() - (self.f.height()+self.y()+self.height()+22)
        self.f.move(QPoint(x,y))
        self.f.hide()
        self.repaint()
    
    def resizeEvent(self, a0):
        if hasattr(self,"f"):
            if not self.f.isHidden() :a = 1 
            else : a = 0
            self.f.setParent(None)
        QLineEdit.resizeEvent(self,a0)
        self.Buttons_Rects()
        self.create_the_frame()
        if a :
            self.f.show()
        
    def Buttons_Rects(self):
        Xpoint = self.width()-43
        self.button_rect_4 = QRect(Xpoint,0,31,51)
        Xpoint -= 31
        self.button_rect_3 = QRect(Xpoint,0,31,51)
        Xpoint -= 31
        self.button_rect_2 = QRect(Xpoint,0,31,51)
        Xpoint -= 75
        self.button_rect_1 = QRect(Xpoint,0,75,51)
    
    def paintEvent(self, a0):
        self.Buttons_Rects()
        return super().paintEvent(a0)
    
    def mouseMoveEvent(self, event):
        QLineEdit.mouseMoveEvent(self,event)
        if self.text() :
            if self.button_rect_1.contains(event.pos()):
                self.a = 1
                self.setCursor(Qt.ArrowCursor)
            elif self.button_rect_2.contains(event.pos()):
                self.a = 2 
                self.setCursor(Qt.ArrowCursor)
            elif self.button_rect_3.contains(event.pos()):
                self.a = 3
                self.setCursor(Qt.ArrowCursor)
            elif self.button_rect_4.contains(event.pos()):
                self.a = 4
                self.setCursor(Qt.ArrowCursor)
            else :
                self.a = 0
                self.setCursor(Qt.IBeamCursor)
            self.repaint()
            if self.a != 1 : self.f.hide()


    
    def mousePressEvent(self, event):
        if self.button_rect_1.contains(event.pos()):
            self.a = 1 
            self.clicked_.emit()
        return super().mousePressEvent(event)
    
    def leaveEvent(self, a0):
        self.a = 0
        return super().leaveEvent(a0)
    


class Frame_Menu(QFrame):
    def __init__(self,parent,*args,**kwargs):
        QFrame.__init__(self,*args,**kwargs)

        self.setFixedSize(230,120)
        self.setParent(parent)
        self.setStyleSheet(" background-color : #fff;border :none ")
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0,0,0,60))
        self.setGraphicsEffect(self.shadow)
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0,0,0,0)
        
        self.Button_1 = Push_Button_(text='Taches',text_color='#5c70be',hover_active_bg='#f1f3fa',
            hover_background='#f4f5f4',active_bg='#f4f6fb',path_icon='icons\home_active.png',toggled=False)
        self.Button_2 = Push_Button_(text='Prise en Main',toggled=False,text_color='#5c70be',hover_active_bg='#f1f3fa'
           , hover_background='#f4f5f4',active_bg='#f4f6fb',path_icon='icons\waving-hand.png')
        self.Button_3 = Push_Button_(text='Courses',path_icon ='icons\cart.png',toggled=False,text_color='#586570'
            ,hover_active_bg='#f4f6f6',hover_background='#f4f5f4',active_bg='#f4f6f6')
        self.Button_1.clicked.connect(lambda:self.hide())
        self.layout.addWidget(self.Button_1)
        self.layout.addWidget(self.Button_3)
        self.layout.addWidget(self.Button_2)

