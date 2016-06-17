"""Library to test generated QR Codes."""

import base64
import qrtools

from robot.api import logger


class QRDecoder(object):
    """Keywords to test the REST API using Requests."""

    def check_if_an_image_is_a_valid_qr_code(self, image_element):
        """Check if an image is a QR Code.
        
        ``image_element`` is supposed to be a selenium element of an image,
        with a ``src`` attribute that is a PNG image encoded as Base64.
        """
        encoded_data = image_element.get_attribute('src')
        if not encoded_data.startswith('data:image/png;base64,'):
            raise RuntimeError('Image is not a PNG encoded as Base64')

        encoded_data = encoded_data.replace('data:image/png;base64,', '')
        logger.info('Base64 Data: %s' % encoded_data)
        png_data = base64.b64decode(encoded_data)
        with open('/tmp/qrcode_img.png', 'w') as fd:
            fd.write(png_data)

        qr = qrtools.QR()
        result = qr.decode(filename='/tmp/qrcode_img.png')
        if not result:
            raise RuntimeError('Image could not be decoded as a QR Code.')
        logger.info('QR Code Data: %s' % qr.data_to_string())
