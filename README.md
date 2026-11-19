# CI/CD rollback demo

Program Python sederhana untuk memperlihatkan CI/CD yang menjalankan test otomatis dan rollback yang tetap tercatat di Git.

## Versi 1

`final_price()` menghitung harga sesudah diskon. Jalankan secara lokal:

```bash
python -m unittest -v
python app.py
```

Target hasil test: seluruh test lulus.

## Skenario versi 2 yang salah

Ubah satu baris di `app.py` dari:

```python
return round(price * (1 - discount_percent / 100), 2)
```

menjadi:

```python
return round(price * (1 + discount_percent / 100), 2)
```

Test diskon akan gagal: harga Rp100.000 dengan diskon 10% keliru menjadi Rp110.000, padahal seharusnya Rp90.000. GitHub Actions akan menandai push versi 2 sebagai gagal.

## Rollback yang terlacak

Jangan gunakan `git reset --hard` untuk demonstrasi ini karena ia menghapus jejak commit dari branch lokal. Setelah commit V2 yang salah dipush dan CI gagal, gunakan:

```bash
git revert <hash-commit-v2>
git push origin main
```

Git membuat commit baru yang membatalkan perubahan V2. History tetap menunjukkan V1, commit V2 yang gagal, dan commit rollback. CI pada commit rollback seharusnya kembali lulus.
