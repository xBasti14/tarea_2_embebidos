from PyQt5 import QtCore, QtGui, QtWidgets
import serial
import serial.tools.list_ports
from struct import pack,unpack
import time


dic = {
	"BMI270": {
		"acc": {
			"+/- 2g": 0b00000000,
			"+/- 4g": 0b00000001,
			"+/- 8g": 0b00000010,
			"+/- 16g": 0b00000011,
			"25/32": 0b10100001,
			"25/16": 0b10100010,
			"25/8": 0b10100011,
			"25/4": 0b10100100,
			"25/2": 0b10100101,
			"25": 0b1010010,
			"50": 0b10100111,
			"100": 0b10101000,
			"200": 0b10101001,
			"400": 0b10101010,
			"800": 0b10101011,
			"1600": 0b10101100,
		},
		"gy": {
			"+/- 2000 dps, 16.4 LSB/dps": 0b00000000,
			"+/- 1000 dps, 32.8 LSB/dps": 0b00000001,
			"+/- 500 dps, 65.6 LSB/dps": 0b00000010,
			"+/- 250 dps, 131.2 LSB/dps": 0b00000011,
			"+/- 125 dps, 262.4 LSB/dps": 0b00000100,
			"25": 0b10100110,
			"50": 0b10100111,
			"100": 0b10101000,
			"200": 0b10101001,
			"400": 0b10101010,
			"800": 0b10101011,
			"1600": 0b10101100,
			"3200": 0b10101101,
		},
	}
}

class Ui_Dialog(object):
	def clicked(self):
		sensor = self.selec_12.currentData(0)
		if(sensor != "<Ninguno>"):
			mode = self.selec_13.currentData(0)
			frecuencia_muestreo_acc = dic[sensor]["acc"][self.selec_14.currentData(0)]
			sensibilidad_acc = dic[sensor]["acc"][self.selec_15.currentData(0)]
			sensibilidad_gy = dic[sensor]["gy"][self.selec_16.currentData(0)]
			frecuencia_muestreo_gy = dic[sensor]["gy"][self.selec_17.currentData(0)]

			sensor_config = 0 if sensor=="BMI270" else 1

			ser = serial.Serial('COM3', 115200, timeout=1)

			ser.write(pack('BBBBB',
				sensor_config,
				frecuencia_muestreo_acc,
				sensibilidad_acc,
				sensibilidad_gy,
				frecuencia_muestreo_gy
				) + b"#")

			print("Data enviada")

			while True:
				try:
					msg = ser.read_until(b"#")
					msg = msg[:-1]

					msg = msg.decode()
					print(msg)
					status = int(msg.replace("STATUS", ""))
					if status == 200:
						break
				except:
					time.sleep(0.5)
			print("Configuración completa")
			
			while(True):
				try:
					msg = ser.read(39)
					data = unpack("39B", msg)
					print(data)
				except:
					continue

			ser.close()

		else: print("Selecciona un sensor")

	def setupUi(self, Dialog):
		Dialog.setObjectName("Dialog")
		Dialog.resize(774, 836)
		self.label_30 = QtWidgets.QLabel(Dialog)
		self.label_30.setGeometry(QtCore.QRect(350, 130, 101, 21))
		self.label_30.setStyleSheet("color: rgb(0, 0, 0);\n"
"\n"
"")
		self.label_30.setObjectName("label_30")
		self.progressBar = QtWidgets.QProgressBar(Dialog)
		self.progressBar.setGeometry(QtCore.QRect(460, 130, 118, 23))
		self.progressBar.setProperty("value", 0)
		self.progressBar.setObjectName("progressBar")
		self.selec_12 = QtWidgets.QComboBox(Dialog)
		self.selec_12.setGeometry(QtCore.QRect(350, 160, 181, 31))
		self.selec_12.setStyleSheet("background-color: rgb(255, 255, 255);")
		self.selec_12.setObjectName("selec_12")
		self.selec_12.addItem("")
		self.selec_12.addItem("")
		self.selec_12.addItem("")
		self.label_9 = QtWidgets.QLabel(Dialog)
		self.label_9.setGeometry(QtCore.QRect(120, 180, 81, 31))
		self.label_9.setObjectName("label_9")
		self.label_7 = QtWidgets.QLabel(Dialog)
		self.label_7.setGeometry(QtCore.QRect(120, 130, 81, 31))
		self.label_7.setObjectName("label_7")
		self.label_2 = QtWidgets.QLabel(Dialog)
		self.label_2.setGeometry(QtCore.QRect(350, 40, 71, 41))
		self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
		self.label_2.setFrameShape(QtWidgets.QFrame.Box)
		self.label_2.setAlignment(QtCore.Qt.AlignCenter)
		self.label_2.setObjectName("label_2")
		self.selec_13 = QtWidgets.QComboBox(Dialog)
		self.selec_13.setGeometry(QtCore.QRect(360, 300, 181, 31))
		self.selec_13.setStyleSheet("background-color: rgb(255, 255, 255);")
		self.selec_13.setObjectName("selec_13")
		self.selec_13.addItem("")
		self.selec_13.addItem("")
		self.label_31 = QtWidgets.QLabel(Dialog)
		self.label_31.setGeometry(QtCore.QRect(390, 270, 121, 21))
		self.label_31.setStyleSheet("color: rgb(0, 0, 0);\n"
"\n"
"")
		self.label_31.setObjectName("label_31")
		self.label_32 = QtWidgets.QLabel(Dialog)
		self.label_32.setGeometry(QtCore.QRect(170, 100, 121, 21))
		self.label_32.setStyleSheet("color: rgb(0, 0, 0);\n"
"\n"
"")
		self.label_32.setObjectName("label_32")
		self.label_33 = QtWidgets.QLabel(Dialog)
		self.label_33.setGeometry(QtCore.QRect(170, 220, 121, 21))
		self.label_33.setStyleSheet("color: rgb(0, 0, 0);\n"
"\n"
"")
		self.label_33.setObjectName("label_33")
		self.label_8 = QtWidgets.QLabel(Dialog)
		self.label_8.setGeometry(QtCore.QRect(120, 250, 81, 31))
		self.label_8.setObjectName("label_8")
		self.label_10 = QtWidgets.QLabel(Dialog)
		self.label_10.setGeometry(QtCore.QRect(120, 300, 81, 31))
		self.label_10.setObjectName("label_10")
		self.Plot1 = QtWidgets.QGraphicsView(Dialog)
		self.Plot1.setGeometry(QtCore.QRect(60, 420, 291, 181))
		self.Plot1.setFrameShape(QtWidgets.QFrame.Box)
		self.Plot1.setFrameShadow(QtWidgets.QFrame.Plain)
		self.Plot1.setObjectName("Plot1")
		self.Plot2 = QtWidgets.QGraphicsView(Dialog)
		self.Plot2.setGeometry(QtCore.QRect(390, 420, 291, 181))
		self.Plot2.setFrameShape(QtWidgets.QFrame.Box)
		self.Plot2.setFrameShadow(QtWidgets.QFrame.Plain)
		self.Plot2.setObjectName("Plot2")
		self.Plot3 = QtWidgets.QGraphicsView(Dialog)
		self.Plot3.setGeometry(QtCore.QRect(60, 640, 291, 181))
		self.Plot3.setFrameShape(QtWidgets.QFrame.Box)
		self.Plot3.setFrameShadow(QtWidgets.QFrame.Plain)
		self.Plot3.setObjectName("Plot3")
		self.Plot4 = QtWidgets.QGraphicsView(Dialog)
		self.Plot4.setGeometry(QtCore.QRect(390, 640, 291, 181))
		self.Plot4.setFrameShape(QtWidgets.QFrame.Box)
		self.Plot4.setFrameShadow(QtWidgets.QFrame.Plain)
		self.Plot4.setObjectName("Plot4")
		self.label_3 = QtWidgets.QLabel(Dialog)
		self.label_3.setGeometry(QtCore.QRect(120, 390, 151, 21))
		self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
		self.label_3.setFrameShape(QtWidgets.QFrame.Box)
		self.label_3.setAlignment(QtCore.Qt.AlignCenter)
		self.label_3.setObjectName("label_3")
		self.label_4 = QtWidgets.QLabel(Dialog)
		self.label_4.setGeometry(QtCore.QRect(440, 390, 151, 21))
		self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
		self.label_4.setFrameShape(QtWidgets.QFrame.Box)
		self.label_4.setAlignment(QtCore.Qt.AlignCenter)
		self.label_4.setObjectName("label_4")
		self.label_5 = QtWidgets.QLabel(Dialog)
		self.label_5.setGeometry(QtCore.QRect(120, 610, 151, 21))
		self.label_5.setLayoutDirection(QtCore.Qt.LeftToRight)
		self.label_5.setFrameShape(QtWidgets.QFrame.Box)
		self.label_5.setAlignment(QtCore.Qt.AlignCenter)
		self.label_5.setObjectName("label_5")
		self.label_6 = QtWidgets.QLabel(Dialog)
		self.label_6.setGeometry(QtCore.QRect(440, 610, 151, 21))
		self.label_6.setLayoutDirection(QtCore.Qt.LeftToRight)
		self.label_6.setFrameShape(QtWidgets.QFrame.Box)
		self.label_6.setAlignment(QtCore.Qt.AlignCenter)
		self.label_6.setObjectName("label_6")
		self.pushButton = QtWidgets.QPushButton(Dialog)
		self.pushButton.setGeometry(QtCore.QRect(550, 160, 141, 31))
		self.pushButton.setObjectName("pushButton")
		self.pushButton_2 = QtWidgets.QPushButton(Dialog)
		self.pushButton_2.setGeometry(QtCore.QRect(320, 370, 101, 41))
		self.pushButton_2.setObjectName("pushButton_2")
		self.selec_14 = QtWidgets.QComboBox(Dialog)
		self.selec_14.setGeometry(QtCore.QRect(200, 180, 131, 31))
		self.selec_14.setStyleSheet("background-color: rgb(255, 255, 255);")
		self.selec_14.setObjectName("selec_14")
		self.selec_14.addItem("")
		self.selec_14.addItem("")
		self.selec_14.addItem("")
		self.selec_14.addItem("")
		self.selec_14.addItem("")
		self.selec_14.addItem("")
		self.selec_14.addItem("")
		self.selec_14.addItem("")
		self.selec_14.addItem("")
		self.selec_14.addItem("")
		self.selec_14.addItem("")
		self.selec_14.addItem("")
		self.selec_15 = QtWidgets.QComboBox(Dialog)
		self.selec_15.setGeometry(QtCore.QRect(200, 130, 131, 31))
		self.selec_15.setStyleSheet("background-color: rgb(255, 255, 255);")
		self.selec_15.setObjectName("selec_15")
		self.selec_15.addItem("")
		self.selec_15.addItem("")
		self.selec_15.addItem("")
		self.selec_15.addItem("")
		self.selec_16 = QtWidgets.QComboBox(Dialog)
		self.selec_16.setGeometry(QtCore.QRect(200, 250, 161, 31))
		self.selec_16.setStyleSheet("background-color: rgb(255, 255, 255);")
		self.selec_16.setObjectName("selec_16")
		self.selec_16.addItem("")
		self.selec_16.addItem("")
		self.selec_16.addItem("")
		self.selec_16.addItem("")
		self.selec_16.addItem("")
		self.selec_17 = QtWidgets.QComboBox(Dialog)
		self.selec_17.setGeometry(QtCore.QRect(200, 300, 131, 31))
		self.selec_17.setStyleSheet("background-color: rgb(255, 255, 255);")
		self.selec_17.setObjectName("selec_17")
		self.selec_17.addItem("")
		self.selec_17.addItem("")
		self.selec_17.addItem("")
		self.selec_17.addItem("")
		self.selec_17.addItem("")
		self.selec_17.addItem("")
		self.selec_17.addItem("")
		self.selec_17.addItem("")

		self.pushButton.clicked.connect(self.clicked)

		self.retranslateUi(Dialog)
		QtCore.QMetaObject.connectSlotsByName(Dialog)

	def retranslateUi(self, Dialog):
		_translate = QtCore.QCoreApplication.translate
		Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
		self.label_30.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" text-decoration: underline;\">Sensor activo</span></p></body></html>"))
		self.selec_12.setItemText(0, _translate("Dialog", "<Ninguno>"))
		self.selec_12.setItemText(1, _translate("Dialog", "BMI270"))
		self.selec_12.setItemText(2, _translate("Dialog", "BME688"))
		self.label_9.setText(_translate("Dialog", "Frecuencia de \n"
" muestro"))
		self.label_7.setText(_translate("Dialog", "Sensibilidad"))
		self.label_2.setText(_translate("Dialog", "Configuracion \n"
" Sensor"))
		self.selec_13.setItemText(0, _translate("Dialog", "Paralelo"))
		self.selec_13.setItemText(1, _translate("Dialog", "Forzado"))
		self.label_31.setText(_translate("Dialog", "Modo de Funcionamiento"))
		self.label_32.setText(_translate("Dialog", "<html><head/><body><p><span style=\" text-decoration: underline;\">Acelerómetro</span></p></body></html>"))
		self.label_33.setText(_translate("Dialog", "<html><head/><body><p><span style=\" text-decoration: underline;\">Giroscopio</span></p></body></html>"))
		self.label_8.setText(_translate("Dialog", "Sensibilidad"))
		self.label_10.setText(_translate("Dialog", "Frecuencia de \n"
" muestro"))
		self.label_3.setText(_translate("Dialog", "Datos 1: <Datos>"))
		self.label_4.setText(_translate("Dialog", "Datos 2: <Datos>"))
		self.label_5.setText(_translate("Dialog", "Datos 3: <Datos>"))
		self.label_6.setText(_translate("Dialog", "Datos 4: <Datos>"))
		self.pushButton.setText(_translate("Dialog", "Iniciar configuración"))
		self.pushButton_2.setText(_translate("Dialog", "Iniciar captación \n"
" de datos"))
		self.selec_14.setItemText(0, _translate("Dialog", "25/32"))
		self.selec_14.setItemText(1, _translate("Dialog", "25/16"))
		self.selec_14.setItemText(2, _translate("Dialog", "25/8"))
		self.selec_14.setItemText(3, _translate("Dialog", "25/4"))
		self.selec_14.setItemText(4, _translate("Dialog", "25/2"))
		self.selec_14.setItemText(5, _translate("Dialog", "25"))
		self.selec_14.setItemText(6, _translate("Dialog", "50"))
		self.selec_14.setItemText(7, _translate("Dialog", "100"))
		self.selec_14.setItemText(8, _translate("Dialog", "200"))
		self.selec_14.setItemText(9, _translate("Dialog", "400"))
		self.selec_14.setItemText(10, _translate("Dialog", "800"))
		self.selec_14.setItemText(11, _translate("Dialog", "1600"))
		self.selec_15.setItemText(0, _translate("Dialog", "+/- 2g"))
		self.selec_15.setItemText(1, _translate("Dialog", "+/- 4g"))
		self.selec_15.setItemText(2, _translate("Dialog", "+/- 8g"))
		self.selec_15.setItemText(3, _translate("Dialog", "+/- 16g"))
		self.selec_16.setItemText(0, _translate("Dialog", "+/- 2000 dps, 16.4 LSB/dps"))
		self.selec_16.setItemText(1, _translate("Dialog", "+/- 1000 dps, 32.8 LSB/dps"))
		self.selec_16.setItemText(2, _translate("Dialog", "+/- 500 dps, 65.6 LSB/dps"))
		self.selec_16.setItemText(3, _translate("Dialog", "+/- 250 dps, 131.2 LSB/dps"))
		self.selec_16.setItemText(4, _translate("Dialog", "+/- 125 dps, 262.4 LSB/dps"))
		self.selec_17.setItemText(0, _translate("Dialog", "25"))
		self.selec_17.setItemText(1, _translate("Dialog", "50"))
		self.selec_17.setItemText(2, _translate("Dialog", "100"))
		self.selec_17.setItemText(3, _translate("Dialog", "200"))
		self.selec_17.setItemText(4, _translate("Dialog", "400"))
		self.selec_17.setItemText(5, _translate("Dialog", "800"))
		self.selec_17.setItemText(6, _translate("Dialog", "1600"))
		self.selec_17.setItemText(7, _translate("Dialog", "3200"))


if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	Dialog = QtWidgets.QDialog()
	ui = Ui_Dialog()
	ui.setupUi(Dialog)
	Dialog.show()
	sys.exit(app.exec_())
