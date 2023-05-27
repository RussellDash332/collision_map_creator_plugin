import lxml.etree as et

tree = et.fromstring(open('lvl11_final.world').read())

print('Before:', len(tree.findall('.//model')))

for model in tree.findall('.//model'):
    for check in ['chair', 'table', 'bin', 'drawer', 'cubicle', 'sofa', 'toilet', 'cylinder', 'sink', 'kicthen', 'shelf', 'mop', 'openrobotics', 'door', 'clone']:
        if check in model.get('name').lower() or len(model.get('name').lower()) < 5:
            model.getparent().remove(model)
            break

print('After:', len(tree.findall('.//model')))

with open('lvl11.world', 'w+') as f:
    f.write(et.tostring(tree, pretty_print=True).decode())
