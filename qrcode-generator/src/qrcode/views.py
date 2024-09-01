from rest_framework.response import Response
from rest_framework.views import APIView

import qrcode


class QRCodeGeneratorView(APIView):

    def __init__(self):
        super().__init__()
        self.model_service = YourModelService()
        
    def get(self, request, *args, **kwargs):
        data = request.query_params.get('data', 'Hello, QR Code!')

        # generate QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")

        # upload to s3
        response = Response({'message': 'QR code generated successfully', 'image': img.save('qrcode.png')})

        # response url
        return response
