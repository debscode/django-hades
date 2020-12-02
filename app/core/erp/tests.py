from config.wsgi import *
from core.erp.models import *

data = ['Leche y derivados', 'Carnes, pescados y huevos', 'Patatas, legumbres, frutos secos',
        'Verduras y Hortalizas', 'Frutas', 'Cereales y derivados, azúcar y dulces',
        'Grasas, aceite y mantequilla']

for i in data:
    cat = Category(name=i)
    cat.save()
    print('Guardado registro N°{}'.format(cat.id))


# #select * from
# query = Type.objects.all()
# print(query)
#
# #insert
# t = Type()
# t.name = "Test2"
# t.save()

# #update
# t = Type.objects.get(id=1)
# t.name = "Change"
# t.save()

#delete
# try:
#     t = Type.objects.get(id=1)
#     t.delete()
# except Exception as e:
#     print(e)

# obj = Type.objects.filter(name__contains='test')
# obj = Type.objects.filter(name__startswith='T')
# print(obj)

# obj = Employee.objects.filter(type_id = 2)
# print(obj)