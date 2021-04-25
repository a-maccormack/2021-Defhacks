#include <iostream>
#include <fstream>
using namespace std;

// Devuelve el numero mas grande entre dos 1s y su indice
int find_largest_interior_gap(string s, int &gap_start)
{
  int biggest_gap = 0, current_start = -1, N = s.length();
  for (int i = 0; i < N; i++)
    if (s[i] == '1')
    {
      if (current_start != -1 && i - current_start > biggest_gap)
      {
        biggest_gap = i - current_start;
        gap_start = current_start;
      }
      current_start = i;
    }
  return biggest_gap;
}

// Devuelve la distancia más pequeña entre dos 1s
int find_smallest_interior_gap(string s)
{
  int smallest_gap = 1000000000, current_start = -1, N = s.length();
  for (int i = 0; i < N; i++)
    if (s[i] == '1')
    {
      if (current_start != -1 && i - current_start < smallest_gap)
        smallest_gap = i - current_start;
      current_start = i;
    }
  return smallest_gap;
}

// Devuelve el espacio más chico después de agregar a un estudiante al grupo más grande
int try_student_in_largest_gap(string s)
{
  int gap_start, largest_gap = find_largest_interior_gap(s, gap_start);
  if (largest_gap >= 2)
  {
    s[gap_start + largest_gap / 2] = '1';
    return find_smallest_interior_gap(s);
  }
  return -1; // sin espacio!
}

int main(void)
{
  ifstream fin("socdist1.in");
  int N;
  string s, temp_s;
  fin >> N >> s;
  ofstream fout("socdist1.out");
  int answer = 0;

  // Escenario 1.poner a los dos estudiantes en el espacio interno mas grande
  int gap_start, largest_gap = find_largest_interior_gap(s, gap_start);
  if (largest_gap >= 3)
  {
    temp_s = s;
    temp_s[gap_start + largest_gap / 3] = '1';
    temp_s[gap_start + largest_gap * 2 / 3] = '1';
    answer = max(answer, find_smallest_interior_gap(temp_s));
  }

  // Escenario 2. poner estudiantes en las dos puntas
  if (s[0] == '0' && s[N - 1] == '0')
  {
    temp_s = s;
    temp_s[0] = temp_s[N - 1] = '1';
    answer = max(answer, find_smallest_interior_gap(temp_s));
  }

  // Escenario 3. estudiantes a la izquierda + estudiantes en el grupo interior más grande
  if (s[0] == '0')
  {
    temp_s = s;
    temp_s[0] = '1';
    answer = max(answer, try_student_in_largest_gap(temp_s));
  }

  // Escenario 4. Estudiantes a la derecha + estudiantes en el grupo interior más grande
  if (s[N - 1] == '0')
  {
    temp_s = s;
    temp_s[N - 1] = '1';
    answer = max(answer, try_student_in_largest_gap(temp_s));
  }

  // Escenario 5. Estudiantes en el espacio interior mas grande.  Hecho dos veces.
  if (largest_gap >= 2)
  {
    temp_s = s;
    temp_s[gap_start + largest_gap / 2] = '1';
    answer = max(answer, try_student_in_largest_gap(temp_s));
  }

  fout << answer << "\n";
  return 0;
}
