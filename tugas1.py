import math

# Sistem persamaan:
# f1(x,y) = x^2 + xy - 10 = 0
# f2(x,y) = y + 3xy^2 - 57 = 0

# Nilai awal
x0, y0 = 1.5, 3.5
epsilon = 0.000001
max_iter = 100

print("="*80)
print("Rifat Gibran Widiyanto")
print("NIM: 21120123140179")
print("PENYELESAIAN SISTEM PERSAMAAN NONLINEAR")
print("NIM 2 digit terakhir: 79 ")
print(f"Hasil Modulus dari 2 digit NIM terakhir:  {79 % 4}")
print("="*80)
print(f"Sistem persamaan:")
print(f"f1(x,y) = x² + xy - 10 = 0")
print(f"f2(x,y) = y + 3xy² - 57 = 0")
print(f"\nTebakan awal: x0 = {x0}, y0 = {y0}")
print(f"Epsilon: {epsilon}")
print("="*80)

# ============================================================================
# FUNGSI ITERASI g1B dan g2B (Halaman 6)
# g1B: x = sqrt(10 - xy)
# g2B: y = sqrt((57 - y)/(3x))
# ============================================================================

def g1B(x, y):
    val = 10 - x*y
    return math.sqrt(abs(val)) if val >= 0 else -math.sqrt(abs(val))

def g2B(x, y):
    val = (57 - y) / (3*x)
    return math.sqrt(abs(val)) if val >= 0 else -math.sqrt(abs(val))

# ============================================================================
# 1. METODE ITERASI JACOBI dengan g1B dan g2B
# ============================================================================
print("\n" + "="*80)
print("1. METODE ITERASI JACOBI (g1B, g2B)")
print("="*80)
print(f"{'Iter':<6} {'x':<12} {'y':<12} {'deltaX':<12} {'deltaY':<12}")
print("-"*80)

x, y = x0, y0
print(f"{0:<6} {x:<12.6f} {y:<12.6f} {0.0:<12.6f} {0.0:<12.6f}")

for i in range(1, max_iter + 1):
    x_new = g1B(x, y)
    y_new = g2B(x, y)
    
    deltaX = abs(x_new - x)
    deltaY = abs(y_new - y)
    
    print(f"{i:<6} {x_new:<12.6f} {y_new:<12.6f} {deltaX:<12.6f} {deltaY:<12.6f}")
    
    if deltaX < epsilon and deltaY < epsilon:
        print(f"\nKonvergen pada iterasi ke-{i}")
        print(f"Solusi: x = {x_new:.6f}, y = {y_new:.6f}")
        break
    
    x, y = x_new, y_new
else:
    print("\nTidak konvergen dalam batas iterasi maksimum")

# ============================================================================
# 2. METODE ITERASI SEIDEL dengan g1B dan g2B
# ============================================================================
print("\n" + "="*80)
print("2. METODE ITERASI SEIDEL (g1B, g2B)")
print("="*80)
print(f"{'Iter':<6} {'x':<12} {'y':<12} {'deltaX':<12} {'deltaY':<12}")
print("-"*80)

x, y = x0, y0
print(f"{0:<6} {x:<12.6f} {y:<12.6f} {0.0:<12.6f} {0.0:<12.6f}")

for i in range(1, max_iter + 1):
    x_new = g1B(x, y)
    y_new = g2B(x_new, y)  # Menggunakan x_new (perbedaan dengan Jacobi)
    
    deltaX = abs(x_new - x)
    deltaY = abs(y_new - y)
    
    print(f"{i:<6} {x_new:<12.6f} {y_new:<12.6f} {deltaX:<12.6f} {deltaY:<12.6f}")
    
    if deltaX < epsilon and deltaY < epsilon:
        print(f"\nKonvergen pada iterasi ke-{i}")
        print(f"Solusi: x = {x_new:.6f}, y = {y_new:.6f}")
        break
    
    x, y = x_new, y_new
else:
    print("\nTidak konvergen dalam batas iterasi maksimum")

# ============================================================================
# 3. METODE NEWTON-RAPHSON
# ============================================================================
print("\n" + "="*80)
print("3. METODE NEWTON-RAPHSON")
print("="*80)

def f1(x, y):
    return x**2 + x*y - 10

def f2(x, y):
    return y + 3*x*y**2 - 57

def df1_dx(x, y):
    return 2*x + y

def df1_dy(x, y):
    return x

def df2_dx(x, y):
    return 3*y**2

def df2_dy(x, y):
    return 1 + 6*x*y

print(f"{'Iter':<6} {'x':<12} {'y':<12} {'deltaX':<12} {'deltaY':<12}")
print("-"*80)

x, y = x0, y0
print(f"{0:<6} {x:<12.6f} {y:<12.6f} {0.0:<12.6f} {0.0:<12.6f}")

for i in range(1, max_iter + 1):
    u = f1(x, y)
    v = f2(x, y)
    
    du_dx = df1_dx(x, y)
    du_dy = df1_dy(x, y)
    dv_dx = df2_dx(x, y)
    dv_dy = df2_dy(x, y)
    
    det = du_dx * dv_dy - du_dy * dv_dx
    
    if abs(det) < 1e-10:
        print("Determinan Jacobi mendekati nol!")
        break
    
    x_new = x - (u * dv_dy - v * du_dy) / det
    y_new = y + (u * dv_dx - v * du_dx) / det
    
    deltaX = abs(x_new - x)
    deltaY = abs(y_new - y)
    
    print(f"{i:<6} {x_new:<12.6f} {y_new:<12.6f} {deltaX:<12.6f} {deltaY:<12.6f}")
    
    if deltaX < epsilon and deltaY < epsilon:
        print(f"\nKonvergen pada iterasi ke-{i}")
        print(f"Solusi: x = {x_new:.6f}, y = {y_new:.6f}")
        break
    
    x, y = x_new, y_new
else:
    print("\nTidak konvergen dalam batas iterasi maksimum")

# ============================================================================
# 4. METODE SECANT
# ============================================================================
print("\n" + "="*80)
print("4. METODE SECANT")
print("="*80)

# Untuk metode Secant, kita butuh dua tebakan awal untuk setiap variabel
x_prev, y_prev = 1.0, 3.0
x_curr, y_curr = x0, y0

print(f"{'Iter':<6} {'x':<12} {'y':<12} {'deltaX':<12} {'deltaY':<12}")
print("-"*80)
print(f"{0:<6} {x_curr:<12.6f} {y_curr:<12.6f} {0.0:<12.6f} {0.0:<12.6f}")

for i in range(1, max_iter + 1):
    f1_curr = f1(x_curr, y_curr)
    f2_curr = f2(x_curr, y_curr)
    f1_prev = f1(x_prev, y_prev)
    f2_prev = f2(x_prev, y_prev)
    
    # Aproksimasi turunan dengan selisih hingga
    if abs(x_curr - x_prev) < 1e-10:
        x_prev = x_curr - 0.01
    if abs(y_curr - y_prev) < 1e-10:
        y_prev = y_curr - 0.01
        
    df1_approx = (f1_curr - f1_prev) / (x_curr - x_prev + 1e-10)
    df2_approx = (f2_curr - f2_prev) / (y_curr - y_prev + 1e-10)
    
    if abs(df1_approx) < 1e-10 or abs(df2_approx) < 1e-10:
        print("Turunan aproksimasi terlalu kecil!")
        break
    
    x_new = x_curr - f1_curr / df1_approx
    y_new = y_curr - f2_curr / df2_approx
    
    deltaX = abs(x_new - x_curr)
    deltaY = abs(y_new - y_curr)
    
    print(f"{i:<6} {x_new:<12.6f} {y_new:<12.6f} {deltaX:<12.6f} {deltaY:<12.6f}")
    
    if deltaX < epsilon and deltaY < epsilon:
        print(f"\nKonvergen pada iterasi ke-{i}")
        print(f"Solusi: x = {x_new:.6f}, y = {y_new:.6f}")
        break
    
    x_prev, y_prev = x_curr, y_curr
    x_curr, y_curr = x_new, y_new
else:
    print("\nTidak konvergen dalam batas iterasi maksimum")

# ============================================================================
# ANALISIS KONVERGENSI
# ============================================================================
print("\n" + "="*80)
print("ANALISIS KONVERGENSI")
print("="*80)

x_test, y_test = 2.0, 3.0  # Titik tetap

# Untuk g1B dan g2B
dg1B_dx = -y_test / (2 * math.sqrt(10 - x_test * y_test))
dg1B_dy = -x_test / (2 * math.sqrt(10 - x_test * y_test))
dg2B_dx = -(57 - y_test) / (6 * x_test**2 * math.sqrt((57 - y_test)/(3*x_test)))
dg2B_dy = -1 / (6 * x_test * math.sqrt((57 - y_test)/(3*x_test)))

sum1 = abs(dg1B_dx) + abs(dg1B_dy)
sum2 = abs(dg2B_dx) + abs(dg2B_dy)

print(f"\nPada titik (x,y) = ({x_test}, {y_test}):")
print(f"|∂g1B/∂x| + |∂g1B/∂y| = {sum1:.6f}")
print(f"|∂g2B/∂x| + |∂g2B/∂y| = {sum2:.6f}")
print(f"\nSyarat konvergen: kedua nilai < 1")
print(f"Fungsi g1B dan g2B: {'KONVERGEN' if sum1 < 1 and sum2 < 1 else 'TIDAK KONVERGEN'}")

print("\n" + "="*80)
print("PROGRAM SELESAI")
print("="*80)