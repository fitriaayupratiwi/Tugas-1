import streamlit as st

st.set_page_config(page_title="Aplikasi Multi Fitur", layout="centered")

st.title("🔢 Aplikasi Multi Fitur dengan Streamlit")

menu = st.sidebar.selectbox(
    "Pilih Fitur:",
    ["Kalkulator", "Konversi Suhu", "Deret Fibonacci"]
)

# ============================
# 1. Kalkulator
# ============================
if menu == "Kalkulator":
    st.header("🧮 Kalkulator Sederhana")
    a = st.number_input("Masukkan angka pertama", value=0.0)
    b = st.number_input("Masukkan angka kedua", value=0.0)
    operator = st.selectbox("Pilih Operator", ["+", "-", "×", "÷"])

    if st.button("Hitung"):
        if operator == "+":
            hasil = a + b
        elif operator == "-":
            hasil = a - b
        elif operator == "×":
            hasil = a * b
        elif operator == "÷":
            if b != 0:
                hasil = a / b
            else:
                hasil = "Error: Pembagian dengan nol"
        st.success(f"Hasil: {hasil}")

# ============================
# 2. Konversi Suhu
# ============================
elif menu == "Konversi Suhu":
    st.header("🌡️ Konversi Suhu")

    pilihan_input = st.selectbox("Pilih satuan input", ["Celcius", "Reamur", "Fahrenheit"])
    nilai = st.number_input(f"Masukkan nilai suhu dalam {pilihan_input}", value=0.0)

    if st.button("Konversi"):
        if pilihan_input == "Celcius":
            celcius = nilai
            reamur = (4/5) * celcius
            fahrenheit = (9/5) * celcius + 32
        elif pilihan_input == "Reamur":
            celcius = (5/4) * nilai
            reamur = nilai
            fahrenheit = (9/4) * nilai + 32
        elif pilihan_input == "Fahrenheit":
            celcius = (5/9) * (nilai - 32)
            reamur = (4/9) * (nilai - 32)
            fahrenheit = nilai

        st.write(f"🌡️ Celcius: {celcius:.2f} °C")
        st.write(f"🌡️ Reamur: {reamur:.2f} °R")
        st.write(f"🌡️ Fahrenheit: {fahrenheit:.2f} °F")

# ============================
# 3. Deret Fibonacci
# ============================
elif menu == "Deret Fibonacci":
    st.header("🔢 Deret Fibonacci")

    n = st.number_input("Masukkan jumlah suku Fibonacci", min_value=1, step=1)

    def fibonacci(n):
        deret = []
        a, b = 0, 1
        for _ in range(n):
            deret.append(a)
            a, b = b, a + b
        return deret

    if st.button("Generate"):
        hasil = fibonacci(int(n))
        st.success(f"Deret Fibonacci hingga {n} suku:")
        st.write(hasil)
