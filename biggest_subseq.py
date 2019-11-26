def big_sub(s,dict):
  dict = sorted(dict,reverse=True)
  print(type(dict))
  print(dict)
  for x in range(len(dict)):
    print(dict[x])
    seqFound = False
    i = 0
    j = 0
    w = ''
    while(i<len(dict[x]) and j< len(s)):
      if dict[x][i] not in s:
        print(dict[x],': Is not subsequence')
        break
      elif(dict[x][i]==s[j]):
        w += dict[x][i]
        i += 1
        j += 1
      else:
        j += 1
      if w == dict[x]:
          seqFound = True
          print(w,'sequence found')
          break


if __name__ == '__main__':
  s = 'abppplee'
  d = {'able','ale','apple','kangaroo','apples'}
  big_sub(s,d)
