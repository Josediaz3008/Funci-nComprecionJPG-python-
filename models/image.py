from odoo import models, fields, api
from PIL import Image
import io
import base64

class ImageCompression(models.Model):
    _name = 'image.compression'
    _description = 'Image Compression'

    name = fields.Char('Name')
    image = fields.Binary('Image')

    @api.model
    def compress_and_store_image(self, image_data, quality):
        """
        Comprime la imagen y la almacena en el campo 'image'.
        
        :param image_data: Datos de la imagen en formato base64
        :param quality: Calidad de compresión (0-100)
        """
        try:
            # Decodificar la imagen
            image_bytes = base64.b64decode(image_data)
            
            # Abrir la imagen con PIL
            image = Image.open(io.BytesIO(image_bytes))
            
            # Crear un buffer para la imagen comprimida
            buffer = io.BytesIO()
            image.save(buffer, format="JPEG", quality=quality)
            compressed_image_data = buffer.getvalue()
            
            # Codificar en base64
            compressed_image_base64 = base64.b64encode(compressed_image_data).decode('utf-8')
            
            # Almacenar la imagen comprimida en el campo 'image'
            self.write({'image': compressed_image_base64})
        except Exception as e:
            # Manejo de errores
            return {'status': 'error', 'message': str(e)}
        return {'status': 'success'}
