from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import requests
from SPARQLWrapper import SPARQLWrapper, JSON

class MyApp(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 331, 601))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_1)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 200, 321, 191))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_16 = QtWidgets.QLabel(self.groupBox_2)
        self.label_16.setGeometry(QtCore.QRect(10, 70, 71, 16))
        self.label_16.setObjectName("label_16")
        self.label_15 = QtWidgets.QLabel(self.groupBox_2)
        self.label_15.setGeometry(QtCore.QRect(100, 70, 47, 13))
        self.label_15.setObjectName("label_15")
        self.individual_button12 = QtWidgets.QPushButton(self.groupBox_2)
        self.individual_button12.setGeometry(QtCore.QRect(10, 160, 75, 23))
        self.individual_button12.setObjectName("individual_button12")
        self.property_edit_sub12 = QtWidgets.QLineEdit(self.groupBox_2)
        self.property_edit_sub12.setGeometry(QtCore.QRect(100, 90, 91, 20))
        self.property_edit_sub12.setObjectName("property_edit_sub12")
        self.property_edit12 = QtWidgets.QLineEdit(self.groupBox_2)
        self.property_edit12.setGeometry(QtCore.QRect(100, 40, 91, 20))
        self.property_edit12.setObjectName("property_edit12")
        self.individual_edit_sub12 = QtWidgets.QLineEdit(self.groupBox_2)
        self.individual_edit_sub12.setGeometry(QtCore.QRect(10, 90, 81, 20))
        self.individual_edit_sub12.setObjectName("individual_edit_sub12")
        self.label_14 = QtWidgets.QLabel(self.groupBox_2)
        self.label_14.setGeometry(QtCore.QRect(100, 20, 91, 16))
        self.label_14.setObjectName("label_14")
        self.property_button12 = QtWidgets.QPushButton(self.groupBox_2)
        self.property_button12.setGeometry(QtCore.QRect(100, 160, 91, 23))
        self.property_button12.setObjectName("property_button12")
        self.individual_edit12 = QtWidgets.QLineEdit(self.groupBox_2)
        self.individual_edit12.setGeometry(QtCore.QRect(10, 40, 81, 20))
        self.individual_edit12.setObjectName("individual_edit12")
        self.delete_property_button12 = QtWidgets.QPushButton(self.groupBox_2)
        self.delete_property_button12.setGeometry(QtCore.QRect(210, 160, 91, 23))
        self.delete_property_button12.setObjectName("delete_property_button12")
        self.label_12 = QtWidgets.QLabel(self.groupBox_2)
        self.label_12.setGeometry(QtCore.QRect(10, 20, 81, 16))
        self.label_12.setObjectName("label_12")
        self.property_edit_sub22 = QtWidgets.QLineEdit(self.groupBox_2)
        self.property_edit_sub22.setGeometry(QtCore.QRect(100, 130, 91, 20))
        self.property_edit_sub22.setObjectName("property_edit_sub22")
        self.label_17 = QtWidgets.QLabel(self.groupBox_2)
        self.label_17.setGeometry(QtCore.QRect(100, 110, 91, 16))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.groupBox_2)
        self.label_18.setGeometry(QtCore.QRect(210, 110, 91, 16))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.groupBox_2)
        self.label_19.setGeometry(QtCore.QRect(210, 70, 47, 13))
        self.label_19.setObjectName("label_19")
        self.delete_property_edit_sub12 = QtWidgets.QLineEdit(self.groupBox_2)
        self.delete_property_edit_sub12.setGeometry(QtCore.QRect(210, 90, 91, 20))
        self.delete_property_edit_sub12.setObjectName("delete_property_edit_sub12")
        self.delete_property_edit12 = QtWidgets.QLineEdit(self.groupBox_2)
        self.delete_property_edit12.setGeometry(QtCore.QRect(210, 40, 91, 20))
        self.delete_property_edit12.setObjectName("delete_property_edit12")
        self.label_20 = QtWidgets.QLabel(self.groupBox_2)
        self.label_20.setGeometry(QtCore.QRect(210, 20, 91, 16))
        self.label_20.setObjectName("label_20")
        self.delete_property_edit_sub22 = QtWidgets.QLineEdit(self.groupBox_2)
        self.delete_property_edit_sub22.setGeometry(QtCore.QRect(210, 130, 91, 20))
        self.delete_property_edit_sub22.setObjectName("delete_property_edit_sub22")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_1)
        self.groupBox_3.setGeometry(QtCore.QRect(0, 400, 321, 131))
        self.groupBox_3.setObjectName("groupBox_3")
        self.delete_class_edit = QtWidgets.QLineEdit(self.groupBox_3)
        self.delete_class_edit.setGeometry(QtCore.QRect(20, 50, 81, 20))
        self.delete_class_edit.setObjectName("delete_class_edit")
        self.label_26 = QtWidgets.QLabel(self.groupBox_3)
        self.label_26.setGeometry(QtCore.QRect(220, 30, 71, 16))
        self.label_26.setObjectName("label_26")
        self.delete_instance_button = QtWidgets.QPushButton(self.groupBox_3)
        self.delete_instance_button.setGeometry(QtCore.QRect(110, 90, 101, 23))
        self.delete_instance_button.setObjectName("delete_instance_button")
        self.delete_property_button = QtWidgets.QPushButton(self.groupBox_3)
        self.delete_property_button.setGeometry(QtCore.QRect(220, 90, 91, 23))
        self.delete_property_button.setObjectName("delete_property_button")
        self.delete_instance_edit = QtWidgets.QLineEdit(self.groupBox_3)
        self.delete_instance_edit.setGeometry(QtCore.QRect(110, 50, 101, 20))
        self.delete_instance_edit.setObjectName("delete_instance_edit")
        self.delete_class_button = QtWidgets.QPushButton(self.groupBox_3)
        self.delete_class_button.setGeometry(QtCore.QRect(20, 90, 81, 23))
        self.delete_class_button.setObjectName("delete_class_button")
        self.label_27 = QtWidgets.QLabel(self.groupBox_3)
        self.label_27.setGeometry(QtCore.QRect(110, 30, 47, 13))
        self.label_27.setObjectName("label_27")
        self.label_25 = QtWidgets.QLabel(self.groupBox_3)
        self.label_25.setGeometry(QtCore.QRect(20, 30, 71, 16))
        self.label_25.setObjectName("label_25")
        self.delete_property_edit = QtWidgets.QLineEdit(self.groupBox_3)
        self.delete_property_edit.setGeometry(QtCore.QRect(220, 50, 91, 20))
        self.delete_property_edit.setObjectName("delete_property_edit")
        self.result_label = QtWidgets.QPushButton(self.tab_1)
        self.result_label.setGeometry(QtCore.QRect(0, 540, 321, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.result_label.setFont(font)
        self.result_label.setObjectName("result_label")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_1)
        self.groupBox_4.setGeometry(QtCore.QRect(0, 10, 321, 191))
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_10 = QtWidgets.QLabel(self.groupBox_4)
        self.label_10.setGeometry(QtCore.QRect(10, 20, 71, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.groupBox_4)
        self.label_11.setGeometry(QtCore.QRect(100, 20, 91, 16))
        self.label_11.setObjectName("label_11")
        self.label_13 = QtWidgets.QLabel(self.groupBox_4)
        self.label_13.setGeometry(QtCore.QRect(210, 20, 91, 16))
        self.label_13.setObjectName("label_13")
        self.label_21 = QtWidgets.QLabel(self.groupBox_4)
        self.label_21.setGeometry(QtCore.QRect(10, 70, 71, 16))
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.groupBox_4)
        self.label_22.setGeometry(QtCore.QRect(100, 70, 47, 13))
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.groupBox_4)
        self.label_23.setGeometry(QtCore.QRect(210, 70, 71, 16))
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.groupBox_4)
        self.label_24.setGeometry(QtCore.QRect(210, 110, 71, 16))
        self.label_24.setObjectName("label_24")
        self.class_edit = QtWidgets.QLineEdit(self.groupBox_4)
        self.class_edit.setGeometry(QtCore.QRect(10, 40, 81, 20))
        self.class_edit.setObjectName("class_edit")
        self.individual_edit1 = QtWidgets.QLineEdit(self.groupBox_4)
        self.individual_edit1.setGeometry(QtCore.QRect(100, 40, 91, 20))
        self.individual_edit1.setObjectName("individual_edit1")
        self.property_edit1 = QtWidgets.QLineEdit(self.groupBox_4)
        self.property_edit1.setGeometry(QtCore.QRect(210, 40, 91, 20))
        self.property_edit1.setObjectName("property_edit1")
        self.class_edit_sub = QtWidgets.QLineEdit(self.groupBox_4)
        self.class_edit_sub.setGeometry(QtCore.QRect(10, 90, 81, 20))
        self.class_edit_sub.setObjectName("class_edit_sub")
        self.individual_edit_sub1 = QtWidgets.QLineEdit(self.groupBox_4)
        self.individual_edit_sub1.setGeometry(QtCore.QRect(100, 90, 91, 20))
        self.individual_edit_sub1.setObjectName("individual_edit_sub1")
        self.property_edit_sub1 = QtWidgets.QLineEdit(self.groupBox_4)
        self.property_edit_sub1.setGeometry(QtCore.QRect(210, 90, 91, 20))
        self.property_edit_sub1.setObjectName("property_edit_sub1")
        self.property_edit_sub2 = QtWidgets.QLineEdit(self.groupBox_4)
        self.property_edit_sub2.setGeometry(QtCore.QRect(210, 130, 91, 20))
        self.property_edit_sub2.setObjectName("property_edit_sub2")
        self.class_button = QtWidgets.QPushButton(self.groupBox_4)
        self.class_button.setGeometry(QtCore.QRect(10, 160, 75, 23))
        self.class_button.setObjectName("class_button")
        self.individual_button1 = QtWidgets.QPushButton(self.groupBox_4)
        self.individual_button1.setGeometry(QtCore.QRect(110, 160, 75, 23))
        self.individual_button1.setObjectName("individual_button1")
        self.property_button1 = QtWidgets.QPushButton(self.groupBox_4)
        self.property_button1.setGeometry(QtCore.QRect(210, 160, 75, 23))
        self.property_button1.setObjectName("property_button1")
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(10, 10, 71, 16))
        self.label.setObjectName("label")
        self.query_edit = QtWidgets.QTextEdit(self.tab_2)
        self.query_edit.setGeometry(QtCore.QRect(10, 40, 301, 481))
        self.query_edit.setObjectName("query_edit")
        self.query_button = QtWidgets.QPushButton(self.tab_2)
        self.query_button.setGeometry(QtCore.QRect(10, 540, 301, 23))
        self.query_button.setObjectName("query_button")
        self.tabWidget.addTab(self.tab_2, "")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(340, 20, 47, 13))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.result_browser = QtWidgets.QTextBrowser(self.centralwidget)
        self.result_browser.setGeometry(QtCore.QRect(340, 40, 451, 541))
        self.result_browser.setObjectName("result_browser")
        MainWindow.setCentralWidget(self.centralwidget)

        self.add_functions()

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Change"))
        self.label_16.setText(_translate("MainWindow", "New name"))
        self.label_15.setText(_translate("MainWindow", "Property"))
        self.individual_button12.setText(_translate("MainWindow", "Change name"))
        self.label_14.setText(_translate("MainWindow", "First instance"))
        self.property_button12.setText(_translate("MainWindow", "Add property"))
        self.delete_property_button12.setText(_translate("MainWindow", "Delete property"))
        self.label_12.setText(_translate("MainWindow", "Class/instance"))
        self.label_17.setText(_translate("MainWindow", "Second instance"))
        self.label_18.setText(_translate("MainWindow", "Second instance"))
        self.label_19.setText(_translate("MainWindow", "Property"))
        self.label_20.setText(_translate("MainWindow", "First instance"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Delete"))
        self.label_26.setText(_translate("MainWindow", "Property"))
        self.delete_instance_button.setText(_translate("MainWindow", "Delete instance"))
        self.delete_property_button.setText(_translate("MainWindow", "Delete property"))
        self.delete_class_button.setText(_translate("MainWindow", "Delete class"))
        self.label_27.setText(_translate("MainWindow", "Instance"))
        self.label_25.setText(_translate("MainWindow", "Class"))
        self.result_label.setText(_translate("MainWindow", "Ontology view"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Add"))
        self.label_10.setText(_translate("MainWindow", "Class"))
        self.label_11.setText(_translate("MainWindow", "Instance"))
        self.label_13.setText(_translate("MainWindow", "Property"))
        self.label_21.setText(_translate("MainWindow", "Sub class of"))
        self.label_22.setText(_translate("MainWindow", "Type"))
        self.label_23.setText(_translate("MainWindow", "Domen URI"))
        self.label_24.setText(_translate("MainWindow", "Range URI"))
        self.class_button.setText(_translate("MainWindow", "Add class"))
        self.individual_button1.setText(_translate("MainWindow", "Add instance"))
        self.property_button1.setText(_translate("MainWindow", "Add property"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "Functions"))
        self.label.setText(_translate("MainWindow", "SPARQL query"))
        self.query_button.setText(_translate("MainWindow", "Execute"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "SPARQL query"))
        self.label_2.setText(_translate("MainWindow", "Output"))

    def add_functions(self):
        self.query_button.clicked.connect(self.execute_query)
        # add class 1 stroka
        self.class_button.clicked.connect(self.add_class)
        self.individual_button1.clicked.connect(self.add_individual)
        self.individual_button12.clicked.connect(self.change_individual)
        self.property_button1.clicked.connect(self.add_propety)
        self.property_button12.clicked.connect(self.add_propety_ind)
        self.delete_property_button12.clicked.connect(self.delete_propety_ind)
        self.result_label.clicked.connect(self.show_ontology)

        self.delete_class_button.clicked.connect(self.delete_class)
        self.delete_instance_button.clicked.connect(self.delete_instance)
        self.delete_property_button.clicked.connect(self.delete_property)

    def execute_query(self):
        # Получаем SPARQL запрос из текстового поля
        query1 = self.query_edit.toPlainText()
        if query1 == "":
            self.result_browser.clear()
            self.result_browser.insertPlainText("no sparql query inserted")
            return
        query = """
                    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                    PREFIX : <http://www.semanticweb.org/user/ontologies/2023/4/bee_products_new#>
                    %s
                    """ % (query1)

        # Создаем объект SPARQLWrapper и устанавливаем адрес сервера GraphDB
        endpoint = SPARQLWrapper('http://localhost:7200/repositories/bee_prods')

        # Устанавливаем SPARQL запрос
        endpoint.setQuery(query)

        # Устанавливаем формат вывода результатов запроса
        endpoint.setReturnFormat(JSON)

        # Выполняем запрос
        results = endpoint.query().convert()

        # Очищаем поле вывода результатов
        self.result_browser.clear()

        # Выводим результаты запроса в поле вывода
        for result in results['results']['bindings']:
            for var in result:
                self.result_browser.insertPlainText(var + ': ' + result[var]['value'] + '\n')
            self.result_browser.insertPlainText('\n')

    def show_ontology(self):
        # Получаем онтологию из сервера GraphDB
        endpoint = SPARQLWrapper('http://localhost:7200/repositories/bee_prods')
        endpoint.setQuery('SELECT (strafter(str(?entity), \'#\') AS ?className) WHERE { ?entity rdf:type owl:Class}')
        endpoint.setReturnFormat(JSON)
        results = endpoint.query().convert()

        # Очищаем поле вывода результатов
        self.result_browser.clear()

        # Выводим результаты запроса в поле вывода
        self.result_browser.insertPlainText("Классы:" + '\n')
        for result in results['results']['bindings']:
            self.result_browser.insertPlainText(result['className']['value'] + ' ' + '\n')
        self.result_browser.insertPlainText('\n')

        endpoint.setQuery('SELECT (strafter(str(?entity), \'#\') AS ?individual) WHERE { ?entity rdf:type owl:NamedIndividual}')
        endpoint.setReturnFormat(JSON)
        results = endpoint.query().convert()

        # Выводим результаты запроса в поле вывода
        self.result_browser.insertPlainText("Экземпляры:" + ' \n')
        for result in results['results']['bindings']:
            self.result_browser.insertPlainText(result['individual']['value'] + ' ' + '\n')
        self.result_browser.insertPlainText('\n')

        endpoint.setQuery(
            'SELECT (strafter(str(?entity), \'#\') AS ?property) WHERE { ?entity rdf:type owl:ObjectProperty}')
        endpoint.setReturnFormat(JSON)
        results = endpoint.query().convert()

        # Выводим результаты запроса в поле вывода
        self.result_browser.insertPlainText("Связи:" + '\n')
        for result in results['results']['bindings']:
            self.result_browser.insertPlainText(result['property']['value'] + ' ' + '\n')
        self.result_browser.insertPlainText('\n')

    def add_class(self):
        # Get user input
        class_name = self.class_edit.text()
        superclass_name = self.class_edit_sub.text()

        # Check if superclass_name exists in the ontology
        query_superclass_exists = """
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            ASK {
                ?superclass a owl:Class ;
                            rdfs:label "%s" .
            }
        """ % superclass_name

        # Set up the request to check if superclass_name exists in the ontology
        url = "http://localhost:7200/repositories/bee_prods"
        headers = {"Accept": "application/sparql-results+json"}
        data = {"query": query_superclass_exists}

        # Send the request
        response = requests.post(url, headers=headers, data=data)

        # Check the response to see if superclass_name exists in the ontology
        superclass_exists = True
        if not superclass_exists and superclass_name!="":
            print("Error: superclass_name not found")
            self.result_browser.clear()
            self.result_browser.insertPlainText("Error: superclass_name not found")
            return

        # Set up the query to add the class to the ontology
        if superclass_name and superclass_exists:
            query = """
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX owl: <http://www.w3.org/2002/07/owl#>
            PREFIX : <http://www.semanticweb.org/user/ontologies/2023/4/bee_products_new#>
            INSERT DATA {
                :%s rdf:type owl:Class ;
                      rdfs:subClassOf :%s .
            }
            """ % (class_name, superclass_name)
        else:
            query = """
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX owl: <http://www.w3.org/2002/07/owl#>
            PREFIX : <http://www.semanticweb.org/user/ontologies/2023/4/bee_products_new#>
            INSERT DATA {
                :%s rdf:type owl:Class .
            }
            """ % class_name

        # Set up the request to add the class to the ontology
        url = "http://localhost:7200/repositories/bee_prods/statements"
        headers = {"Content-Type": "application/sparql-update"}
        data = query

        # Send the request
        response = requests.post(url, headers=headers, data=data)

        # Check the response
        if response.ok:
            print("Class added successfully!")
            self.result_browser.clear()
            self.result_browser.insertPlainText('Class added successfully')
        else:
            print("Error:", response.text)
            self.result_browser.clear()
            self.result_browser.insertPlainText("Error:" + response.text)

    def add_individual(self):
        # Get user input
        individual_uri = self.individual_edit1.text()
        class_uri = self.individual_edit_sub1.text()
        # Check if class_uri exists in the ontology
        check_query = f"""
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX : <http://www.semanticweb.org/user/ontologies/2023/4/bee_products_new#>

            ASK {{
                :{class_uri} rdf:type owl:Class .
            }}
            """

        url = "http://localhost:7200/repositories/bee_prods"
        headers = {"Accept": "application/sparql-results+json"}
        data = {"query": check_query}

        response = requests.post(url, headers=headers, data=data)

        # Check the response to see if superclass_name exists in the ontology
        superclass_exists = True
        if not superclass_exists:
            print("Error: class_name not found")
            self.result_browser.clear()
            self.result_browser.insertPlainText("Error: class_name not found")
            return
        # Set up the query
        query = """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX : <http://www.semanticweb.org/user/ontologies/2023/4/bee_products_new#>
        PREFIX owl: <http://www.w3.org/2002/07/owl#>

        INSERT DATA {
          :%s rdf:type :%s .
          :%s rdf:type owl:NamedIndividual .
        }
        """ % (individual_uri, class_uri,individual_uri)

        # Set up the request
        url = "http://localhost:7200/repositories/bee_prods/statements"
        headers = {"Content-Type": "application/sparql-update"}
        data = query

        # Send the request
        response = requests.post(url, headers=headers, data=data)

        # Check the response
        if response.ok:
            print("Individual added successfully!")
            self.result_browser.clear()
            self.result_browser.insertPlainText('Individual added successfully')
        else:
            print("Error:", response.text)
            self.result_browser.clear()
            self.result_browser.insertPlainText("Error:" + response.text)


    def add_propety(self):
        # Get user input
        property_uri = self.property_edit1.text()
        domain_uri = self.property_edit_sub1.text()
        range_uri = self.property_edit_sub2.text()
        # Check if class_uri exists in the ontology
        check_query = f"""
                    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                    PREFIX : <http://www.semanticweb.org/user/ontologies/2023/4/bee_products_new#>

                    ASK {{
                        :{domain_uri} rdf:type owl:Class .
                    }}
                    """

        url = "http://localhost:7200/repositories/bee_prods"
        headers = {"Accept": "application/sparql-results+json"}
        data = {"query": check_query}

        response = requests.post(url, headers=headers, data=data)

        # Check the response to see if superclass_name exists in the ontology
        superclass_exists = True
        if not superclass_exists:
            print("Error: class_name for domain not found")
            self.result_browser.clear()
            self.result_browser.insertPlainText("Error: class_name for domain not found")
            return

        # Check if class_uri exists in the ontology
        check_query1 = f"""
                PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                PREFIX : <http://www.semanticweb.org/user/ontologies/2023/4/bee_products_new#>

                ASK {{
                    :{range_uri} rdf:type owl:Class .
                }}
                """

        url = "http://localhost:7200/repositories/bee_prods"
        headers = {"Accept": "application/sparql-results+json"}
        data = {"query": check_query1}

        response = requests.post(url, headers=headers, data=data)

        # Check the response to see if superclass_name exists in the ontology
        superclass_exists = True
        if not superclass_exists:
            print("Error: class_name for range not found")
            self.result_browser.clear()
            self.result_browser.insertPlainText("Error: class_name for range not found")
            return
        # Set up the query
        query = """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX : <http://www.semanticweb.org/user/ontologies/2023/4/bee_products_new#>
        PREFIX owl: <http://www.w3.org/2002/07/owl#>

        INSERT DATA {:%s
            rdf:type owl:ObjectProperty ;
            rdfs:domain :%s ;
            rdfs:range :%s .}
        """ % (property_uri, domain_uri,range_uri)

        # Set up the request
        url = "http://localhost:7200/repositories/bee_prods/statements"
        headers = {"Content-Type": "application/sparql-update"}
        data = query

        # Send the request
        response = requests.post(url, headers=headers, data=data)

        # Check the response
        if response.ok:
            print("Property added successfully!")
            self.result_browser.clear()
            self.result_browser.insertPlainText('Property added successfully')
        else:
            print("Error:", response.text)
            self.result_browser.clear()
            self.result_browser.insertPlainText("Error:" + response.text)


    def add_propety_ind(self):
        ind_1 = self.property_edit12.text()
        property = self.property_edit_sub12.text()
        ind_2 = self.property_edit_sub22.text()
        if ind_1.__eq__(ind_2):
            print("Error: equal names")
            self.result_browser.clear()
            self.result_browser.insertPlainText("Error: equal names")
            return

        check_query = f"""
                        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                        PREFIX : <http://www.semanticweb.org/user/ontologies/2023/4/bee_products_new#>

                        ASK {{
                            :{property} rdf:type owl:ObjectProperty .
                        }}
                        """

        url = "http://localhost:7200/repositories/bee_prods"
        headers = {"Accept": "application/sparql-results+json"}
        data = {"query": check_query}

        response = requests.post(url, headers=headers, data=data)

        # Check the response to see if superclass_name exists in the ontology
        superclass_exists = True
        if not superclass_exists:
            print("Error: property not found")
            self.result_browser.clear()
            self.result_browser.insertPlainText("Error: property not found")
            return
        check_query1 = f"""
                PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                PREFIX : <http://www.semanticweb.org/user/ontologies/2023/4/bee_products_new#>

                ASK {{
                    :{ind_1} rdf:type owl:NamedIndividual .
                }}
                """

        url1 = "http://localhost:7200/repositories/bee_prods"
        headers1 = {"Accept": "application/sparql-results+json"}
        data1 = {"query": check_query1}

        response = requests.post(url1, headers=headers1, data=data1)

        # Check the response to see if superclass_name exists in the ontology
        superclass_exists1 = True
        if not superclass_exists1:
            print("Error: first individual not found")
            self.result_browser.clear()
            self.result_browser.insertPlainText("Error:first individual not found")
            return
        check_query2 = f"""
                        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                        PREFIX : <http://www.semanticweb.org/user/ontologies/2023/4/bee_products_new#>

                        ASK {{
                            :{ind_2} rdf:type owl:NamedIndividual .
                        }}
                        """
        url2 = "http://localhost:7200/repositories/bee_prods"
        headers2 = {"Accept": "application/sparql-results+json"}
        data2 = {"query": check_query2}

        response = requests.post(url2, headers=headers2, data=data2)

        # Check the response to see if superclass_name exists in the ontology
        superclass_exists2 = True
        if not superclass_exists2:
            print("Error: second individual not found")
            self.result_browser.clear()
            self.result_browser.insertPlainText("Error:second individual not found")
            return
        query = """
            PREFIX : <http://www.semanticweb.org/user/ontologies/2023/4/bee_products_new#>
            INSERT DATA {{
                :{} :{} :{}
            }}
        """.format(ind_1, property, ind_2)

        # Set up the request
        url = "http://localhost:7200/repositories/bee_prods/statements"
        headers = {"Content-Type": "application/sparql-update"}
        data = query

        # Send the request
        response = requests.post(url, headers=headers, data=data)

        # Check the response
        if response.ok:
            print("Property to individual added successfully!")
            self.result_browser.clear()
            self.result_browser.insertPlainText('Property to individual added successfully')
        else:
            print("Error:", response.text)
            self.result_browser.clear()
            self.result_browser.insertPlainText("Error:" + response.text)


    def change_individual(self):
        # Get user input
        individual_uri = "http://www.semanticweb.org/user/ontologies/2023/4/bee_products_new#" + self.individual_edit12.text()
        new_individual_uri = "http://www.semanticweb.org/user/ontologies/2023/4/bee_products_new#" + self.individual_edit_sub12.text()
        check_query = f"""
                    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                    PREFIX : <http://www.semanticweb.org/user/ontologies/2023/4/bee_products_new#>

                    ASK {{
                        <{individual_uri}> rdf:type owl:NamedIndividual .
                    }}
                    """

        url = "http://localhost:7200/repositories/bee_prods"
        headers = {"Accept": "application/sparql-results+json"}
        data = {"query": check_query}

        response = requests.post(url, headers=headers, data=data)

        # Check the response to see if superclass_name exists in the ontology
        superclass_exists = True
        check_query1 = f"""
                            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                            PREFIX : <http://www.semanticweb.org/user/ontologies/2023/4/bee_products_new#>

                            ASK {{
                                <{individual_uri}> rdf:type owl:Class .
                            }}
                            """

        url1 = "http://localhost:7200/repositories/bee_prods"
        headers1 = {"Accept": "application/sparql-results+json"}
        data1 = {"query": check_query1}

        response1 = requests.post(url1, headers=headers1, data=data1)

        # Check the response to see if superclass_name exists in the ontology
        superclass_exists1 = response1.json()['boolean']
        if not superclass_exists and not superclass_exists1:
            print("Error: object for change not found")
            self.result_browser.clear()
            self.result_browser.insertPlainText("Error: object for change not found")
            return
        query = f"""
                DELETE {{ <{individual_uri}> ?p ?o }}
                INSERT {{ <{new_individual_uri}> ?p ?o }}
                WHERE {{ <{individual_uri}> ?p ?o }}
                """

        # Set up the request
        url = "http://localhost:7200/repositories/bee_prods/statements"
        headers = {"Content-Type": "application/sparql-update"}
        data = query

        # Send the request
        response = requests.post(url, headers=headers, data=data)

        # Check the response
        if response.ok:
            print("URL of the object updated successfully!")
        else:
            print("Error:", response.text)
            self.result_browser.clear()
            self.result_browser.insertPlainText("Error:" + response.text)
        query = f"""
                DELETE {{ ?s ?p <{individual_uri}> }}
                INSERT {{ ?s ?p <{new_individual_uri}> }}
                WHERE {{ ?s ?p <{individual_uri}> }}
                """

        # Set up the request
        url = "http://localhost:7200/repositories/bee_prods/statements"
        headers = {"Content-Type": "application/sparql-update"}
        data = query

        # Send the request
        response = requests.post(url, headers=headers, data=data)

        # Check the response
        if response.ok:
            print("URL of the object and all links updated successfully!")
            self.result_browser.clear()
            self.result_browser.insertPlainText('URL of the object and all links updated successfully')
        else:
            print("Error:", response.text)
            self.result_browser.clear()
            self.result_browser.insertPlainText("Error:" + response.text)

    def delete_propety_ind(self):
        ind_1 = self.delete_property_edit12.text()
        property = self.delete_property_edit_sub12.text()
        ind_2 = self.delete_property_edit_sub22.text()
        if ind_1.__eq__(ind_2):
            print("Error: equal names")
            self.result_browser.clear()
            self.result_browser.insertPlainText("Error: equal names")
            return
        check_query = f"""
                PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                PREFIX : <http://www.semanticweb.org/user/ontologies/2023/4/bee_products_new#>

                ASK {{
                    :{property} rdf:type owl:ObjectProperty .
                }}
                """

        url = "http://localhost:7200/repositories/bee_prods"
        headers = {"Accept": "application/sparql-results+json"}
        data = {"query": check_query}

        response = requests.post(url, headers=headers, data=data)

        # Check the response to see if superclass_name exists in the ontology
        superclass_exists = True
        if not superclass_exists:
            print("Error: property not found")
            self.result_browser.clear()
            self.result_browser.insertPlainText("Error: property not found")
            return
        check_query1 = f"""
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX : <http://www.semanticweb.org/user/ontologies/2023/4/bee_products_new#>

        ASK {{
            :{ind_1} rdf:type owl:NamedIndividual .
        }}
        """

        url1 = "http://localhost:7200/repositories/bee_prods"
        headers1 = {"Accept": "application/sparql-results+json"}
        data1 = {"query": check_query1}

        response = requests.post(url1, headers=headers1, data=data1)

        # Check the response to see if superclass_name exists in the ontology
        superclass_exists1 = True
        if not superclass_exists1:
            print("Error: first individual not found")
            self.result_browser.clear()
            self.result_browser.insertPlainText("Error:first individual not found")
            return
        check_query2 = f"""
                PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                PREFIX : <http://www.semanticweb.org/user/ontologies/2023/4/bee_products_new#>

                ASK {{
                    :{ind_2} rdf:type owl:NamedIndividual .
                }}
                """
        url2 = "http://localhost:7200/repositories/bee_prods"
        headers2 = {"Accept": "application/sparql-results+json"}
        data2 = {"query": check_query2}

        response = requests.post(url2, headers=headers2, data=data2)

        # Check the response to see if superclass_name exists in the ontology
        superclass_exists2 = True
        if not superclass_exists2:
            print("Error: second individual not found")
            self.result_browser.clear()
            self.result_browser.insertPlainText("Error:second individual not found")
            return
        query = """
            PREFIX : <http://www.semanticweb.org/user/ontologies/2023/4/bee_products_new#>
            DELETE {
                    :%s :%s :%s .
                    }
            WHERE {
                    :%s :%s :%s .
                    }
        """% (ind_1, property,ind_2,ind_1, property,ind_2)

        # Set up the request
        url = "http://localhost:7200/repositories/bee_prods/statements"
        headers = {"Content-Type": "application/sparql-update"}
        data = query

        # Send the request
        response = requests.post(url, headers=headers, data=data)

        # Check the response
        if response.ok:
            print("Property to individual deleted successfully!")
            self.result_browser.clear()
            self.result_browser.insertPlainText('Property to individual deleted successfully')
        else:
            print("Error:", response.text)
            self.result_browser.clear()
            self.result_browser.insertPlainText("Error:" + response.text)

    def delete_class(self):
        # Get user input
        class_name = self.delete_class_edit.text()
        # Check if class_uri exists in the ontology
        check_query = f"""
                            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                            PREFIX : <http://www.semanticweb.org/user/ontologies/2023/4/bee_products_new#>

                            ASK {{
                                :{class_name} rdf:type owl:Class .
                            }}
                            """

        url = "http://localhost:7200/repositories/bee_prods"
        headers = {"Accept": "application/sparql-results+json"}
        data = {"query": check_query}

        response = requests.post(url, headers=headers, data=data)

        # Check the response to see if superclass_name exists in the ontology
        superclass_exists = True
        if not superclass_exists:
            print("Error: class_name not found")
            self.result_browser.clear()
            self.result_browser.insertPlainText("Error: class_name not found")
            return
        # Set up the query
        query = """
           PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
           PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
           PREFIX : <http://www.semanticweb.org/user/ontologies/2023/4/bee_products_new#>
           PREFIX owl: <http://www.w3.org/2002/07/owl#>

           DELETE WHERE {
                          ?individual a :%s .
                          ?individual ?p ?o .
                        }
           """ %class_name

        # Set up the request
        url = "http://localhost:7200/repositories/bee_prods/statements"
        headers = {"Content-Type": "application/sparql-update"}
        data = query

        # Send the request
        response = requests.post(url, headers=headers, data=data)

        # Check the response
        if response.ok:
            print("Individuals of class removed successfully!")
            self.result_browser.clear()
            self.result_browser.insertPlainText('Individuals of class removed successfully')
        else:
            print("Error:", response.text)
            self.result_browser.clear()
            self.result_browser.insertPlainText("Error:" + response.text)

        # Set up the query
        query = """
           PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
           PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
           PREFIX : <http://www.semanticweb.org/user/ontologies/2023/4/bee_products_new#>
           PREFIX owl: <http://www.w3.org/2002/07/owl#>

           DELETE WHERE {
                          :%s ?p ?o .
                        }
           """ %class_name

        # Set up the request
        url = "http://localhost:7200/repositories/bee_prods/statements"
        headers = {"Content-Type": "application/sparql-update"}
        data = query

        # Send the request
        response = requests.post(url, headers=headers, data=data)

        # Check the response
        if response.ok:
            print("Class removed successfully!")
            self.result_browser.clear()
            self.result_browser.insertPlainText('Class removed successfully')
        else:
            print("Error:", response.text)
            self.result_browser.clear()
            self.result_browser.insertPlainText("Error:" + response.text)

    def delete_instance(self):
        ind = self.delete_instance_edit.text()
            # Check if class_uri exists in the ontology
        check_query = f"""
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX : <http://www.semanticweb.org/user/ontologies/2023/4/bee_products_new#>

        ASK {{
            :{ind} rdf:type owl:NamedIndividual .
        }}
        """

        url = "http://localhost:7200/repositories/bee_prods"
        headers = {"Accept": "application/sparql-results+json"}
        data = {"query": check_query}

        response = requests.post(url, headers=headers, data=data)

        # Check the response to see if superclass_name exists in the ontology
        superclass_exists = True
        if not superclass_exists:
            print("Error: individual not found")
            self.result_browser.clear()
            self.result_browser.insertPlainText("Error: individual not found")
            return
        # Set up the query
        query = """
           PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
           PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
           PREFIX : <http://www.semanticweb.org/user/ontologies/2023/4/bee_products_new#>
           PREFIX owl: <http://www.w3.org/2002/07/owl#>
           DELETE {
                  ?s ?p ?o .
                }
                WHERE {
                  ?s rdf:type owl:NamedIndividual .
                  ?s rdfs:subClassOf* :%s .
                  ?s ?p ?o .
                }
           """ % (ind)

        # Set up the request
        url = "http://localhost:7200/repositories/bee_prods/statements"
        headers = {"Content-Type": "application/sparql-update"}
        data = query

        # Send the request
        response = requests.post(url, headers=headers, data=data)

        # Check the response
        if response.ok:
            print("Individual removed successfully!")
            self.result_browser.clear()
            self.result_browser.insertPlainText('Individual removed successfully')
        else:
            print("Error:", response.text)
            self.result_browser.clear()
            self.result_browser.insertPlainText("Error:" + response.text)


    def delete_property(self):
        property = self.delete_property_edit.text()
        # Check if class_uri exists in the ontology
        check_query = f"""
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX : <http://www.semanticweb.org/user/ontologies/2023/4/bee_products_new#>

        ASK {{
            :{property} rdf:type owl:ObjectProperty .
        }}
        """

        url = "http://localhost:7200/repositories/bee_prods"
        headers = {"Accept": "application/sparql-results+json"}
        data = {"query": check_query}

        response = requests.post(url, headers=headers, data=data)

        # Check the response to see if superclass_name exists in the ontology
        superclass_exists = True
        if not superclass_exists:
            print("Error: property not found")
            self.result_browser.clear()
            self.result_browser.insertPlainText("Error: property not found")
            return
        # Set up the query
        query = """
                   PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                   PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                   PREFIX : <http://www.semanticweb.org/user/ontologies/2023/4/bee_products_new#>
                   PREFIX owl: <http://www.w3.org/2002/07/owl#>

                   DELETE { ?s :%s ?o }
                            WHERE {
                              ?s :%s ?o .
                            };
                   """ %(property,property)

        # Set up the request
        url = "http://localhost:7200/repositories/bee_prods/statements"
        headers = {"Content-Type": "application/sparql-update"}
        data = query

        # Send the request
        response = requests.post(url, headers=headers, data=data)

        # Check the response
        if response.ok:
            print("Property removed successfully!")
            self.result_browser.clear()
            self.result_browser.insertPlainText('Property removed successfully')
        else:
            print("Error:", response.text)
            self.result_browser.clear()
            self.result_browser.insertPlainText("Error:" + response.text)
        # Set up the query
        query = """
                   PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                   PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                   PREFIX : <http://www.semanticweb.org/user/ontologies/2023/4/bee_products_new#>
                   PREFIX owl: <http://www.w3.org/2002/07/owl#>

                   DELETE {
                              ?s ?p ?o .
                            }
                            WHERE {
                              ?s rdf:type owl:ObjectProperty .
                              ?s rdfs:subClassOf* :%s .
                              ?s ?p ?o .
                            }
                   """ %property

        # Set up the request
        url = "http://localhost:7200/repositories/bee_prods/statements"
        headers = {"Content-Type": "application/sparql-update"}
        data = query

        # Send the request
        response = requests.post(url, headers=headers, data=data)

        # Check the response
        if response.ok:
            print("Property removed successfully!")
            self.result_browser.clear()
            self.result_browser.insertPlainText('Property removed successfully')
        else:
            print("Error:", response.text)
            self.result_browser.clear()
            self.result_browser.insertPlainText("Error:" + response.text)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    gui = MyApp()
    gui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())