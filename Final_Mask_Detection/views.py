from django.shortcuts import render
from django.http.response import StreamingHttpResponse
from Final_Mask_Detection.camera import MaskDetect


# Create your views here.


def index(request):
	return render(request, 'stream.html')


def gen(camera):
	while True:
		frame = camera.get_frame()
		yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def mask_feed(request):
	return StreamingHttpResponse(gen(MaskDetect()),content_type='multipart/x-mixed-replace; boundary=frame')