import modules

class NoScrollTextBrowser(modules.QTextBrowser):
    def __init__(self, parent = None) -> None:
        super().__init__(parent)

        self.setVerticalScrollBarPolicy(modules.Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(modules.Qt.ScrollBarAlwaysOff)
        self.setReadOnly(True)
        self.setTextInteractionFlags(modules.Qt.TextSelectableByMouse)
        
        self.setStyleSheet(
        f"""
        QTextBrowser {{
            border-radius: 10px;
            padding: 2px;
        }}
            
        #sender_message {{
            background-color: lightblue;
        }}
            
        #other_message {{
            background-color: white;
        }}
        """
        )
        self.setSizePolicy(modules.QSizePolicy.Fixed, modules.QSizePolicy.Fixed) 
        #self.setSizeAdjustPolicy(modules.QTextBrowser.AdjustToContents)

    def wheelEvent(self, e: modules.QWheelEvent) -> None:
        e.ignore()

    def setDocument(self, document: modules.QTextDocument, text: str) -> None:
        super().setDocument(document)

        if text:
            self.setText(text)

        font_metrix = modules.QFontMetrics(self.font())
        text_width = font_metrix.width(self.toPlainText())

        '''
        Lots of resizing happening here, but it's necessary to get the correct sizings.
        Since the source document has a different sizing, it will give incorrect dimensions
        to this text browser. We have to do resizings to get the size according to this objects
        original dimensions.
        '''
        if text_width < 600:
            self.setWordWrapMode(False)
            self.setMinimumWidth(text_width+10)
            self.setMaximumWidth(text_width+10)
        elif text_width >= 600:
            self.setMinimumWidth(600)
            self.setMaximumWidth(600)
    
    def resizeEvent(self, a0: modules.QResizeEvent) -> None:
        super().resizeEvent(a0)
        
        doc_size = self.document().size().toSize()
        
        self.setFixedHeight(doc_size.height())
        self.setFixedWidth(doc_size.width()+10)
