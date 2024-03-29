# -*- coding: utf-8 -*-
"""
/***************************************************************************
 OnlineRoutingMapperDialog
                                 A QGIS plugin
 Generate routes by using online services (Google Directions, Here, MapBox, YourNavigation, OSRM etc.)
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2018-10-01
        git sha              : $Format:%H$
        copyright            : (C) 2018 by Mehmet Selim BILGIN
        email                : mselimbilgin@yahoo.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from PyQt5 import uic
from PyQt5 import QtWidgets

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'OnlineRoutingMapper_dialog_base.ui'))

class OnlineRoutingMapperDialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(OnlineRoutingMapperDialog, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        
        self.setupUi(self)
        

FORM_CLASS_AG_PEDIDO, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'OnlineRoutingMapper_dialog_base_agendar_pedido.ui'))

class OnlineRoutingMapperDialogAgPedido(QtWidgets.QDialog, FORM_CLASS_AG_PEDIDO):
    def __init__(self, parent=None):
        """Constructor."""
        super(OnlineRoutingMapperDialogAgPedido, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)

FORM_CLASS_MOD_MAPA, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'OnlineRoutingMapper_dialog_base_mod_mapa.ui'))

class OnlineRoutingMapperDialogModMapa(QtWidgets.QDialog, FORM_CLASS_MOD_MAPA):
    def __init__(self, parent=None):
        """Constructor."""
        super(OnlineRoutingMapperDialogModMapa, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
FORM_CLASS_MOD_MAPA, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'OnlineRoutingMapper_dialog_base_mod_bombas.ui'))

class OnlineRoutingMapperDialogModBombas(QtWidgets.QDialog, FORM_CLASS_MOD_MAPA):
    def __init__(self, parent=None):
        """Constructor."""
        super(OnlineRoutingMapperDialogModBombas, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)

FORM_CLASS_VER_PEDIDOS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'OnlineRoutingMapper_dialog_base_ver_pedidos.ui'))

class OnlineRoutingMapperDialogVerPedidos(QtWidgets.QDialog, FORM_CLASS_VER_PEDIDOS):
    def __init__(self, parent=None):
        """Constructor."""
        super(OnlineRoutingMapperDialogVerPedidos, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)

FORM_CLASS_ESTADISTICAS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'OnlineRoutingMapper_dialog_base_estadisticas.ui'))

class OnlineRoutingMapperDialogEstadisticas(QtWidgets.QDialog, FORM_CLASS_ESTADISTICAS):
    def __init__(self, parent=None):
        """Constructor."""
        super(OnlineRoutingMapperDialogEstadisticas, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)








