## PyQt5 pyuic vs loadUi

This is comparison of PyQt5 pyuic vs loadUi


<table>
<tr>
<td> Conversion? </td> <td> Outside Wrapper Class </td> <td> Inside Wrapper Class<br/>ui is loaded to self</td> <td> Inside Wrapper Class<br/>ui is loaded to self.ui</td>
</tr>
<tr>
<td> No Conversion </td>
<td>

```py
from PyQt5 import uic

w = uic.loadUi("mainwindow.ui")

w.setWindowTitle("My Title")
w.show()
```

</td>
<td>
  
```py
import sys
from PyQt5.QtWidgets import
  QMainWindow, QApplication
from PyQt5 import uic

class MainWindow(QMainWindow):

  def __init__(self, *args):
    super().__init__(*args)
    # loadUi does what setupUi does
    uic.loadUi("mainwindow.ui", self)

# sys.argv in case the app
# accepts command line arguments
app = QApplication(sys.argv)

w = MainWindow() 
w.show()
app.exec_()
```

</td>
<td>
  
NA - 2nd argument is existing widget.<br/>
Ui is loaded to self.

</td>


</tr>
<td> With Conversion </td>
<td>
NA - not commonly used
</td>
<td>

```py
import sys
from PyQt5.QtWidgets import
  QMainWindow, QApplication

from MainWindow_ui import UiMainWindow

class MainWindow(QMainWindow, Ui_MainWindow):

  def __init__(self, *args):

    super().__init__(*args)
    self.setupUi(self)
```

</td>
<td>

```py
import sys
from PyQt5.QtWidgets import
  QMainWindow, QApplication

from MainWindow_ui import UiMainWindow

class MainWindow(QMainWindow):

  def __init__(self, *args):

    super().__init__(*args)
    self.ui = UiMainWindow()
    self.ui.setupUi(self)
```

</td>
<tr>
</table>

## PySide2 pyuic vs loadUi

This is comparison of PySide2 pyuic vs loader.load

<table>
<tr>
<td> Conversion? </td> <td> Outside Wrapper Class </td> <td> Inside Wrapper Class<br/>ui is loaded to self</td> <td> Inside Wrapper Class<br/>ui is loaded to self.ui</td>
</tr>
<tr>
<td> No Conversion </td>
<td>

```py
from PySide2.QtUiTools import QUiLoader

loader = QUiLoader()

w = loader.load("mainwindow.ui", None)

w.setWindowTitle("My Title")
w.show()
```

</td>
<td>
  
NA - 2nd argument is parent widget.<br/>
Ui is NOT loaded to self. 

</td>
<td>
  
```py
import sys
from PySide2.QtWidgets import
  QMainWindow, QApplication
from PySide2.QtUiTools import QUiLoader

loader = QUiLoader()

class MainWindow(QMainWindow):

  def __init__(self, *args):
    super().__init__(*args)
    self.ui = loader.load("mainwindow.ui", None)
```

</td>


</tr>
<td> With Conversion </td>
<td>
NA - not commonly used
</td>
<td>

```py
import sys
from PySide2.QtWidgets import
  QMainWindow, QApplication

from MainWindow_ui import UiMainWindow

class MainWindow(QMainWindow, Ui_MainWindow):

  def __init__(self, *args):

    super().__init__(*args)
    self.setupUi(self)
```

</td>
<td>

```py
import sys
from PySide2.QtWidgets import
  QMainWindow, QApplication

from MainWindow_ui import UiMainWindow

class MainWindow(QMainWindow):

  def __init__(self, *args):

    super().__init__(*args)
    self.ui = UiMainWindow()
    self.ui.setupUi(self)
```

</td>
<tr>
</table>

Notes:

* In PyQt5, the second argument to `loadUi` is the *existing* widget, hence the ui is loaded into `self`. In PySide2, the second argument to `load` is the *parent* widget. However, it is commonly used like this `self.ui = loader.load("mainwindow.ui", None)`
* If `ui` is loaded thru `self` then widgets like the button are accessible like so `self.button.clicked.connect(self.button_clicked)`
* If `ui` is loaded thru `self.ui` then widgets like the button are accessible like so `self.ui.button.clicked.connect(self.button_clicked)`
* In newer Python versions,

```py
class MainWindow(QMainWindow):

  def __init__(self, *args):
    super().__init__(*args)
```
is same as

```py
class MainWindow(QMainWindow):

  def __init__(self, *args):
    super(MainWindow, self).__init__(*args)
```

provided the 1st argument to `super` is the name of the class (i.e `MainWindow`), and 2nd argument is `self`
