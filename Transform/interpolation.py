class interpolation:

    def linear_interpolation(self, pt1, pt2, unknown):
        """Computes the linear interpolation for the unknown values using pt1 and pt2
        take as input
        pt1: known point pt1 and f(pt1) or intensity value
        pt2: known point pt2 and f(pt2) or intensity value
        unknown: take and unknown location
        return the f(unknown) or intentity at unknown"""

        # Write your code for linear interpolation here
        if (pt2[0]-pt1[0]) == 0:
            a = 0
        else:
            a = (pt2[0]-unknown[0])/(pt2[0]-pt1[0])
        if (pt2[0]-pt1[0]) == 0:
            b = 0
        else:
            b = (unknown[0]-pt1[0])/(pt2[0]-pt1[0])

        i = (a*pt1[2])+(b*pt2[2])

        return i

    def bilinear_interpolation(self, pt1, pt2, pt3, pt4, unknown):
        """Computes the linear interpolation for the unknown values using pt1 and pt2
        take as input
        pt1: known point pt1 and f(pt1) or intensity value
        pt2: known point pt2 and f(pt2) or intensity value
        pt1: known point pt3 and f(pt3) or intensity value
        pt2: known point pt4 and f(pt4) or intensity value
        unknown: take and unknown location
        return the f(unknown) or intensity at unknown"""

        # Write your code for bilinear interpolation here
        # May be you can reuse or call linear interpolation method to compute this task
        first = self.linear_interpolation(pt1, pt3, unknown)
        second = self.linear_interpolation(pt2, pt4, unknown)

        a, b = 0, 0

        if (pt2[1]-pt1[1]) != 0:
            a = (pt2[1]-unknown[1])/(pt2[1]-pt1[1])

        if (pt2[1]-pt1[1]) != 0:
            b = (unknown[1]-pt1[1])/(pt2[1]-pt1[1])

        i = (a*first)+(b*second)

        return i
