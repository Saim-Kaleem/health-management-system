import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import sys

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        # Add a title
        self.setWindowTitle("Hello World")
        # Set layout
        self.setLayout(qtw.QVBoxLayout())
        # Create a label
        my_label = qtw.QLabel("Pick something from the list below")
        # Change the font size of the label
        my_label.setFont(qtg.QFont('Helvetica', 18))
        self.layout().addWidget(my_label)
        # Create an combo box
        my_combo = qtw.QComboBox(self,
            editable=True,
            insertPolicy=qtw.QComboBox.InsertAtTop)
        # Add items to the combo box
        my_combo.addItem("Pepperoni", "Pepperoni")
        my_combo.addItem("Cheese", "Cheese")
        my_combo.addItem("Mushroom", "Mushroom")
        my_combo.addItem("Chicken", "Chicken")
        # Add combo box to the layout
        self.layout().addWidget(my_combo)
        # Create a button
        my_button = qtw.QPushButton("Press Me!", clicked = lambda: press_it())
        self.layout().addWidget(my_button)
        # Show the app
        self.show()
        def press_it():
            # Add name to label
            my_label.setText(f"You picked {my_combo.currentText()}!")
            # Clear the combo box
            my_combo.setCurrentIndex(0)