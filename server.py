from speedyserv import app

from speedyserv.controllers import table_controller
from speedyserv.controllers import meal_controller
from speedyserv.controllers import category_controller

if __name__ == '__main__':
    app.run(debug=True)