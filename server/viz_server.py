import cv2

from flask import Flask, request, render_template
from py_flask_movie.flask_movie import FlaskMovie
from py_pipe.pipe import Pipe

from bhp_sep.dataset_processor import DataProcessor

dp = DataProcessor()

app=Flask(__name__)
fm = FlaskMovie(app=app)
pipe = Pipe(limit=None)
fm.create('viz',pipe)

@app.route('/', methods=['GET', 'POST'])
def main():
    args = request.form
    data_columns = []
    for _ in args:
        data_columns.append(_)
    print(len(data_columns))
    if data_columns:
        plt = dp.visualizer(*data_columns)
        plt.tight_layout()
        plt.savefig('/home/developer/PycharmProjects/bhp-sep/server/temp.jpg')
    return render_template('index.html')

def start():
    fm.start("0.0.0.0", 5000)
    while True:
        pipe.push_wait()
        pipe.push(cv2.imread('/home/developer/PycharmProjects/bhp-sep/server/temp.jpg'))






# from io import BytesIO
#
# import cv2
# from flask import Flask, request, redirect, url_for, render_template
# from matplotlib import pyplot
# from py_flask_movie.flask_movie import FlaskMovie
# from bhp_sep.dataset_processor import DataProcessor
# from py_pipe.pipe import Pipe
# import  numpy as np
# # import matplotlib as plt
# # from flask_api import status
#
#
# app = Flask(__name__)
# dp = DataProcessor()
# fm = FlaskMovie(app)
# fm.start(bind_ip='0.0.0.0', bind_port=5000)
# pipe = Pipe()
# fm.create("viz", pipe=pipe)
#
#
# class VizServer:
#
#     @staticmethod
#     @app.route('/')
#     def index():
#         return render_template('index.html')
#
#     @staticmethod
#     @app.route("/select", methods=['POST'])
#     def select():
#         args = request.args
#         data_columns = []
#         for _ in args:
#             data_columns.append(_)
#
#         print(len(data_columns))
#         if len(data_columns) > 0:
#             plt = dp.visualizer2(*data_columns)
#             plt.tight_layout()
#             plt.savefig('temp.jpg')
#             pipe.push(cv2.imread('temp.jpg'))
#
#         content = {'success': 'success'}
#         return content, status.HTTP_404_NOT_FOUND
#
#
#
#
#
#
