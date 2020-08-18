def crop_hydrated(f):
  def hasWaterNeighbor(row,col):
    return True in [True if f[r][c]=='w'else False 
    for r in range(row-1,row+2)
    if r > -1 and r < len(f)
    for c in range(col-1,col+2)
    if c > -1 and c < len(f[0])]
  # replace watered c's with C
  return 'c' not in ['C' 
    if hasWaterNeighbor(r,c) 
    else f[r][c] 
    for r in range(len(f))
    for c in range(len(f[0]))
    if f[r][c]=='c']

  
print(crop_hydrated([['c', 'w', 'c'],
                     ['c', 'c', 'c'],
                     ['w', 'c', 'c']]))