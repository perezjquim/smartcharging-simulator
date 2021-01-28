from core import *
from data import *
from ui import *

from flask import Flask

oSimulator = Simulator( )
oSimulator.onInit( )

oDataServer = DataServer( oSimulator )

oApp = Flask( __name__ )
oApp.register_blueprint( oDataServer.getBlueprint() )		

print( "Great success" )