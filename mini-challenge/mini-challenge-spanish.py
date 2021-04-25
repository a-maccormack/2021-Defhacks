f = open("socdist1.in", "r")

N = int(f.readline())
s = f.readline()

f.close()

# // Devuelve el numero mas grande entre dos 1s y su indice


def find_largest_interior_gap(s):
    biggest_gap = 0
    current_start = -1
    gap_start = 0
    for i in range(N):
        if s[i] == "1":
            current_start = i
        else:
            if i-current_start > biggest_gap and current_start != -1:
                biggest_gap = i-current_start
                gap_start = current_start
    return gap_start, biggest_gap + 1

# Devuelve la distancia más pequeña entre dos 1s


def find_smallest_interior_gap(s):
    s = s.strip("0")
    s = s[1:-1]
    s = s.split("1")
    smallest_gap = len(min(s)) + 1
    return smallest_gap

# Devuelve el espacio más chico después de agregar a un estudiante al grupo más grande


def try_student_in_largest_gap(s):
    gap_start, largest_gap = find_largest_interior_gap(s)
    if largest_gap >= 2:
        s = s[:gap_start + largest_gap//2] + "1" + \
            s[gap_start + largest_gap//2 + 1:]
        return find_smallest_interior_gap(s)
    return -1  # sin espacio!


answer = 0

# Escenario 1.poner a los dos estudiantes en el espacio interno mas grande
gap_start, largest_gap = find_largest_interior_gap(s)
if largest_gap >= 3:
    temp_s = s
    temp_s = temp_s[:gap_start + largest_gap // 3] + \
        "1" + temp_s[gap_start + largest_gap // 3 + 1:]
    temp_s = temp_s[:gap_start + largest_gap * 2 // 3] + \
        "1" + temp_s[gap_start + largest_gap * 2 // 3 + 1:]
    answer = max(answer, find_smallest_interior_gap(temp_s))


# Escenario 2. poner estudiantes en las dos puntas
if s[0] == "0" and s[-1] == "0":
    temp_s = s
    temp_s = "1" + temp_s[1:-1] + "1"
    answer = max(answer, find_smallest_interior_gap(temp_s))


# Escenario 3. estudiantes a la izquierda + estudiantes en el grupo interior más grande
if s[0] == "0":
    temp_s = s
    temp_s = "1" + temp_s[1:]
    answer = max(answer, try_student_in_largest_gap(temp_s))


# Escenario 4. Estudiantes a la derecha + estudiantes en el grupo interior más grande
if s[-1] == "0":
    temp_s = s
    temp_s = temp_s[:-1] + "1"
    answer = max(answer, try_student_in_largest_gap(temp_s))


# Escenario 5. Estudiantes en el espacio interior mas grande.  Hecho dos veces.
if largest_gap >= 2:
    temp_s = s
    temp_s = temp_s[:gap_start + largest_gap // 2] + \
        "1" + temp_s[gap_start + largest_gap // 2 + 1:]
    answer = max(answer, try_student_in_largest_gap(temp_s))


f = open("socdist1.out", "w")

f.write(str(answer))

f.close()
