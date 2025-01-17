from controller import app


if __name__ == '__main__':
    # Запуск сервера SocketIO с использованием приложения Flask
    app.run(debug=False)