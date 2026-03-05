# Given an array of intervals where intervals[i] = [starti, endi], 
# merge all overlapping intervals, and return an array of the 
# non-overlapping intervals that cover all the intervals in the input.

def merge(intervals):
     # Assumption made that all sub-lists are:
          # ordered [start, finish], s.t. intervals are "directional" ([19, 4] & [3, 8] do not overlap due to directionality)

     # sorted() to sort the list (sorted by sublists' first element in ascending order)
     intervals = sorted(intervals)
     overlapList = []

     # Split by "direction"
     asc = []
     des = []
     for i in range(len(intervals)):
          if min(intervals[i]) == intervals[i][0]:
               asc.append(intervals[i])
          else:
               des.append(intervals[i])
     
     ascOver = [asc[0]] # need [asc[0]] *NOT* asc[0] because then we have a list of list elements, not a list of two elements
     for up_interval in asc[1:]:
          last = ascOver[-1] # set last as the last list element from our list of lists

          # compare item at index 0 (min. element) of current interation with index 1 (max. element) of the last element of our condensed list
          # of intervals
          if up_interval[0] <= last[1]:
               last[1] = max(up_interval[1], last[1]) # update the maximum of the overlapping interval in our condensed list
          else:
               ascOver.append(up_interval) # if there is no overlap, then we cannot condense, so we add to our condensed list

     desOver = [des[0]] # likewise, as line 259
     for low_interval in des[1:]: # do I need to differentiate up_interval and low_interval? it doesn't reset on it's own in the second loop
          last = desOver[-1]

          # compare the minimum element of current iteration to the maximum element of our condensed list of intervals
          if low_interval[1] <= last[0]:
               last[0] = max(low_interval[0], last[0])
          else:
               ascOver.append(low_interval)

     overlapList = sorted(ascOver + desOver)

     return overlapList