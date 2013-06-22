# (c) 2013 Joost Yervante Damad <joost@damad.be>
# License: GPL

import os.path
import shlex

def detect(fn):
  if os.path.isdir(fn): return None
  try:
    with open(fn, 'r') as f:
      l = f.readlines()
      l0 = l[0]
      l2 = l0.split()
      if (l2[0] == 'PCBNEW-LibModule-V1'): return "1"
      elif (l2[0] == 'PCBNEW-LibModule-V2'): return "2"
      return None
  except:
    return None

def num_to_type(i):
  i = int(i)
  return {
    17: 'glue',
    19: 'paste',
    21: 'silk',
    23: 'stop',
    25: 'docu',
  }.get(i)
    
class Import:

  def __init__(self, fn):
    self.fn = fn

  def import_module(self, name, lines):
    meta = {}
    meta['type'] = 'meta'
    meta['name'] = name
    meta['id'] = uuid.uuid4().hex
    meta['desc'] = None
    l = [meta]
    metric = True

    def cd(s): 
      if meta['desc'] == None:
        meta['desc'] = s[1]
      else:
        meta['desc'] = meta['desc'] + "\n" + s[1]
      return None

    def units(s):
      metric = s[1] == 'mm'
      return None

    def label(s, is_value):
      shape = { 'shape': 'label', 'type': 'silk' }
      shape['value'] = s[11]
      if (is_value):
        shape['value'] = 'VALUE'
      shape['x'] = float(s[1])
      shape['y'] = -float(s[2])
      shape['dy'] = float(s[3])
      shape['w'] = float(s[6])
      return shape

    def ds(s):
      shape = { 'shape': 'line' }
      shape['x1'] = float(s[1])
      shape['y1'] = -float(s[2])
      shape['x2'] = float(s[3])
      shape['y2'] = -float(s[4])
      shape['w'] = float(s[5])
      shape['type'] = num_to_type(s[6])
      return shape

    # DC Xcentre Ycentre Xpoint Ypoint Width Layer
    def dc(s):
      shape = { 'shape': 'circle' }
      x = float(s[1])
      y = -float(s[2])
      shape['x'] = x
      shape['y'] = y
      ex = float(s[3])
      ey = float(s[4])
      dx = abs(x - ex)
      if f_eq(dx, dy):
        shape['r'] = dx*math.sqrt(2)
        if f_eq(shape['width'], shape['r']):
          shape['type'] = 'disc'
          shape['r'] = shape['r'] * 2
          del shape['width']
      else:
        shape['rx'] = dx*math.sqrt(2)
        shape['ry'] = dy*math.sqrt(2)
      shape['type'] = num_to_type(s[6])
      return shape

    # DA Xcentre Ycentre Xstart_point Ystart_point angle width layer
    def da(s):
      shape = { 'shape': 'arc' }
      shape['x1'] = float(s[1])
      shape['y1'] = -float(s[2])
      shape['x2'] = float(s[3])
      shape['y2'] = -float(s[4])
      shape['a'] = float(s[5])/10
      shape['w'] = float(s[6])
      shape['type'] = num_to_type(s[7])
      return shape

    # DP 0 0 0 0 corners_count width layer
    # Dl corner_posx corner_posy
    def dp(s):
      pass
      # TODO, polygon needs multiline parsing

    for i in range(0, len(lines)):
      s = shlex.split(lines[i])
      k = s[0]
      if k == '$EndMODULE':
        return mod
      elif k == '$PAD':
        (i, pad) = import_pad(lines, i)
        l.append(pad)
      else:
        res = {
          'cd': cd,
          'units': units,
          't0': lambda a: label(a, False),
          't1': lambda a: label(a, True),
          'ds': ds,
          'dc': dc,
          'da': da,
          'dp': dp,
        }.get(s[0].lower(), lambda a: None)(s)
        if res != None:
          l.append(res)
    return l

  def import_footprint(self, name):
    with open(self.fn, 'r') as f:
      lines = f.readlines()
    for i in range(0, len(lines)):
      s = shlex.split(lines[i])
      if s[0] == '$MODULE' and s[1] == name:
        return self.import_module(name, lines[i+1:])
    raise Exception("footprint not found %s" % (name))

  def list(self):
    with open(self.fn, 'r') as f:
      lines = f.readlines()
    for line in lines:
      s = shlex.split(line)
      if s[0] == '$MODULE':
        print s[1]

class Export:

  def __init__(self, fn):
    self.fn = fn

  def export_footprint(self, interim):
    raise Exception("Export to KiCad old not yet supported")

  def save(self):
    pass