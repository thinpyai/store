from rest_framework.response import Response
from rest_framework.views import APIView

import qrcode


class QRCodeGeneratorView(APIView):
    def get(self, request, *args, **kwargs):
        data = request.query_params.get('data', 'Hello, QR Code!')
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        response = Response({'message': 'QR code generated successfully', 'image': img.save('qrcode.png')})
        return response
