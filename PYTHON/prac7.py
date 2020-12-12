def threeNumberSort(array, order):
    # Write your code here.
    fV = order[0]
    sV = order[1]

    fi, si, ti = 0, 0, len(array)-1

    while si <= ti:
        val = array[si]

        if val == fV:
            array[si], array[fi] = array[fi], array[si]
            fi += 1
            si += 1
        elif val == sV:
            si += 1
        else:
            array[si], array[ti] = array[ti], array[si]
            ti -= 1
    return array
