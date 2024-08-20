from odoo import http
from odoo.http import request

class ImageCompressionController(http.Controller):

    @http.route('/compress_image', type='json', auth='public', methods=['POST'])
    def compress_image(self, image_base64, quality):
        """
        Ruta para comprimir una imagen y almacenarla.
        
        :param image_base64: Imagen en formato base64
        :param quality: Calidad de compresión
        """
        if not (0 <= quality <= 100):
            return {'status': 'error', 'message': 'Quality must be between 0 and 100'}

        # Crear una instancia del modelo
        image_model = request.env['image.compression'].create({})
        
        # Comprimir y almacenar la imagen
        return image_model.compress_and_store_image(image_base64, quality)
