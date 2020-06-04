import sys
from PyQt5 import QtWidgets, QtGui
import pytube
from pytube import YouTube
import os
import urllib.request

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("YouTube Downloader")
        self.setWindowIcon(QtGui.QIcon("yt_logo.png"))
        self.resize(1500, 750)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.proceed = QtWidgets.QPushButton(self.centralwidget)
        self.proceed.setObjectName("proceed")
        self.proceed.setText("Proceed")
        self.proceed.clicked.connect(self.list_options)
        self.gridLayout.addWidget(self.proceed, 2, 0, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 6, 0, 1, 5)
        self.videoURL = QtWidgets.QLabel(self.centralwidget)
        self.videoURL.setObjectName("videoURL")
        self.videoURL.setText("Video URL:")
        self.gridLayout.addWidget(self.videoURL, 0, 0, 1, 1)
        self.selectLocation = QtWidgets.QLabel(self.centralwidget)
        self.selectLocation.setObjectName("selectLocation")
        self.selectLocation.setText("Select Location:")
        self.gridLayout.addWidget(self.selectLocation, 4, 0, 1, 1)
        self.download = QtWidgets.QPushButton(self.centralwidget)
        self.download.setObjectName("download")
        self.download.setText("Download")
        self.download.clicked.connect(self.download_video)
        self.gridLayout.addWidget(self.download, 8, 2, 1, 1)
        self.inputLocation = QtWidgets.QLineEdit(self.centralwidget)
        self.inputLocation.setObjectName("inputLocation")
        self.gridLayout.addWidget(self.inputLocation, 5, 0, 1, 4)
        self.browse = QtWidgets.QPushButton(self.centralwidget)
        self.browse.setObjectName("browse")
        self.browse.setText("Browse")
        self.browse.clicked.connect(self.showFilePicker)
        self.gridLayout.addWidget(self.browse, 5, 4, 1, 1)
        self.inputURL = QtWidgets.QLineEdit(self.centralwidget)
        self.inputURL.setObjectName("inputURL")
        self.gridLayout.addWidget(self.inputURL, 1, 0, 1, 5)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 3, 0, 1, 4)
        self.thumbnail = QtWidgets.QLabel(self.centralwidget)
        self.thumbnail.setObjectName("thumbnail")
        self.thumbnail.setText("")
        self.gridLayout.addWidget(self.thumbnail, 3, 4, 1, 1)
        self.setCentralWidget(self.centralwidget)
        QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
        self.show()

    def showFilePicker(self):
        location = QtWidgets.QFileDialog.getExistingDirectory(self.centralwidget, "Select Folder")
        if location:
            self.inputLocation.setText(location)

    def list_options(self):
        video_url = self.inputURL.text()
        if video_url:
            global size
            global videos
            self.listWidget.clear()
            yt = YouTube(str(video_url), on_progress_callback = self.progress_function)

            url = yt.thumbnail_url
            data = urllib.request.urlopen(url).read()
            pixmap = QtGui.QPixmap()
            pixmap.loadFromData(data)
            pixmap = pixmap.scaled(300, 200)
            self.thumbnail.setPixmap(pixmap)

            videos = yt.streams.order_by('resolution')
            count = 1
            self.listWidget.addItem(f'{yt.title}\n')
            for video in videos:
                size = video.filesize
                stream = f'{count}. {video} {round(size/1024**2, 2)} MB'
                self.listWidget.addItem(stream)
                count += 1
        else:
            QtWidgets.QMessageBox.about(self, "Type URL", "Please type the Video URL.")

    def download_video(self):
        if self.listWidget.selectedItems():
            video = self.listWidget.selectedItems()[0].text()
            choice = int(video.split('.')[0])
            req_video = videos[choice-1]
            if self.inputLocation.text():
                path = self.inputLocation.text()
            else:
                path = os.getcwd()
            req_video.download(path)
        else:
            QtWidgets.QMessageBox.about(self, "Error", "Please type the Video URL & select a video to download.")


    def progress_function(self, stream, chunk, bytes_remaining):
        self.progressBar.setValue(float(1 - bytes_remaining/size)*float(100))

def main():
    app = QtWidgets.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
