from aiohttp.web import Application
from app.web.app import run_app

app = Application()

if __name__ == '__main__':
    run_app()
