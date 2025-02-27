from ui_main import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QIcon
from qasync import QEventLoop
import ui_functions 
import asyncio
import ctypes

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon(":/images/images/images/icon.png"))

        self.loop = loop or asyncio.get_event_loop()
        self.setupUi(self) # Initializes ui_main.py
        self.maximized = False # Used to check if window is maximized
        self.StackedWidget.setCurrentWidget(self.Home)
        self.btn_start.setCheckable(True)

        self.btn_open.clicked.connect(lambda: ui_functions.load_template_file(self))
        self.btn_save.clicked.connect(lambda: ui_functions.save_template_file(self))
        
        self.btn_next.clicked.connect(lambda: ui_functions.check_inputs(self))
        self.btn_start.clicked.connect(lambda: ui_functions.communicate_with_api(self))    
        self.btn_back.clicked.connect(lambda: ui_functions.button_click(self, self.btn_back))    
        self.btn_settings.clicked.connect(lambda: ui_functions.expand_settings(self))
        self.data_table.itemSelectionChanged.connect(lambda: ui_functions.items_selected(self))
        self.btn_delete_row.clicked.connect(lambda: ui_functions.delete_row(self))
        self.btn_info.clicked.connect(lambda: ui_functions.expand_about(self))
        self.box_cosine.stateChanged.connect(lambda: ui_functions.on_box_cosine_changed(self, self.box_cosine))
if __name__ == "__main__":
    app = QApplication()
    app.setStyle('Fusion')

    # Needed to make Windows use an icon for SubGPT in the taskbar
    myappid = 'SubGPT.version.1.0'  
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

    loop = QEventLoop(app) 
    asyncio.set_event_loop(loop)

    window = MainWindow()
    window.show()

    with loop:
        loop.run_forever()
