from waitress import serve
from whitenoise import WhiteNoise

from src.server import MainServer


if __name__ == '__main__':
    app = WhiteNoise(MainServer(), f'src/views/static/', prefix='/static')
    print("Сервер запущен")
    serve(app, host='0.0.0.0', port='8020')
