from PySide6.QtCore import Qt, QDateTime
from PySide6.QtWidgets import QMainWindow, QPushButton, QMessageBox, QTableWidgetItem, QDialog, QDateTimeEdit
from PySide6.QtGui import QIcon

from lib.static import LOGO_FILE, LOGO_XS_FILE
from ui.compiled.ui_testing2 import Ui_MainWindow

from lib.services.server import conectar_base_datos
from ui.compiled.ui_providerInputForm import Ui_providerAdd
from ui.compiled.ui_clientInputForm import Ui_Form
from ui.compiled.ui_productInputForm import Ui_Form as Purchase
from ui.compiled.ui_distributorInputForm import Ui_Form as Distributor
from ui.compiled.ui_salesInputForm import Ui_Form as Sales
from ui.compiled.ui_loteInputForm import Ui_Form as Lote
from ui.compiled.ui_employeeInputForm import Ui_Form as Employee
from ui.compiled.ui_titleInputForm import Ui_Form as Title
from ui.compiled.ui_deptoInputForm import Ui_Form as Dpto
import mysql.connector

class Dpto_ADD(QDialog, Dpto):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Agregar Departamento")
        self.btnOk.clicked.connect(self.acceptButton)
        self.btnCancel.clicked.connect(self.close)
    
    def cancelButton(self):
        self.reject()

    def acceptButton(self):
        ayudaLista = [self.textId.toPlainText(), self.textGerente.toPlainText(), self.textDesc.toPlainText(), self.textName.toPlainText()]
        if not all(not item for item in ayudaLista):
            self.accept()
            self.close()
            return ayudaLista
        QMessageBox.warning(self, "Error", "Ingrese todos los datos")
        return

class Title_ADD(QDialog, Title):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Agregar Cargo")
        self.btnOk.clicked.connect(self.acceptButton)
        self.btnCancel.clicked.connect(self.close)
    
    def cancelButton(self):
        self.reject()

    def acceptButton(self):
        ayudaLista = [self.textId.toPlainText(), self.textDesc.toPlainText(), self.textName.toPlainText(), self.textSalary.toPlainText(), self.textTimein.toPlainText(), self.textTimeout.toPlainText()]
        if not all(not item for item in ayudaLista):
            self.accept()
            self.close()
            return ayudaLista
        QMessageBox.warning(self, "Error", "Ingrese todos los datos")
        return

class Employee_ADD(QDialog, Employee):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Agregar Empleado")
        self.btnOk.clicked.connect(self.acceptButton)
        self.btnCancel.clicked.connect(self.close)
    
    def cancelButton(self):
        self.reject()

    def acceptButton(self):
        ayudaLista = [self.textId.toPlainText(), self.textName.toPlainText(), self.textSurname.toPlainText(), self.textTel.toPlainText(), self.textTitle.toPlainText(), self.textDepartment.toPlainText(), self.textEmpl.toPlainText(), self.textSalary.toPlainText(), self.textActive.toPlainText()]
        if not all(not item for item in ayudaLista):
            self.accept()
            self.close()
            return ayudaLista
        QMessageBox.warning(self, "Error", "Ingrese todos los datos")
        return

class Lote_ADD(QDialog, Lote):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Agregar Lote")
        self.btnOk.clicked.connect(self.acceptButton)
        self.btnCancel.clicked.connect(self.close)
        self.textLoteDate.setDateTime(QDateTime.currentDateTime())
    
    def cancelButton(self):
        self.reject()

    def acceptButton(self):
        ayudaLista = [self.textId.toPlainText(), self.textPzs.toPlainText(), self.textLoteDate.dateTime().toString("yyyy-MM-dd")]
        if not all(not item for item in ayudaLista):
            self.accept()
            self.close()
            return ayudaLista
        QMessageBox.warning(self, "Error", "Ingrese todos los datos")
        return

class Sales_ADD(QDialog, Sales):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Agregar Venta")
        self.btnOk.clicked.connect(self.acceptButton)
        self.btnCancel.clicked.connect(self.close)
        self.textSaleDate.setDateTime(QDateTime.currentDateTime())
    
    def cancelButton(self):
        self.reject()

    def acceptButton(self):
        ayudaLista = [self.textId.toPlainText(), self.textClient.toPlainText(), self.textAmount.toPlainText(), self.textCost.toPlainText(),self.textSaleDate.dateTime().toString("yyyy-MM-dd"), self.textLote.toPlainText()]
        if not all(not item for item in ayudaLista):
            self.accept()
            self.close()
            return ayudaLista
        QMessageBox.warning(self, "Error", "Ingrese todos los datos")
        return

class Distributor_ADD(QDialog, Distributor):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Agregar Distribuidor")
        self.btnOk.clicked.connect(self.acceptButton)
        self.btnCancel.clicked.connect(self.close)
        self.textDate.setDateTime(QDateTime.currentDateTime())
    
    def cancelButton(self):
        self.reject()

    def acceptButton(self):
        ayudaLista = [self.textId.toPlainText(), self.textSale.toPlainText(), self.textDate.dateTime().toString("yyyy-MM-dd"), self.textNombre.toPlainText(), self.textTel.toPlainText()]
        if not all(not item for item in ayudaLista):
            self.accept()
            self.close()
            return ayudaLista
        QMessageBox.warning(self, "Error", "Ingrese todos los datos")
        return

class Purchase_ADD(QDialog, Purchase):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Agregar Compra")
        self.btnOk.clicked.connect(self.acceptButton)
        self.btnCancel.clicked.connect(self.close)
    
    def cancelButton(self):
        self.reject()

    def acceptButton(self):
        ayudaLista = [self.textId.toPlainText(), self.textProvider.toPlainText(), self.textAmount.toPlainText(), self.textCost.toPlainText(), self.textProduct.toPlainText()]
        if not all(not item for item in ayudaLista):
            self.accept()
            self.close()
            return ayudaLista
        QMessageBox.warning(self, "Error", "Ingrese todos los datos")
        return

class Material_ADD(QDialog, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Agregar Material")
        self.btnOk.clicked.connect(self.acceptButton)
        self.btnCancel.clicked.connect(self.close)
    
    def cancelButton(self):
        self.reject()

    def acceptButton(self):
        ayudaLista = [self.textId.toPlainText(), self.textProvider.toPlainText(), self.textExistence.toPlainText(), self.textLote.toPlainText(), self.textRegister.toPlainText(), self.textName.toPlainText()]
        if not all(not item for item in ayudaLista):
            self.accept()
            self.close()
            return ayudaLista
        QMessageBox.warning(self, "Error", "Ingrese todos los datos")
        return

class Provider_ADD(QDialog, Ui_providerAdd):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Agregar proveedor")
        self.btnOk.clicked.connect(self.acceptButton)
        self.btnCancel.clicked.connect(self.close)
    
    def cancelButton(self):
        self.reject()

    def acceptButton(self):
        ayudaLista = [self.textName.toPlainText(), self.textContact.toPlainText(), self.textPhone.toPlainText(), self.textEmail.toPlainText(), self.textAddres.toPlainText()]
        if not all(not item for item in ayudaLista):
            self.accept()
            self.close()
            return ayudaLista
        QMessageBox.warning(self, "Error", "Ingrese todos los datos")
        return

class MainView(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        
        # * Windows
        self.login_view = None
       
        # * Config UI
        self.setupUi(self)
        self.setWindowTitle("Plumadorchara") 
        self.setWindowIcon(QIcon(str(LOGO_FILE)))

        # * Set initial state
        self.username = None
        self.initial_state()

        # * Connect Events
        self.btnProvider.clicked.connect(lambda: self.change_main_page(self.btnProvider, 0,))
        self.btnMaterial.clicked.connect(lambda: self.change_main_page(self.btnMaterial, 1,))
        self.btnPurchase.clicked.connect(lambda: self.change_main_page(self.btnPurchase, 2,))
        self.btnDistributor.clicked.connect(lambda: self.change_main_page(self.btnDistributor, 3,))
        self.btnSales.clicked.connect(lambda: self.change_main_page(self.btnSales, 4,))
        self.btnLote.clicked.connect(lambda: self.change_main_page(self.btnLote, 5,))
        self.btnEmployee.clicked.connect(lambda: self.change_main_page(self.btnEmployee, 6,))
        self.btnTitle.clicked.connect(lambda: self.change_main_page(self.btnTitle, 7,))
        self.btnDepartment.clicked.connect(lambda: self.change_main_page(self.btnDepartment, 8,))

        self.btnClose.clicked.connect(self.close)
        self.btnLogOut.clicked.connect(self.logout)

        self.btnDeleteRow.clicked.connect(self.deleteSelected)
        self.btnUpdateRow.clicked.connect(self.updateData)
        self.btnAdd.clicked.connect(self.addNew)

    # getting of client
    def base_datos(self, table):
        conexion = conectar_base_datos()
        if conexion:
            try:
                mysqlcursor = conexion.cursor()
                mysqlcursor.execute(f"SELECT * FROM {table}")
                self.result = mysqlcursor.fetchall()
                conexion.close()
                return self.result
            except mysql.connector.Error as err:
                QMessageBox.warning(self, "Error", f"Error: {err}")
                return
    
    # query throw data
    def llenar_tablas_datos(self, tabla, QTableWidget):
        allClients = self.base_datos(tabla)
        if allClients:
            lenght = len(allClients)
            QTableWidget.setRowCount(lenght)
            fila = 0
            for item in allClients:
                for index in range(len(item)):
                    QTableWidget.setItem(fila, index, QTableWidgetItem(str(item[index])))
                fila += 1
        else:
            print(f"Error")
 
    # actions
    def deleteSelected(self):
        self.support = []
        if self.tableMaterial.selectedItems() or self.tableProvider.selectedItems() or self.tablePurchase.selectedItems() or self.tableDistributor.selectedItems() or self.tableSales.selectedItems() or self.tableLote.selectedItems() or self.tableEmployee.selectedItems() or self.tableTitle.selectedItems() or self.tableDepartment.selectedItems():
            rango = 0
            conexion = conectar_base_datos()
            if conexion:
                try:
                    mysqlcursor = conexion.cursor() 
                    current_view = self.stacked1Contenido.currentIndex()

                    # tabla de proveedores
                    if current_view == 0:
                        self.selected = self.tableProvider.selectedItems()
                        for item in self.selected:
                            self.support.insert(rango, item.text())
                            rango += 1
                        self.boxNew = QMessageBox(self)
                        self.boxNew.setWindowTitle("Advertencia!")
                        self.boxNew.setText(f"Estas apunto de borrar los datos de: {str(self.support[1])}")
                        self.boxNew.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                        button = self.boxNew.exec()
                        if button == QMessageBox.Ok:
                            sql = "DELETE FROM proveedor WHERE idProveedor = %s;"
                            mysqlcursor.execute(sql, (self.support[0],))
                            conexion.commit()
                            QMessageBox.warning(self, "Borrado!", "Dato borrado exitosamente")
                            self.llenar_tablas_datos("proveedor", self.tableProvider)

                    # tabla de materiales
                    if current_view == 1:
                        self.selected = self.tableMaterial.selectedItems()
                        for item in self.selected:
                            self.support.insert(rango, item.text())
                            rango += 1
                        self.boxNew = QMessageBox(self)
                        self.boxNew.setWindowTitle("Advertencia!")
                        self.boxNew.setText(f"Estas apunto de borrar los datos de: {str(self.support[1])}")
                        self.boxNew.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                        button = self.boxNew.exec()
                        if button == QMessageBox.Ok:
                            sql = "DELETE FROM materiales WHERE idMateriales = %s;"
                            mysqlcursor.execute(sql, (self.support[0],))
                            conexion.commit()
                            QMessageBox.warning(self, "Borrado!", "Dato borrado exitosamente")
                            self.llenar_tablas_datos("materiales", self.tableMaterial)

                    # tabla de compras
                    if current_view == 2:
                        self.selected = self.tablePurchase.selectedItems()
                        for item in self.selected:
                            self.support.insert(rango, item.text())
                            rango += 1
                        self.boxNew = QMessageBox(self)
                        self.boxNew.setWindowTitle("Advertencia!")
                        self.boxNew.setText(f"Estas apunto de borrar los datos de: {str(self.support[1])}")
                        self.boxNew.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                        button = self.boxNew.exec()
                        if button == QMessageBox.Ok:
                            sql = "DELETE FROM compra WHERE idCompra = %s;"
                            mysqlcursor.execute(sql, (self.support[0],))
                            conexion.commit()
                            QMessageBox.warning(self, "Borrado!", "Dato borrado exitosamente")
                            self.llenar_tablas_datos("compra", self.tablePurchase)

                    # tabla de distribuidores
                    if current_view == 3:
                        self.selected = self.tableDistributor.selectedItems()
                        for item in self.selected:
                            self.support.insert(rango, item.text())
                            rango += 1
                        self.boxNew = QMessageBox(self)
                        self.boxNew.setWindowTitle("Advertencia!")
                        self.boxNew.setText(f"Estas apunto de borrar los datos de: {str(self.support[1])}")
                        self.boxNew.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                        button = self.boxNew.exec()
                        if button == QMessageBox.Ok:
                            sql = "DELETE FROM distribuidores WHERE idDistribuidores = %s;"
                            mysqlcursor.execute(sql, (self.support[0],))
                            conexion.commit()
                            QMessageBox.warning(self, "Borrado!", "Dato borrado exitosamente")
                            self.llenar_tablas_datos("distribuidores", self.tableDistributor)
                    
                    # tabla de ventas
                    if current_view == 4:
                        self.selected = self.tableSales.selectedItems()
                        for item in self.selected:
                            self.support.insert(rango, item.text())
                            rango += 1
                        self.boxNew = QMessageBox(self)
                        self.boxNew.setWindowTitle("Advertencia!")
                        self.boxNew.setText(f"Estas apunto de borrar los datos de: {str(self.support[1])}")
                        self.boxNew.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                        button = self.boxNew.exec()
                        if button == QMessageBox.Ok:
                            sql = "DELETE FROM venta WHERE idVenta = %s;"
                            mysqlcursor.execute(sql, (self.support[0],))
                            conexion.commit()
                            QMessageBox.warning(self, "Borrado!", "Dato borrado exitosamente")
                            self.llenar_tablas_datos("venta", self.tableSales)
                    
                    # tabla de Lote
                    if current_view == 5:
                        self.selected = self.tableLote.selectedItems()
                        for item in self.selected:
                            self.support.insert(rango, item.text())
                            rango += 1
                        self.boxNew = QMessageBox(self)
                        self.boxNew.setWindowTitle("Advertencia!")
                        self.boxNew.setText(f"Estas apunto de borrar los datos de: {str(self.support[1])}")
                        self.boxNew.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                        button = self.boxNew.exec()
                        if button == QMessageBox.Ok:
                            sql = "DELETE FROM lote WHERE IdLote = %s;"
                            mysqlcursor.execute(sql, (self.support[0],))
                            conexion.commit()
                            QMessageBox.warning(self, "Borrado!", "Dato borrado exitosamente")
                            self.llenar_tablas_datos("lote", self.tableLote)
                    
                    # tabla de empleado
                    if current_view == 6:
                        self.selected = self.tableEmployee.selectedItems()
                        for item in self.selected:
                            self.support.insert(rango, item.text())
                            rango += 1
                        self.boxNew = QMessageBox(self)
                        self.boxNew.setWindowTitle("Advertencia!")
                        self.boxNew.setText(f"Estas apunto de borrar los datos de: {str(self.support[1])}")
                        self.boxNew.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                        button = self.boxNew.exec()
                        if button == QMessageBox.Ok:
                            sql = "DELETE FROM empleado WHERE idEmpleado = %s;"
                            mysqlcursor.execute(sql, (self.support[0],))
                            conexion.commit()
                            QMessageBox.warning(self, "Borrado!", "Dato borrado exitosamente")
                            self.llenar_tablas_datos("empleado", self.tableEmployee)
                    
                    # tabla de cargos
                    if current_view == 7:
                        self.selected = self.tableTitle.selectedItems()
                        for item in self.selected:
                            self.support.insert(rango, item.text())
                            rango += 1
                        self.boxNew = QMessageBox(self)
                        self.boxNew.setWindowTitle("Advertencia!")
                        self.boxNew.setText(f"Estas apunto de borrar los datos de: {str(self.support[1])}")
                        self.boxNew.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                        button = self.boxNew.exec()
                        if button == QMessageBox.Ok:
                            sql = "DELETE FROM cargo WHERE idCargo = %s;"
                            mysqlcursor.execute(sql, (self.support[0],))
                            conexion.commit()
                            QMessageBox.warning(self, "Borrado!", "Dato borrado exitosamente")
                            self.llenar_tablas_datos("cargo", self.tableTitle)
                    
                    # tabla de departamentos
                    if current_view == 8:
                        self.selected = self.tableDepartment.selectedItems()
                        for item in self.selected:
                            self.support.insert(rango, item.text())
                            rango += 1
                        self.boxNew = QMessageBox(self)
                        self.boxNew.setWindowTitle("Advertencia!")
                        self.boxNew.setText(f"Estas apunto de borrar los datos de: {str(self.support[1])}")
                        self.boxNew.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                        button = self.boxNew.exec()
                        if button == QMessageBox.Ok:
                            sql = "DELETE FROM departamento WHERE idDepartamento = %s;"
                            mysqlcursor.execute(sql, (self.support[0],))
                            conexion.commit()
                            QMessageBox.warning(self, "Borrado!", "Dato borrado exitosamente")
                            self.llenar_tablas_datos("departamento", self.tableDepartment)



                except mysql.connector.Error as err:
                    QMessageBox.warning(self, "Error", f"Error: {err}")
                finally:
                    conexion.close()
        else:
            QMessageBox.warning(self, "Error", "No seleccionaste ningun dato a borrar")

    def updateData(self):
        # revisar que se haya seleccionado un dato
        if self.tableProvider.selectedItems() or self.tableMaterial.selectedItems() or self.tablePurchase.selectedItems() or self.tableDistributor.selectedItems() or self.tableSales.selectedItems() or self.tableLote.selectedItems() or self.tableEmployee.selectedItems() or self.tableTitle.selectedItems() or self.tableDepartment.selectedItems():
            index = self.stacked1Contenido.currentIndex()
            support = []
            rango = 0
            # editar tabla de proveedor
            if index == 0:
                self.selected = self.tableProvider.selectedItems()
                for item in self.selected:
                    support.insert(rango, item.text())
                    rango += 1
                # compararlos con los datos de la base de datos
                conexion = conectar_base_datos()
                try:
                    mysqlconexion = conexion.cursor()
                    # hacer la consulta 
                    sql = "SELECT * FROM proveedor WHERE idProveedor = %s"
                    mysqlconexion.execute(sql, (support[0],))
                    respuesta_busqueda = mysqlconexion.fetchall()
                    # tenemos que volver el dato a entero
                    support[0] = int(support[0])
                    # comparar si se edito algun dato
                    if set(respuesta_busqueda[0]) == set(support):
                        QMessageBox.warning(self, "Error", "Ningun dato fue editado.")
                        return
                    else:
                        self.boxNew = QMessageBox(self)
                        self.boxNew.setWindowTitle("Advertencia!")
                        self.boxNew.setText(f"Estas apunto de editar los datos seleccionados a: {str(support)}")
                        self.boxNew.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                        button = self.boxNew.exec()
                        if button == QMessageBox.Ok:
                            sql = "UPDATE proveedor SET Nombre = %s, Material = %s, Telefono = %s, Email = %s WHERE idProveedor = %s;"
                            mysqlconexion.execute(sql, (support[1], support[2], support[3], support[4], support[0]))
                            conexion.commit()
                            QMessageBox.warning(self, "Actualizacion", "Datos editados exitosamente")
                            self.llenar_tablas_datos("proveedor", self.tableProvider)
                except mysql.connector.Error as err:
                    QMessageBox.warning(self, "Error", f"Error: {err}")
                finally:
                    conexion.close()

            # para la tabla materiales
            if index == 1:
                self.selected = self.tableMaterial.selectedItems()
                for item in self.selected:
                    support.insert(rango, item.text())
                    rango += 1
                # compararlos con los datos de la base de datos
                conexion = conectar_base_datos()
                try:
                    mysqlconexion = conexion.cursor()
                    # hacer la consulta 
                    sql = "SELECT * FROM materiales WHERE idMateriales = %s"
                    mysqlconexion.execute(sql, (support[0],))
                    respuesta_busqueda = mysqlconexion.fetchall()
                    # tenemos que volver el dato a entero
                    support[0] = int(support[0])
                    # comparar si se edito algun dato
                    if set(respuesta_busqueda[0]) == set(support):
                        QMessageBox.warning(self, "Error", "Ningun dato fue editado.")
                        return
                    else:
                        self.boxNew = QMessageBox(self)
                        self.boxNew.setWindowTitle("Advertencia!")
                        self.boxNew.setText(f"Estas apunto de editar los datos seleccionados a: {str(support)}")
                        self.boxNew.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                        button = self.boxNew.exec()
                        if button == QMessageBox.Ok:
                            sql = "UPDATE materiales SET Proveedor = %s, Existencia_almacen = %s, Necesario_lote = %s, Registro_Compra = %s, Nombre = %s WHERE idMateriales = %s;"
                            mysqlconexion.execute(sql, (support[1], support[2], support[3], support[4], support[5], support[0]))
                            conexion.commit()
                            QMessageBox.warning(self, "Actualizacion", "Datos editados exitosamente")
                            self.llenar_tablas_datos("materiales", self.tableMaterial)
                except mysql.connector.Error as err:
                    QMessageBox.warning(self, "Error", f"Error: {err}")
                finally:
                    conexion.close()
            
            # para la tabla compra
            if index == 2:
                self.selected = self.tablePurchase.selectedItems()
                for item in self.selected:
                    support.insert(rango, item.text())
                    rango += 1
                # compararlos con los datos de la base de datos
                conexion = conectar_base_datos()
                try:
                    mysqlconexion = conexion.cursor()
                    # hacer la consulta 
                    sql = "SELECT * FROM compra WHERE idCompra = %s"
                    mysqlconexion.execute(sql, (support[0],))
                    respuesta_busqueda = mysqlconexion.fetchall()
                    # tenemos que volver el dato a entero
                    support[0] = int(support[0])
                    # comparar si se edito algun dato
                    if set(respuesta_busqueda[0]) == set(support):
                        QMessageBox.warning(self, "Error", "Ningun dato fue editado.")
                        return
                    else:
                        self.boxNew = QMessageBox(self)
                        self.boxNew.setWindowTitle("Advertencia!")
                        self.boxNew.setText(f"Estas apunto de editar los datos seleccionados a: {str(support)}")
                        self.boxNew.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                        button = self.boxNew.exec()
                        if button == QMessageBox.Ok:
                            sql = "UPDATE compra SET Proveedor = %s, Cantidad = %s, Costo = %s, Producto = %s WHERE idCompra = %s;"
                            mysqlconexion.execute(sql, (support[1], support[2], support[3], support[4], support[0]))
                            conexion.commit()
                            QMessageBox.warning(self, "Actualizacion", "Datos editados exitosamente")
                            self.llenar_tablas_datos("compra", self.tablePurchase)
                except mysql.connector.Error as err:
                    QMessageBox.warning(self, "Error", f"Error: {err}")
                finally:
                    conexion.close()
            
            # para la tabla distribuidores
            if index == 3:
                self.selected = self.tableDistributor.selectedItems()
                for item in self.selected:
                    support.insert(rango, item.text())
                    rango += 1
                # compararlos con los datos de la base de datos
                conexion = conectar_base_datos()
                try:
                    mysqlconexion = conexion.cursor()
                    # hacer la consulta 
                    sql = "SELECT * FROM distribuidores WHERE idDistribuidores = %s"
                    mysqlconexion.execute(sql, (support[0],))
                    respuesta_busqueda = mysqlconexion.fetchall()
                    # tenemos que volver el dato a entero
                    support[0] = int(support[0])
                    # comparar si se edito algun dato
                    if set(respuesta_busqueda[0]) == set(support):
                        QMessageBox.warning(self, "Error", "Ningun dato fue editado.")
                        return
                    else:
                        self.boxNew = QMessageBox(self)
                        self.boxNew.setWindowTitle("Advertencia!")
                        self.boxNew.setText(f"Estas apunto de editar los datos seleccionados a: {str(support)}")
                        self.boxNew.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                        button = self.boxNew.exec()
                        if button == QMessageBox.Ok:
                            sql = "UPDATE distribuidores SET Venta = %s, Fecha_desde_cliente = %s, Nombre = %s, Num_Telefono = %s WHERE idDistribuidores = %s;"
                            mysqlconexion.execute(sql, (support[1], support[2], support[3], support[4], support[0]))
                            conexion.commit()
                            QMessageBox.warning(self, "Actualizacion", "Datos editados exitosamente")
                            self.llenar_tablas_datos("distribuidores", self.tableDistributor)
                except mysql.connector.Error as err:
                    QMessageBox.warning(self, "Error", f"Error: {err}")
                finally:
                    conexion.close()
            
            # para la tabla ventas
            if index == 4:
                self.selected = self.tableSales.selectedItems()
                for item in self.selected:
                    support.insert(rango, item.text())
                    rango += 1
                # compararlos con los datos de la base de datos
                conexion = conectar_base_datos()
                try:
                    mysqlconexion = conexion.cursor()
                    # hacer la consulta 
                    sql = "SELECT * FROM venta WHERE idVenta = %s"
                    mysqlconexion.execute(sql, (support[0],))
                    respuesta_busqueda = mysqlconexion.fetchall()
                    # tenemos que volver el dato a entero
                    support[0] = int(support[0])
                    # comparar si se edito algun dato
                    if set(respuesta_busqueda[0]) == set(support):
                        QMessageBox.warning(self, "Error", "Ningun dato fue editado.")
                        return
                    else:
                        self.boxNew = QMessageBox(self)
                        self.boxNew.setWindowTitle("Advertencia!")
                        self.boxNew.setText(f"Estas apunto de editar los datos seleccionados a: {str(support)}")
                        self.boxNew.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                        button = self.boxNew.exec()
                        if button == QMessageBox.Ok:
                            sql = "UPDATE venta SET Cliente = %s, Cantidad = %s, Costo = %s, Fecha_venta = %s, Lotes_vendidos = %s WHERE idVenta = %s;"
                            mysqlconexion.execute(sql, (support[1], support[2], support[3], support[4], support[5], support[0]))
                            conexion.commit()
                            QMessageBox.warning(self, "Actualizacion", "Datos editados exitosamente")
                            self.llenar_tablas_datos("venta", self.tableSales)
                except mysql.connector.Error as err:
                    QMessageBox.warning(self, "Error", f"Error: {err}")
                finally:
                    conexion.close()
            
            # para la tabla lote
            if index == 5:
                self.selected = self.tableLote.selectedItems()
                for item in self.selected:
                    support.insert(rango, item.text())
                    rango += 1
                # compararlos con los datos de la base de datos
                conexion = conectar_base_datos()
                try:
                    mysqlconexion = conexion.cursor()
                    # hacer la consulta 
                    sql = "SELECT * FROM lote WHERE IdLote = %s"
                    mysqlconexion.execute(sql, (support[0],))
                    respuesta_busqueda = mysqlconexion.fetchall()
                    # tenemos que volver el dato a entero
                    support[0] = int(support[0])
                    # comparar si se edito algun dato
                    if set(respuesta_busqueda[0]) == set(support):
                        QMessageBox.warning(self, "Error", "Ningun dato fue editado.")
                        return
                    else:
                        self.boxNew = QMessageBox(self)
                        self.boxNew.setWindowTitle("Advertencia!")
                        self.boxNew.setText(f"Estas apunto de editar los datos seleccionados a: {str(support)}")
                        self.boxNew.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                        button = self.boxNew.exec()
                        if button == QMessageBox.Ok:
                            sql = "UPDATE lote SET Cantidad_Piezas = %s, Fecha_Lote = %s WHERE IdLote = %s;"
                            mysqlconexion.execute(sql, (support[1], support[2], support[0]))
                            conexion.commit()
                            QMessageBox.warning(self, "Actualizacion", "Datos editados exitosamente")
                            self.llenar_tablas_datos("lote", self.tableLote)
                except mysql.connector.Error as err:
                    QMessageBox.warning(self, "Error", f"Error: {err}")
                finally:
                    conexion.close()
            
            # para la tabla empleado
            if index == 6:
                self.selected = self.tableEmployee.selectedItems()
                for item in self.selected:
                    support.insert(rango, item.text())
                    rango += 1
                # compararlos con los datos de la base de datos
                conexion = conectar_base_datos()
                try:
                    mysqlconexion = conexion.cursor()
                    # hacer la consulta 
                    sql = "SELECT * FROM empleado WHERE idEmpleado = %s"
                    mysqlconexion.execute(sql, (support[0],))
                    respuesta_busqueda = mysqlconexion.fetchall()
                    # tenemos que volver el dato a entero
                    support[0] = int(support[0])
                    # comparar si se edito algun dato
                    if set(respuesta_busqueda[0]) == set(support):
                        QMessageBox.warning(self, "Error", "Ningun dato fue editado.")
                        return
                    else:
                        self.boxNew = QMessageBox(self)
                        self.boxNew.setWindowTitle("Advertencia!")
                        self.boxNew.setText(f"Estas apunto de editar los datos seleccionados a: {str(support)}")
                        self.boxNew.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                        button = self.boxNew.exec()
                        if button == QMessageBox.Ok:
                            sql = "UPDATE empleado SET Nombre = %s, Apellidos = %s, Num_telefono = %s, Puesto = %s, Departamento = %s, Tiempo_Activo = %s, Sueldo = %s, Activo = %s WHERE idEmpleado = %s;"
                            mysqlconexion.execute(sql, (support[1], support[2], support[3], support[4], support[5], support[6], support[7], support[8], support[0]))
                            conexion.commit()
                            QMessageBox.warning(self, "Actualizacion", "Datos editados exitosamente")
                            self.llenar_tablas_datos("empleado", self.tableEmployee)
                except mysql.connector.Error as err:
                    QMessageBox.warning(self, "Error", f"Error: {err}")
                finally:
                    conexion.close()
            
            # para la tabla cargo
            if index == 7:
                self.selected = self.tableTitle.selectedItems()
                for item in self.selected:
                    support.insert(rango, item.text())
                    rango += 1
                # compararlos con los datos de la base de datos
                conexion = conectar_base_datos()
                try:
                    mysqlconexion = conexion.cursor()
                    # hacer la consulta 
                    sql = "SELECT * FROM cargo WHERE idCargo = %s"
                    mysqlconexion.execute(sql, (support[0],))
                    respuesta_busqueda = mysqlconexion.fetchall()
                    # tenemos que volver el dato a entero
                    support[0] = int(support[0])
                    # comparar si se edito algun dato
                    if set(respuesta_busqueda[0]) == set(support):
                        QMessageBox.warning(self, "Error", "Ningun dato fue editado.")
                        return
                    else:
                        self.boxNew = QMessageBox(self)
                        self.boxNew.setWindowTitle("Advertencia!")
                        self.boxNew.setText(f"Estas apunto de editar los datos seleccionados a: {str(support)}")
                        self.boxNew.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                        button = self.boxNew.exec()
                        if button == QMessageBox.Ok:
                            sql = "UPDATE cargo SET Descripcion = %s, Nombre = %s, Sueldo_Base = %s, Horario_Entrada = %s, Horario_Salida = %s WHERE idCargo = %s;"
                            mysqlconexion.execute(sql, (support[1], support[2], support[3], support[4], support[5], support[0]))
                            conexion.commit()
                            QMessageBox.warning(self, "Actualizacion", "Datos editados exitosamente")
                            self.llenar_tablas_datos("cargo", self.tableTitle)
                except mysql.connector.Error as err:
                    QMessageBox.warning(self, "Error", f"Error: {err}")
                finally:
                    conexion.close()
            
            # para la tabla departamento
            if index == 8:
                self.selected = self.tableDepartment.selectedItems()
                for item in self.selected:
                    support.insert(rango, item.text())
                    rango += 1
                # compararlos con los datos de la base de datos
                conexion = conectar_base_datos()
                try:
                    mysqlconexion = conexion.cursor()
                    # hacer la consulta 
                    sql = "SELECT * FROM departamento WHERE idDepartamento = %s"
                    mysqlconexion.execute(sql, (support[0],))
                    respuesta_busqueda = mysqlconexion.fetchall()
                    # tenemos que volver el dato a entero
                    support[0] = int(support[0])
                    # comparar si se edito algun dato
                    if set(respuesta_busqueda[0]) == set(support):
                        QMessageBox.warning(self, "Error", "Ningun dato fue editado.")
                        return
                    else:
                        self.boxNew = QMessageBox(self)
                        self.boxNew.setWindowTitle("Advertencia!")
                        self.boxNew.setText(f"Estas apunto de editar los datos seleccionados a: {str(support)}")
                        self.boxNew.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                        button = self.boxNew.exec()
                        if button == QMessageBox.Ok:
                            sql = "UPDATE departamento SET Gerente = %s, Descripcion = %s, Nombre = %s WHERE idDepartamento = %s;"
                            mysqlconexion.execute(sql, (support[1], support[2], support[3], support[0]))
                            conexion.commit()
                            QMessageBox.warning(self, "Actualizacion", "Datos editados exitosamente")
                            self.llenar_tablas_datos("departamento", self.tableDepartment)
                except mysql.connector.Error as err:
                    QMessageBox.warning(self, "Error", f"Error: {err}")
                finally:
                    conexion.close()
        else:
            QMessageBox.warning(self, "Error", "No hay datos a modificar")

    def addNew(self):
        conexion = conectar_base_datos()
        try:
            vista_actual = self.stacked1Contenido.currentIndex()
            mysqlconexion = conexion.cursor()
            # para la tabla de proveedores
            if vista_actual == 0:
                form = Provider_ADD()
                result = form.exec()
                if result:
                    response = form.acceptButton()
                    # se recibieron datos
                    sql = "INSERT INTO proveedor (idProveedor,Nombre,Material,Telefono,Email) VALUES(%s, %s, %s, %s, %s)"
                    values = (response[0], response[1], response[2], response[3], response[4])
                    mysqlconexion.execute(sql, values)
                    conexion.commit()
                    QMessageBox.warning(self, "Exito", "Datos agregados con exito")
                    self.llenar_tablas_datos("proveedor", self.tableProvider)
            # para la tabla de materiales
            if vista_actual == 1:
                form = Material_ADD()
                result = form.exec()
                if result:
                    response = form.acceptButton()
                    # se recibieron datos
                    sql = "INSERT INTO materiales (idMateriales,Proveedor,Existencia_almacen,Necesario_lote,Registro_Compra,Nombre) VALUES(%s, %s, %s,%s, %s, %s)"
                    values = (response[0], response[1], response[2], response[3], response[4], response[5])
                    mysqlconexion.execute(sql, values)
                    conexion.commit()
                    QMessageBox.warning(self, "Exito", "Datos agregados con exito")
                    self.llenar_tablas_datos("materiales", self.tableMaterial)
            # para la tabla de compras
            if vista_actual == 2:
                form = Purchase_ADD()
                result = form.exec()
                if result:
                    response = form.acceptButton()
                    # se recibieron datos
                    print(response)
                    sql = "INSERT INTO compra (idCompra,Proveedor,Cantidad,Costo,Producto) VALUES(%s, %s, %s, %s, %s)"
                    values = (response[0], response[1], response[2], response[3], response[4])
                    mysqlconexion.execute(sql, values)
                    conexion.commit()
                    QMessageBox.warning(self, "Exito", "Datos agregados con exito")
                    self.llenar_tablas_datos("compra", self.tablePurchase)
            # para la tabla de Distribuidores
            if vista_actual == 3:
                form = Distributor_ADD()
                result = form.exec()
                if result:
                    response = form.acceptButton()
                    # se recibieron datos
                    sql = "INSERT INTO distribuidores (idDistribuidores,Venta,Fecha_desde_cliente,Nombre,Num_Telefono) VALUES(%s, %s, %s,%s, %s)"
                    values = (response[0], response[1], response[2], response[3], response[4])
                    mysqlconexion.execute(sql, values)
                    conexion.commit()
                    QMessageBox.warning(self, "Exito", "Datos agregados con exito")
                    self.llenar_tablas_datos("distribuidores", self.tableDistributor)
            # para la tabla de ventas
            if vista_actual == 4:
                form = Sales_ADD()
                result = form.exec()
                if result:
                    response = form.acceptButton()
                    # se recibieron datos
                    print(response)
                    sql = "INSERT INTO venta (idVenta,Cliente,Cantidad,Costo,Fecha_venta,Lotes_vendidos) VALUES(%s, %s, %s, %s, %s, %s)"
                    values = (response[0], response[1], response[2], response[3], response[4], response[5])
                    mysqlconexion.execute(sql, values)
                    conexion.commit()
                    QMessageBox.warning(self, "Exito", "Datos agregados con exito")
                    self.llenar_tablas_datos("venta", self.tableSales)
            # para la tabla de Lote
            if vista_actual == 5:
                form = Lote_ADD()
                result = form.exec()
                if result:
                    response = form.acceptButton()
                    # se recibieron datos
                    sql = "INSERT INTO lote (IdLote,Cantidad_Piezas,Fecha_lote) VALUES(%s, %s, %s)"
                    values = (response[0], response[1], response[2])
                    mysqlconexion.execute(sql, values)
                    conexion.commit()
                    QMessageBox.warning(self, "Exito", "Datos agregados con exito")
                    self.llenar_tablas_datos("lote", self.tableLote)
            # para la tabla de empleados
            if vista_actual == 6:
                form = Employee_ADD()
                result = form.exec()
                if result:
                    response = form.acceptButton()
                    # se recibieron datos
                    print(response)
                    sql = "INSERT INTO empleado (idEmpleado,Nombre,Apellidos,Num_telefono,Puesto,Departamento,Tiempo_Activo,Sueldo,Activo) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                    values = (response[0], response[1], response[2], response[3], response[4], response[5], response[6], response[7], response[8])
                    mysqlconexion.execute(sql, values)
                    conexion.commit()
                    QMessageBox.warning(self, "Exito", "Datos agregados con exito")
                    self.llenar_tablas_datos("empleado", self.tableEmployee)
            # para la tabla de cargos
            if vista_actual == 7:
                form = Title_ADD()
                result = form.exec()
                if result:
                    response = form.acceptButton()
                    # se recibieron datos
                    sql = "INSERT INTO cargo (idCargo,Descripcion,Nombre,Sueldo_Base,Horario_Entrada,Horario_Salida) VALUES(%s, %s, %s, %s, %s, %s)"
                    values = (response[0], response[1], response[2], response[3], response[4], response[5])
                    mysqlconexion.execute(sql, values)
                    conexion.commit()
                    QMessageBox.warning(self, "Exito", "Datos agregados con exito")
                    self.llenar_tablas_datos("cargo", self.tableTitle)
            # para la tabla de departamentos
            if vista_actual == 8:
                form = Dpto_ADD()
                result = form.exec()
                if result:
                    response = form.acceptButton()
                    # se recibieron datos
                    print(response)
                    sql = "INSERT INTO departamento (idDepartamento,Gerente,Descripcion,Nombre) VALUES(%s, %s, %s, %s)"
                    values = (response[0], response[1], response[2], response[3])
                    mysqlconexion.execute(sql, values)
                    conexion.commit()
                    QMessageBox.warning(self, "Exito", "Datos agregados con exito")
                    self.llenar_tablas_datos("departamento", self.tableDepartment)
        except mysql.connector.Error as err:
            QMessageBox.warning(self, "Error",f"Error: {err}")
        finally:
            conexion.close()

    # valor inicial de la vista
    def initial_state(self):
        """ Set initial state for the window """
        self.lbCompany.setText("Plumadorchara")
        self.lbUser.setText(self.username if self.username is not None else "USER")
        self.stacked1Contenido.setCurrentIndex(0)
        for btn_nav in self.findChildren(QPushButton): btn_nav.setChecked(False)

        self.llenar_tablas_datos("proveedor", self.tableProvider)

    # cuando escucha que vista fue cambiada
    def change_main_page(self, pressed_btn_nav, stack1_index):
        # * Alternate state for each btnNav button
        for btn_nav in self.findChildren(QPushButton): btn_nav.setChecked(False)
        pressed_btn_nav.setChecked(True)
        # * Set active the selected page
        self.stacked1Contenido.setCurrentIndex(stack1_index)
        # load data from the first table
        if stack1_index == 0:
            self.llenar_tablas_datos("proveedor", self.tableProvider)
        if stack1_index == 1:
            self.llenar_tablas_datos("materiales", self.tableMaterial)
        if stack1_index == 2:
            self.llenar_tablas_datos("compra", self.tablePurchase)
        if stack1_index == 3:
            self.llenar_tablas_datos("distribuidores", self.tableDistributor)
        if stack1_index == 4:
            self.llenar_tablas_datos("venta", self.tableSales)
        if stack1_index == 5:
            self.llenar_tablas_datos("lote", self.tableLote)
        if stack1_index == 6:
            self.llenar_tablas_datos("empleado", self.tableEmployee)
        if stack1_index == 7:
            self.llenar_tablas_datos("cargo", self.tableTitle)
        if stack1_index == 8:
            self.llenar_tablas_datos("departamento", self.tableDepartment)

    def logout(self):
        self.login_view.initial_state()
        self.login_view.show()
        self.close()