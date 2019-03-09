from io import BytesIO

import cv2
from flask import Flask, request, redirect, url_for, render_template
from matplotlib import pyplot
from py_flask_movie.flask_movie import FlaskMovie
from bhp_sep.dataset_processor import DataProcessor
from py_pipe.pipe import Pipe
import  numpy as np
# import matplotlib as plt
from flask_api import status


def fig2data(fig):
    """
    @brief Convert a Matplotlib figure to a 4D numpy array with RGBA channels and return it
    @param fig a matplotlib figure
    @return a numpy 3D array of RGBA values
    """
    # draw the renderer
    fig.canvas.draw()

    # Get the RGBA buffer from the figure
    w, h = fig.canvas.get_width_height()
    buf = np.fromstring(fig.canvas.tostring_argb(), dtype=np.uint8)
    buf.shape = (w, h, 4)

    # canvas.tostring_argb give pixmap in ARGB mode. Roll the ALPHA channel to have it in RGBA mode
    buf = np.roll(buf, 3, axis=2)
    return buf

app = Flask(__name__)
dp = DataProcessor()
fm = FlaskMovie(app)
fm.start(bind_ip='0.0.0.0', bind_port=5000)
pipe = Pipe()
fm.create("viz", pipe=pipe)


class VizServer:

    @staticmethod
    @app.route('/')
    def index():
        return render_template('index.html')

    @staticmethod
    @app.route("/select", methods=['POST'])
    def select():
        args = request.args
        data_columns = []
        for _ in args:
            data_columns.append(_)

        print(len(data_columns))
        if len(data_columns) > 0:
            plt = dp.visualizer2(*data_columns)
            plt.tight_layout()
            plt.savefig('temp.jpg')
            pipe.push(cv2.imread('temp.jpg'))

        content = {'success': 'success'}
        return content, status.HTTP_404_NOT_FOUND






