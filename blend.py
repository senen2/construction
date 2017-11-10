import bpy
import sys

def has_material(obj, material):
	if material in bpy.data.materials:
		mat = bpy.data.materials[material]
	else:
		return False

	for slot in obj.material_slots:
		if slot.material == mat:
			return True
	return False

def build_apu(obj, material):
	x, y, z = obj.dimensions
	name = material  + " " + obj.name
	if material == 'beam':
		l, h = (x, y) if x > y else (y, x)
		n = 10 if h > .22 else 4
		return Beam(name, l, area=z*h, num_varillas=n)
	elif material == 'column':
		h = x if x > y else y
		n = 10 if h > .22 else 4
		return Estructura(name, z, area=x*y, num_varillas=n)
	elif material == 'door_garage':
		return PuertaGaraje(name, 1)
	elif material[:4] == 'door':
		return Puerta(name, 1)
	elif material[:5] == 'floor':
		return Piso(name, x*y)
	elif material == 'roof':
		return Techo(name, x*y)
	elif material[:4] == 'slab':
		return Placa(name, x*y, z)
	elif material[:5] == 'stair':
		return Placa(name, x*y, .17)
	elif material[:4] == 'wall':
		if x > y:
			return Pared(name, x*z)
		else:
			return Pared(name, y*z)
	elif material[:6] == 'window':
		return Ventana(name, 1)
	else:
		return None

dir = '/home/carlos/Documents/val/casa/scripts'
if not dir in sys.path:
    sys.path.append(dir )

from obra import *

materials = ['beam', 'column', 'door', 'door_garage', 'floor', 'roof', 'slab', 'slab_floor', 'stair', 'wall', 'window']

apus = []

for obj in bpy.context.selected_objects:
	for material in materials:
		if has_material(obj, material):
			apu = build_apu(obj, material)
			if apu:
				apus.append(apu)
			break

if apus:
	obra = Obra('obra', apus=apus)
	obra.show_items()
	obra.show_res_items()
	obra.show_mp()
	obra.show_mo()
	print("\nmp+mo", "{:,}".format(obra.valor_mp + obra.valor_mo))
else:
	print("\nnothing to process")