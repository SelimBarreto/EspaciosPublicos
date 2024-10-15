import json
import os
from django.core.management.base import BaseCommand
from espacios.models import InstalacionDeportiva

class Command(BaseCommand):
    help = 'Carga instalaciones deportivas desde un archivo JSON'

    def handle(self, *args, **kwargs):
        # Genera la ruta absoluta al archivo JSON
        base_dir = os.path.dirname(os.path.abspath(__file__))
        json_path = os.path.join(base_dir, 'C:\EspaciosPublicos\Base_De_Datos_Espacios_Publicos\espacios_publicos\data\instalaciones_deportivas.json')

        # Asegúrate de que la ruta sea válida
        self.stdout.write(f'Usando la ruta: {json_path}')

        with open(json_path, encoding='utf-8') as file:
            data = json.load(file)

            for item in data['features']:
                properties = item['properties']
                InstalacionDeportiva.objects.update_or_create(
                    id=properties['no'],
                    defaults={
                        'nombre': properties['nombre_instalacion'],
                        'alcaldia': properties['alcaldia'],
                        'direccion': properties['direccion'],
                        'deporte': properties['deporte'],
                        'horario': properties['horario'],
                        'costo': properties['costo'],
                        'servicios': properties.get('servicios', 'No especificado'),
                        'tipo_pasto': properties.get('tipo_pasto', 'No especificado'),
                        'acepta_mascotas': properties.get('acepta_mascotas', False),
                    }
                )
            self.stdout.write(self.style.SUCCESS('Datos cargados exitosamente.'))
