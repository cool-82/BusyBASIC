#no stealling pretty please

#heres some example code: 
#00101 10011 01000 11100 10000 10111 00010 01000 11100
#it prints 1 if the bit is 1 and 0 if its 0 but in a workaround way and i only just realised that it could be heavily simplified
#but this is to show off how it works not to be efficient
data = []
print("how many bits should there be?")
zzzzaaaarrrrgggg = int(input())
for i in range(zzzzaaaarrrrgggg):
    data.append(0)
oger = (input())
paso = oger.replace(" ", "")
lines = [paso[i:i+5] for i in range(0, len(paso), 5)]
print("program:", lines)
program = []
brancher = 0
for blorg in lines:
  parts = [blorg[b:b+1] for b in range(0, len(blorg), 1)]
  eee = ''.join(parts[0:3])
  aaa= ''.join(parts[3:6])
  program.append(eee)
  program.append(aaa)
print("splitted program:", program)

datapointer = 0
pc = 0
aae = ''
fakepc = 0

print("starting code exexcution")
while str(program[pc]) != "111" and pc + 1 <= len(program) -1:
  aae = program[pc]
  fakepc = str(round(int(pc/2 +1)))
  print("instruction", fakepc, pc)
  print("code:", program[pc] + program[pc + 1])
  pc += 1
  eea = program[pc]
  fakepc = str(round(int(pc/2 +1)))
  
  if aae == "100":
    if eea == "11":
      brancher = pc
      print("branch set at instruction", fakepc)
      print("skipping ahead to end of branch")
      while ( str(program[pc]) + str(program[pc + 1]) ) != "10000":
        pc += 1
        fakepc = str(round(int(pc/2 +1)))
        if pc/2 == round(int(pc/2)):
          if int(program[pc] + program[pc + 1]) != 10000:
            print("skipping instruction", str(fakepc) + ".", "code:", str(program[pc] + program[pc + 1]))
          else:
            print("found branch end at instruction", fakepc + ".", "code:", program[pc] + program[pc + 1])
      continue
    elif eea == "00":
      pc += 1
      continue
  elif aae == "000":
    if eea == "00":
      datapointer -= 1
    elif eea == "10":
      datapointer += 1
    elif eea == "01":
      datapointer -= 2
    elif eea == "11":
      datapointer += 2
  elif aae == "001":
    if eea == "00" or eea == "11":
      if data[datapointer] == 1:
        data[datapointer] = 0
      elif data[datapointer] == 0:
        data[datapointer] = 1
    elif eea == "01":
      print("set bit", str(datapointer), "to 1")
      data[datapointer] = 1
    elif eea == "10":
      data[datapointer] = 0
    pc += 1
  elif aae == "010":
    print("DISPLAYING:", data[datapointer])
    pc += 1
  elif aae == "101":
    number = str(data[datapointer]) + str(data[datapointer])
    print("does", eea, "equal", number + "?")
    if number == eea:
      print("branch time")
      pc = brancher + 1
      fakepc = str(round(int(pc/2 +1)))
      print("going to instruction", fakepc)
      print(str(pc), str(fakepc))
  wait = input()
print("stopped code execution")
