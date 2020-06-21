#!/usr/bin/python
MAX_LINE_LENGTH = 80

def right_align_paragraph(text, margin=MAX_LINE_LENGTH):
  l = []
  w = []
  for c in text:
    if c == '\n':
      output = ''.join([' '] * (margin - len(l)) + l)
      print output
      l = []
      w = []
    if c == ' ':
      if len(l) + len(w) < margin:
        l.extend(w)
        l.append(' ')
        w = []
      else:
        print ''.join([' '] * (margin - len(l)) + l)
        l = w
        w = []
    elif len(w) < margin:
      w += c
    else:
      print 'Not possible to allign'
      break
  print ''.join(w)

if __name__ == '__main__':
    right_align_paragraph(raw_input(),5)


