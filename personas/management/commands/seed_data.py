from django.core.management.base import BaseCommand
from personas.models import Company, Person


class Command(BaseCommand):
    help = 'Crea datos de ejemplo para probar la aplicación'

    def handle(self, *args, **options):
        companies_data = [
            {'name': 'TechCorp', 'email': 'info@techcorp.com', 'phone': '555-0101', 'address': 'Av. Tecnología 100'},
            {'name': 'Green Solutions', 'email': 'contacto@green.com', 'phone': '555-0102', 'address': 'Calle Verde 200'},
            {'name': 'DataFlow', 'email': 'hello@dataflow.io', 'phone': '555-0103', 'address': 'Blvd. Datos 300'},
            {'name': 'Innovatech', 'email': 'info@innovatech.com', 'phone': '555-0104', 'address': 'Av. Innovación 400'},
            {'name': 'GlobalSoft', 'email': 'ventas@globalsoft.com', 'phone': '555-0105', 'address': 'Calle Global 500'},
        ]

        companies = []
        for data in companies_data:
            company, created = Company.objects.get_or_create(name=data['name'], defaults=data)
            companies.append(company)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Empresa creada: {company.name}'))
            else:
                self.stdout.write(f'Empresa ya existe: {company.name}')

        people_data = [
            {'first_name': 'Carlos', 'last_name': 'García', 'email': 'carlos@techcorp.com', 'phone': '555-1001', 'position': 'Desarrollador', 'company': companies[0]},
            {'first_name': 'María', 'last_name': 'López', 'email': 'maria@techcorp.com', 'phone': '555-1002', 'position': 'Diseñadora', 'company': companies[0]},
            {'first_name': 'Juan', 'last_name': 'Martínez', 'email': 'juan@techcorp.com', 'phone': '555-1003', 'position': 'Gerente', 'company': companies[0]},
            {'first_name': 'Ana', 'last_name': 'Rodríguez', 'email': 'ana@green.com', 'phone': '555-1004', 'position': 'Consultora', 'company': companies[1]},
            {'first_name': 'Pedro', 'last_name': 'Sánchez', 'email': 'pedro@green.com', 'phone': '555-1005', 'position': 'Analista', 'company': companies[1]},
            {'first_name': 'Laura', 'last_name': 'Fernández', 'email': 'laura@dataflow.io', 'phone': '555-1006', 'position': 'Ingeniera', 'company': companies[2]},
            {'first_name': 'Diego', 'last_name': 'Torres', 'email': 'diego@dataflow.io', 'phone': '555-1007', 'position': 'DevOps', 'company': companies[2]},
            {'first_name': 'Sofia', 'last_name': 'Ramírez', 'email': 'sofia@dataflow.io', 'phone': '555-1008', 'position': 'Scrum Master', 'company': companies[2]},
            {'first_name': 'Andrés', 'last_name': 'Morales', 'email': 'andres@innovatech.com', 'phone': '555-1009', 'position': 'Arquitecto', 'company': companies[3]},
            {'first_name': 'Elena', 'last_name': 'Vargas', 'email': 'elena@innovatech.com', 'phone': '555-1010', 'position': 'Product Owner', 'company': companies[3]},
            {'first_name': 'Roberto', 'last_name': 'Díaz', 'email': 'roberto@globalsoft.com', 'phone': '555-1011', 'position': 'Director TI', 'company': companies[4]},
            {'first_name': 'Carmen', 'last_name': 'Ruiz', 'email': 'carmen@globalsoft.com', 'phone': '555-1012', 'position': 'Desarrolladora', 'company': companies[4]},
        ]

        for data in people_data:
            person, created = Person.objects.get_or_create(
                email=data['email'],
                defaults=data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Persona creada: {person.full_name}'))
            else:
                self.stdout.write(f'Persona ya existe: {person.full_name}')

        self.stdout.write(self.style.SUCCESS('\nDatos de ejemplo creados correctamente.'))
