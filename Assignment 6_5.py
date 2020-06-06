text = "X-DSPAM-Confidence:    0.8475";
pos=text.rfind(' ')
num=float(text[pos+1: ])
print(num)