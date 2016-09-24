brew install opencv3 --with-python3 --with-examples --with-contrib --with-tbb --with-ffmpeg --with-gstreamer --with-qt
pip install numpy
echo /usr/local/opt/opencv3/lib/python3.5/site-packages >> venv/lib/python3.5/site-packages/opencv3.pth


# mplayer -vo caca MovieName.avi
