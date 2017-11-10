# -*- coding: utf-8 -*-
import pandas as pd

def res_mp(apus, cantidad):
	mp = apus.copy()
	mp['cantidad_mp'] = [x.cantidad_mp for x in mp['tipo']]
	mp['unidad'] = [x.unidad for x in mp['tipo']]
	mp['pu'] = [x.pu for x in mp['tipo']]
	mp['tipo'] = [x.tipo for x in mp['tipo']]
	mp['cantidad'] = mp['cantidad'] * mp['cantidad_mp']
	mp = res(mp, 'tipo')
	mp['cantidad'] = mp['cantidad'] * cantidad
	# mp = (mp.groupby(['tipo', 'unidad', 'pu'])['cantidad'].sum() * cantidad).reset_index()
	# mp['valor'] = mp['cantidad'] * mp['pu']
	return mp.round(2)

def res_apus(apus):
	apus = [x.r for x in apus]
	apus = pd.DataFrame(data=apus, columns=['nombre', 'type', 'unidad', 'cantidad', 'pu', 'valor'])
	items = res(apus, 'type')
	# valor_items = items['valor'].sum()
	return items.round(2)

# def res_mp_obras1(obras):
# 	# mp = [y for x in obras for z in x.apus for y in z.materiales]
# 	mp = pd.concat([z.materiales for x in obras for z in x.apus])
# 	print "*****"
# 	print mp.iloc[0]
# 	mp['cantidad_mp'] = [x.cantidad_mp for x in mp['tipo']]
# 	mp['unidad'] = [x.unidad for x in mp['tipo']]
# 	mp['pu'] = [x.pu for x in mp['tipo']]
# 	mp['tipo'] = [x.tipo for x in mp['tipo']]
# 	mp['cantidad'] = mp['cantidad'] * mp['cantidad_mp']

# 	mp = mp.groupby(['tipo', 'unidad', 'pu'])['cantidad'].sum().reset_index()
# 	# mp = mp.round(0)
# 	mp['valor'] = mp['cantidad'] * mp['pu']

# 	return mp

def res(m, key):
	m = m.groupby([key, 'unidad', 'pu'])['cantidad'].sum().reset_index()
	m['valor'] = (m['cantidad'] * m['pu']).round(0)
	return m

def res_mo_obra(apus):
	mo = pd.concat([x.mo for x in apus])
	return res(mo, 'tarea').round(2)

def res_mp_obras(obras):
	mp = pd.concat([z.mp for x in obras for z in x.apus])
	return res(mp, 'tipo').round(2)

def res_mo_obras(obras):
	mo = pd.concat([z.mo for x in obras for z in x.apus])
	return res(mo, 'tarea').round(2)

def res_items_obras(obras):
	apus = [z.r for x in obras for z in x.apus]
	apus = pd.DataFrame(data=apus, columns=['nombre', 'type', 'unidad', 'cantidad', 'pu', 'valor'])
	items = apus.groupby(['nombre', 'unidad', 'pu'])['cantidad'].sum().reset_index()
	items['valor'] = (items['cantidad'] * items['pu']).round(2)
	valor_items = items['valor'].sum()
	return items
