def removeEmptyList(l):
  flat_list = flatten(l)
  return list(filter(ifNotSpace, flat_list))

def flatten(xss):
    return [x for xs in xss for x in xs]

def ifNotSpace(variable):
  if variable == '':
    return False
  else:
    return True
