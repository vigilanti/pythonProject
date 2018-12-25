"""
Project for Week 4 of "Python Data Representations".
Find differences in file contents.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

IDENTICAL = -1

def singleline_diff(line1, line2):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
    Output:
      Returns the index where the first difference between
      line1 and line2 occurs.

      Returns IDENTICAL if the two lines are the same.
    """
    maximum=0
    if(len(line1)<len(line2)):
        maximum=len(line1)
    else:
        maximum=len(line2)
    for index in range(0,maximum):
        if(line1[index]!=line2[index]):
            return index
        if (index == maximum-1 and len(line1)!=len(line2)):
            return index+1
    if(len(line1)==0 and len(line2)==0):
        return IDENTICAL
    elif (len(line1)==0 or len(line2)==0):
        return 0
    return IDENTICAL


def singleline_diff_format(line1, line2, idx):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
      idx   - index at which to indicate difference
    Output:
      Returns a three line formatted string showing the location
      of the first difference between line1 and line2.

      If either input line contains a newline or carriage return,
      then returns an empty string.

      If idx is not a valid index, then returns an empty string.
    """
    str_equals=""
    index1=0
    while index1<idx:
        str_equals+='='
        index1+=1
    if(len(line1)<idx or len(line2)<idx):
        return ""
    if(idx>=0):
        return (line1+"\n"+str_equals+"^\n"+line2+"\n")
    return ""


def multiline_diff(lines1, lines2):
    """
    Inputs:
      lines1 - list of single line strings
      lines2 - list of single line strings
    Output:
      Returns a tuple containing the line number (starting from 0) and
      the index in that line where the first difference between lines1
      and lines2 occurs.

      Returns (IDENTICAL, IDENTICAL) if the two lists are the same.
    """
    maximum=0
    if (len(lines1)<len(lines2)):
        maximum=len(lines1)
    else:
        maximum=len(lines2)
    for index in range(0,maximum):
        if(singleline_diff(lines1[index],lines2[index])>=0):
            return (index,singleline_diff(lines1[index],lines2[index]))
    if (len(lines1)>maximum or len(lines2)>maximum):
        return(maximum,0)
    return (IDENTICAL, IDENTICAL)


def get_file_lines(filename):
    """
    Inputs:
      filename - name of file to read
    Output:
      Returns a list of lines from the file named filename.  Each
      line will be a single line string with no newline ('\n') or
      return ('\r') characters.

      If the file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    file_list=[]
    filedata=open(filename,"rt")
    for line in filedata:
        file_list.append(line.rstrip('\n'))
    return file_list


def file_diff_format(filename1, filename2):
    """
    Inputs:
      filename1 - name of first file
      filename2 - name of second file
    Output:
      Returns a four line string showing the location of the first
      difference between the two files named by the inputs.

      If the files are identical, the function instead returns the
      string "No differences\n".

      If either file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    line1=[]
    line2=[]
    file1 = open(filename1, 'r')
    file2 = open(filename2, 'r')
    for line in file1:
        line1.append(line.rstrip('\n'))
    for line in file2:
        line2.append(line.rstrip('\n'))
    maximum=0
    if(len(line1)<len(line2)):
        maximum=len(line1)
    else:
        maximum=len(line2)
    for index in range(0,maximum):
        if singleline_diff(line1[index],line2[index])!=-1:
            buffer=singleline_diff(line1[index],line2[index])
            str_equals=""
            index1=0
            while index1<buffer:
                str_equals+='='
                index1+=1
            return("Line "+str(index)+":\n"+line1[index]+"\n"+str_equals+"^\n"+line2[index]+"\n")
    if(len(line1)==0 and len(line2)==0):
        return "No differences\n"
    elif(len(line2)==0):
        return("Line 0:\n"+line1[0]+"\n^\n\n")
    return "No differences\n"
