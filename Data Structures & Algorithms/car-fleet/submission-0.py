class Solution(object):
    def carFleet(self, target, position, speed):
        if not position:
            return 0
        s = {}
        for i in range(len(position)):
            s[position[i]] = (target-position[i])/float(speed[i])
        l = sorted(position,reverse=True)
        count = 1
        fleet_time = s[l[0]]
        for i in range(1,len(l)):
            if s[l[i]]>fleet_time:
                fleet_time = s[l[i]]
                count+=1
        return count