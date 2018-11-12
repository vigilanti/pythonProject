"""
	This program will find a peak in one dimension array
"""

def peak(element,start,stop):
		mid=(start+stop)//2
		if element[mid-1]<=element[mid] and element[mid+1]<=element[mid]:
			return mid
		elif element[mid-1]>element[mid]:
			return peak(element,start,mid)
		elif element[mid+1]>element[mid]:
			return peak(element,mid+1,stop)
		return -1

print(peak([1,2,1,5,4,4,7],0,7))
