from math import sqrt, ceil

# Магический квадрат
def nearest_square ( n ):
    #sq =  int ( sqrt ( ceil ( sqrt ( n ) ) ** 2 ) )
    sq = ceil ( sqrt ( n ) )
    if ( sq%2 == 0 ): # Только нечётные
        sq += 1
    return sq

def create_magic_square ( num ):
    N = nearest_square ( num )
    arr = [ [ '' for x in range(N) ] for y in range(N) ] 

    n = 1
    i, j = 0, N//2
    
    while n <= N**2:
        arr[ i ][ j ] = n
        n += 1
        newi, newj = (i-1) % N, (j+1)% N
        if arr[ newi ][ newj ]:
            i += 1
        else:
            i, j = newi, newj
    return [ arr, N ]

def magic_square ( s, rev ):
    l = len ( s )
    output = ''
    spec_char = '_'
    square = create_magic_square ( l )

    Matrix, size = square[ 0 ], square[ 1 ]
    toCip = s + ( spec_char * ( size**2 - l ) )

    if rev:
        output = [ '' for x in range ( size**2 ) ]
        toCip = [ s[ i:i+size ] for i in range(0, len(s), size)]

    for i in range ( size ):
        for j in range ( size ):
            if rev:
                output[ Matrix[ i ][ j ] - 1 ] = toCip[ i ][ j ]
            else:
                output += toCip[ Matrix[ i ][ j ] - 1 ]

    return ''.join ( output ).replace ( spec_char, '' ) if rev else output