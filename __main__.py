from apis.factory import create_app

if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', port=8001)