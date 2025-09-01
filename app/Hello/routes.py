from flask import Blueprint
name = "Gabriel Gadens"
hello_bp = Blueprint('Hello',__name__)

@hello_bp.route('/')
def index():
          return "Hello World"

@hello_bp.route('/sobre')
def sobre():
          return "Olá, "+name