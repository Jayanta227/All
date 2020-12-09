#this programme transposes musical notations written in the txt file and
#outputs in outfile

steps = input('enter number of semitones: ')
notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
with open('txt') as f:
    for line in f.readlines():
        in_arr = line.strip().split(' ');
        # print(line)
        for i in range(len(in_arr)):
            in_arr[i] = in_arr[i].strip()
            in_arr[i] = in_arr[i].capitalize()

        out_arr = []
        for i in in_arr:
            index = notes.index(i)
            if index+int(steps) > 11:
                out_arr.append(notes[index+int(steps)-12])
            else:
                out_arr.append(notes[index+int(steps)])

        with open('txtout', 'a') as outfile:
            outfile.writelines(str(out_arr)+'\n')

