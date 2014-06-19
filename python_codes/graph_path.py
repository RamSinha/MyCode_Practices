import sys



def adjlist_find_paths(a, n, m, path=[]):
  "Find paths from node index n to m using adjacency list a."
  path = path + [n]
  if n == m:
    return [path]
  paths = []
  for child in a[n]:
    if child not in path:
      child_paths = adjlist_find_paths(a, child, m, path)
      for child_path in child_paths:
        paths.append(child_path)
  return paths


if __name__=='__main__':
    d={}
    m=int(raw_input().strip())
    while True:
        (a,b) = tuple([int(i) for i in raw_input().strip().split()])
        if a==0 and b==0:
            break
        if d.has_key(a):
            temp=d.get(a)
            temp.append(b)
            d[a]=temp
        else:
            d[a]=[b]
    print len(adjlist_find_paths(d,1,m))
    #sys.exit(0)
    #print d



