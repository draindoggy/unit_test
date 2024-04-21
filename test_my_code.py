import unittest
import io

def generate_spiral_matrix(n):
    a = [[0] * n for _ in range(n)]
    count = 0
    for i in range(n):
        count += 1
        a[0][i] = count
    j = 0
    i = n - 1
    n -= 1
    while len(a) ** 2 != count:
        for k in range(n):
            j += 1
            count += 1
            a[j][i] = count
        for k in range(n):
            i -= 1
            count += 1
            a[j][i] = count
        for k in range(n - 1):
            j -= 1
            count += 1
            a[j][i] = count
        for k in range(n - 1):
            i += 1
            count += 1
            a[j][i] = count
        n -= 2
    return a

class TestSpiralMatrix(unittest.TestCase):

    def test_generate_spiral_matrix(self):
        expected_matrix = [[1, 2, 3], [8, 9, 4], [7, 6, 5]]

        generated_matrix = generate_spiral_matrix(3)

        self.assertEqual(generated_matrix, expected_matrix)

if __name__ == '__main__':
    unittest.main()